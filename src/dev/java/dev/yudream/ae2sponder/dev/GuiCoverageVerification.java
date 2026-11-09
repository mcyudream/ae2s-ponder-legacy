package dev.yudream.ae2sponder.dev;

import ae2.client.gui.AEBaseGui;
import ae2.client.gui.style.GuiStyleManager;
import dev.yudream.ae2sponder.compat.AE2SGuiCatalog;
import java.util.List;
import net.createmod.ponder.api.gui.GuiTutorial;
import net.createmod.ponder.client.guitutorial.GuiDemoScreen;
import net.createmod.ponder.client.guitutorial.GuiTutorialDrawing;
import net.createmod.ponder.client.guitutorial.GuiTutorials;
import net.minecraft.client.Minecraft;
import net.minecraft.item.Item;
import net.minecraft.util.ResourceLocation;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;

/** Every catalog entry: actual AE2S classes/styles/resources and independent bilingual framebuffer playback. */
final class GuiCoverageVerification {
    private final Minecraft mc=Minecraft.getMinecraft();
    private final List<AE2SGuiCatalog.Entry> entries=new AE2SGuiCatalog().all().stream()
        .sorted(java.util.Comparator.comparing(AE2SGuiCatalog.Entry::id)).toList();
    private int index,language,phase,operationCapture;
    private final dev.yudream.ae2sponder.compat.AE2SGuiDemoRenderer completeDemo=new dev.yudream.ae2sponder.compat.AE2SGuiDemoRenderer();

    boolean tick(ClientVerification host)throws Exception {
        if(index>=entries.size()) {
            if(language++==0){index=phase=0;return false;}
            Display.setDisplayMode(new DisplayMode(1280,720));mc.resize(1280,720);mc.displayGuiScreen(null);return true;
        }
        String code=language==0?"en_us":"zh_cn";
        if(!code.equals(mc.getLanguageManager().getCurrentLanguage().getLanguageCode())) {
            mc.gameSettings.language=code;mc.getLanguageManager().setCurrentLanguage(mc.getLanguageManager().getLanguage(code));mc.refreshResources();
        }
        var entry=entries.get(index);GuiTutorial lesson=GuiTutorials.resolve("ae2s_ponder:"+entry.id());
        if(phase==0) {
            host.check(AEBaseGui.class.isAssignableFrom(Class.forName(entry.screen(),false,getClass().getClassLoader())),entry.id()+": native AE2S GUI class exists");
            host.check(GuiTutorials.forComponent(lesson.components().get(0)).stream().anyMatch(t->t.id().equals(lesson.id())),entry.id()+": GUI reachable from its actual component");
            for(var component:lesson.components())host.check(Item.REGISTRY.containsKey(component),entry.id()+": native component exists: "+component);
            if(!entry.style().isEmpty())host.check(GuiStyleManager.loadStyleDoc(entry.style())!=null,entry.id()+": native style loads and validates");
            for(var step:lesson.steps()) {
                host.check(!GuiTutorialDrawing.text(step.title()).startsWith("ae2s_ponder.")&&!GuiTutorialDrawing.text(step.text()).startsWith("ae2s_ponder."),entry.id()+": "+code+" operation text resolves");
                for(var action:step.demo())if(!action.item().isEmpty())host.check(Item.REGISTRY.containsKey(new ResourceLocation(action.item())),entry.id()+": demo resource exists: "+action.item());
            }
            if(!lesson.texture().isEmpty())try(var resource=mc.getResourceManager().getResource(new ResourceLocation(lesson.texture()))) {
                host.check(javax.imageio.ImageIO.read(resource.getInputStream())!=null,entry.id()+": installed AE2S texture decodes");
            }
            var demo=new GuiDemoScreen(lesson,()->mc.displayGuiScreen(null),false);mc.displayGuiScreen(demo);
            host.check(demo.machineBounds().y()+demo.machineBounds().height()<=demo.height-52,entry.id()+": complete appearance stays above the footer hint and playback controls");
            host.check(completeDemo.slotCount(entry.id())+completeDemo.widgetCount(entry.id())>0||!lesson.texture().isEmpty(),entry.id()+": complete appearance has primitives independent of highlights");
            for(int operationIndex=0;operationIndex<lesson.steps().size();operationIndex++) {
                var operation=lesson.steps().get(operationIndex);demo.session().seek(operationIndex,25);
                var complete=completeDemo.layout(demo.session());
                if(entry.id().equals("terminal_settings")&&operationIndex%3==0) {
                    host.check(complete.target("widget.rememberCheckbox")!=null&&complete.target("widget.clearExternalCheckbox")==null,entry.id()+": internal and external search options remain mutually exclusive");
                }
                if(entry.id().equals("pattern_modifier")) {
                    host.check((complete.target("widget.amount_0")!=null)==(operationIndex!=2)
                        &&(complete.target("widget.replace")!=null)==(operationIndex==2)
                        &&complete.target("widget.property_0")==null,entry.id()+": mode-specific controls and highlights share visibility");
                }
                if(entry.id().equals("craft_cpu_list")) {
                    var first=complete.target("cpu.row.0");var search=complete.target("widget.search");
                    host.check(first.y()>=search.y()+search.height(),entry.id()+": first CPU row stays below the native search header");
                }
                if(entry.id().equals("cell_terminal")) {
                    host.check(java.util.stream.IntStream.range(0,8).allMatch(i->complete.target("widget.cellTab"+i)!=null),entry.id()+": all native top tabs remain inside the complete viewport");
                }
                var r=net.createmod.ponder.client.guitutorial.GuiTutorialDrawing.demoTarget(demo.session(),operation.target());
                host.check(r!=null&&r.x()>=0&&r.y()>=0&&r.x()+r.width()<=lesson.width()&&r.y()+r.height()<=lesson.height(),entry.id()+": highlight remains inside the complete model: "+operation.target());
                for(float scale:new float[]{.45f,.75f,1f,1.5f}) {
                    var scaled=GuiTutorialDrawing.scaled(r,17,23,scale);
                    host.check(scaled.x()+scaled.width()==17+Math.round((r.x()+r.width())*scale)&&scaled.y()+scaled.height()==23+Math.round((r.y()+r.height())*scale),entry.id()+": scaled highlight preserves primitive edges at "+scale);
                }
            }
            demo.session().playing(false);demo.session().seekAbsolute(Math.min(demo.session().lastTick(),180));
            var mark=lesson.targets().get(demo.session().step().target()).bounds();
            host.check(mark.width()>0&&mark.height()>0,entry.id()+": visible authored operation target");
            host.screenshot("coverage-"+entry.id()+"-"+code+".png");phase++;
        } else if(phase==1) {
            var demo=(GuiDemoScreen)mc.currentScreen;demo.session().seekAbsolute(demo.session().lastTick());
            String end=demo.session().demoSlot(demo.session().step().target()).toString();
            demo.session().seekAbsolute(0);demo.session().seekAbsolute(demo.session().lastTick());
            host.check(end.equals(demo.session().demoSlot(demo.session().step().target()).toString()),entry.id()+": independent seek/replay reconstructs final state");
            if(index%12==0) {
                Display.setDisplayMode(new DisplayMode(640,480));mc.resize(640,480);host.screenshot("coverage-small-"+entry.id()+"-"+code+".png");phase++;
            } else {phase=3;operationCapture=0;}
        } else if(phase==2) {Display.setDisplayMode(new DisplayMode(1280,720));mc.resize(1280,720);phase=3;operationCapture=0;}
        else {
            if(operationCapture<lesson.steps().size()) {
                var demo=(GuiDemoScreen)mc.currentScreen;demo.session().seek(operationCapture,35);
                host.screenshot("operation-"+entry.id()+"-"+(operationCapture++)+"-"+code+".png");
            } else {index++;phase=0;}
        }
        return false;
    }
}
