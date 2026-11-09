package dev.yudream.ae2sponder.compat;

import ae2.client.gui.Icon;
import ae2.client.gui.style.*;
import ae2.client.gui.widgets.AE2Button;
import ae2.client.gui.widgets.AETextField;
import ae2.client.gui.widgets.AECheckbox;
import ae2.client.gui.widgets.NumberEntryWidget;
import ae2.client.gui.NumberEntryType;
import ae2.client.gui.widgets.SimpleIconButton;
import ae2.client.gui.widgets.TabButton;
import ae2.client.Point;
import ae2.core.localization.GuiText;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.awt.Rectangle;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;
import net.createmod.ponder.api.gui.GuiTutorial;
import net.createmod.ponder.api.gui.GuiDemoLayout;
import net.createmod.ponder.client.guitutorial.GuiTutorialDrawing;
import net.createmod.ponder.api.gui.GuiDemoState;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.Gui;
import net.minecraft.client.renderer.GlStateManager;
import net.minecraft.client.renderer.RenderHelper;
import net.minecraft.client.resources.I18n;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.util.ResourceLocation;
import net.minecraft.util.text.TextComponentString;

/** Complete AE2S appearance, with independent sample state. No native GUI/container is created. */
public final class AE2SGuiDemoRenderer {
    private static final class Widget {
        String kind, icon, label, text;
        int x,y,width,height;
    }
    private static final class Appearance {
        int width,height,x,y,upgrades;
        String style,screen,texture;
        Map<String,Widget> widgets;
        Map<String,int[]> slots;
        List<String> toolbar;
    }
    private final Map<String,Appearance> appearances;
    private final Map<String,GuiStyle> styles=new HashMap<>();
    private final Map<String,Icon> icons=new HashMap<>();
    private record NumberDemo(NumberEntryWidget widget,List<net.minecraft.client.gui.GuiButton> buttons) {}
    private final Map<String,NumberDemo> numbers=new HashMap<>();
    private final Map<String,AETextField> fields=new HashMap<>();
    private final Minecraft mc=Minecraft.getMinecraft();

    public AE2SGuiDemoRenderer() {
        try(var resource=mc.getResourceManager().getResource(new ResourceLocation("ae2s_ponder","ponder/gui/appearances.json"));
            var reader=new InputStreamReader(resource.getInputStream(),StandardCharsets.UTF_8)) {
            appearances=new Gson().fromJson(reader,new TypeToken<LinkedHashMap<String,Appearance>>(){}.getType());
        }catch(java.io.IOException failure){throw new IllegalStateException("Cannot load complete AE2S GUI appearances",failure);}
    }

    public int widgetCount(String id){return appearances.get(id).widgets.size()+appearances.get(id).toolbar.size();}
    public int slotCount(String id){return appearances.get(id).slots.size();}
    /** Ponder owns coordinate transforms, clipping, layers and highlight resolution. */
    public GuiDemoLayout layout(GuiDemoState session) {
        var tutorial=session.tutorial();var a=appearances.get(tutorial.id().getPath());if(a==null)return null;
        var style=a.style.isEmpty()?null:styles.computeIfAbsent(a.style,GuiStyleManager::loadStyleDoc);
        var builder=GuiDemoLayout.builder(tutorial.width(),tutorial.height());var root=builder.root();
        tutorial.targets().forEach((key,target)->root.region(key,target.bounds()));
        var content=root.group(a.x,a.y);
        content.node("",new GuiTutorial.Rect(0,0,a.width,a.height),GuiDemoLayout.BACKGROUND,()->background(a,style,session));
        if(!a.toolbar.isEmpty())content.node("widget.verticalToolbar",new GuiTutorial.Rect(-17,1,20,a.toolbar.size()*22+2),GuiDemoLayout.PANEL,()->toolbar(a));
        if(a.upgrades>0)content.node("widget.upgrades",new GuiTutorial.Rect(a.width+1,0,29,a.upgrades*18+12),GuiDemoLayout.PANEL,()->upgrades(a));
        for(var entry:a.widgets.entrySet()) {
            String key="widget."+entry.getKey();var w=entry.getValue();
            boolean modal=w.kind.equals("colorwindow");
            if(!visible(a,session,entry.getKey())||(modal&&!session.step().target().equals(key))){root.hideTarget(key);continue;}
            int layer=modal?GuiDemoLayout.MODAL:Set.of("encoding","panel","cpulist","viewcells").contains(w.kind)?GuiDemoLayout.PANEL:GuiDemoLayout.CONTROL;
            content.node(key,new GuiTutorial.Rect(w.x,w.y,w.width,w.height),layer,()->drawWidget(a,style,session,entry.getKey(),w));
            if(entry.getKey().equals("progressBar"))content.region("progress",new GuiTutorial.Rect(w.x,w.y,w.width,w.height));
        }
        for(var slot:a.slots.entrySet()) {
            if(a.screen.equals("GuiPatternModifier")&&slot.getKey().contains("PATTERN_MODIFIER_")) {
                if(session.stepIndex()!=2||!slot.getKey().contains("REPLACE_")){root.hideTarget(slot.getKey());continue;}
            }
            int[] r=slot.getValue();
            content.node(slot.getKey(),new GuiTutorial.Rect(r[0],r[1],r[2],r[3]),GuiDemoLayout.SLOT,()->{
                icon("SLOT_BACKGROUND",r[0]-1,r[1]-1,18,18);
                GuiTutorial.Stack stack=session.demoSlot(slot.getKey());
                if(stack.item().isEmpty()&&slot.getKey().startsWith("repo.")) {
                    int index=Integer.parseInt(slot.getKey().substring(5));
                    if(index<8)stack=new GuiTutorial.Stack(SAMPLE_ITEMS[index],64-index*4);
                }
                item(stack,r[0],r[1]);
            });
        }
        if(style!=null)for(var entry:style.getText().entrySet()) {
            String key=entry.getKey();var text=entry.getValue();
            if(key.equals("entriesShown")||text.getPosition()==null||(a.screen.equals("GuiCraftError")&&key.equals("dialog_title"))||(a.screen.equals("GuiTerminalSettings")&&!key.equals("dialog_title")&&session.stepIndex()%3!=1)){root.hideTarget("text."+key);continue;}
            String value=displayText(a,text,key,session);var r=AE2SGuiTextGeometry.bounds(text,new Rectangle(0,0,a.width,a.height),value);
            if(r!=null)content.node("text."+key,r,GuiDemoLayout.TEXT,()->drawTextEntry(a,style,session,key,text));
            else root.hideTarget("text."+key);
        }
        if(a.screen.equals("GuiPatternAccessTerm")||a.screen.equals("GuiPEATerm"))patternAccessContent(content,a);
        if(a.screen.equals("GuiCraftConfirmCpuList"))cpuListContent(content);
        content.node("",new GuiTutorial.Rect(0,0,a.width,a.height),GuiDemoLayout.CONTENT,()->dynamicContent(a,session));
        for(var entry:tutorial.targets().entrySet())if(entry.getValue().type()==GuiTutorial.TargetType.SLOT&&!a.slots.containsKey(entry.getKey())) {
            var r=entry.getValue().bounds();
            root.node(entry.getKey(),r,GuiDemoLayout.SLOT,()->{
                icon("SLOT_BACKGROUND",r.x()-1,r.y()-1,18,18);item(session.demoSlot(entry.getKey()),r.x(),r.y());
            });
        }
        return builder.build();
    }

    private boolean visible(Appearance a,GuiDemoState session,String id) {
        if(a.screen.equals("GuiPatternImportPrioritySettings")&&id.startsWith("priorityButton"))return Integer.parseInt(id.substring(14))<ae2.api.client.PatternImportPriorities.getRegistered().size();
        if(a.screen.equals("GuiPatternModifier")) {
            if(id.equals("mode"))return true;
            if(id.equals("replace"))return session.stepIndex()==2;
            if(id.equals("clear")||id.startsWith("amount_"))return session.stepIndex()!=2;
            return false;
        }
        if(!a.screen.equals("GuiTerminalSettings")||id.equals("back"))return true;
        Set<String> search=Set.of("useInternalSearchRadio","useExternalSearchRadio","rememberCheckbox","autoFocusCheckbox","syncWithExternalCheckbox","clearExternalCheckbox");
        Set<String> wireless=Set.of("pickBlockCheckbox","craftIfMissingCheckbox","restockCheckbox","magnetCheckbox","pickupToMECheckbox","magnetSettingsButton");
        int page=session.stepIndex()%3;
        return page==0?search.contains(id)&&!id.equals("clearExternalCheckbox"):page==2?wireless.contains(id):!search.contains(id)&&!wireless.contains(id);
    }

    private void background(Appearance a,GuiStyle style,GuiDemoState session) {
        if(a.screen.equals("GuiPatternModifier")) {
            blit(session.stepIndex()==2?"pattern_editor_3":"pattern_editor_1",0,0,0,0,176,212);
        }else if(style!=null&&style.getTerminalStyle()!=null) {
            var t=style.getTerminalStyle();int y=0;
            for(var part:List.of(t.getHeader(),t.getFirstRow(),t.getRow(),t.getLastRow(),t.getBottom())) {
                part.copy().dest(0,y).blit();y+=part.getSrcHeight();
            }
        }else if(style!=null&&style.getGeneratedBackground()!=null) {
            BackgroundGenerator.draw(a.width,a.height,0,0);
        }else if(style!=null&&style.getBackground()!=null) {
            style.getBackground().dest(0,0).blit();
        }else if(a.screen.equals("GuiAdvancedMemoryCard")) {
            style.getImage("backgroundTop").copy().dest(0,0).blit();
            for(int i=0;i<2;i++)style.getImage("backgroundRow").copy().dest(0,60+i*42).blit();
            style.getImage("backgroundBottom").copy().dest(0,144).blit();
        }else if(a.screen.equals("GuiRequester")||a.screen.equals("GuiRequesterTerm")) {
            String texture=a.screen.equals("GuiRequester")?"requester":"requester_terminal";
            blit(texture,0,0,0,0,195,20);
            for(int i=0;i<5;i++)blit(texture,0,20+i*19,0,38,195,19);
            blit(texture,0,115,0,a.screen.equals("GuiRequester")?114:133,195,101);
        }else if(a.screen.equals("GuiCellTerminal")) {
            blit("cell_terminal",0,0,0,0,208,19);
            for(int i=0;i<6;i++)blit("cell_terminal",0,19+i*18,0,52,208,18);
            blit("cell_terminal",0,127,0,158,208,98);
        }else if(a.screen.equals("GuiPatternAccessTerm")||a.screen.equals("GuiPEATerm")) {
            blit("ex_pattern_access_terminal",0,0,0,0,213,30);
            for(int i=0;i<4;i++) {
                int textRow=i==0?30:i==3?102:66;
                blit("ex_pattern_access_terminal",0,30+i*18,0,textRow,213,18);
                if(i%2==1)blit("ex_pattern_access_terminal",0,30+i*18,0,i==3?120:84,178,18);
            }
            if(a.screen.equals("GuiPEATerm"))blit("ex_pattern",0,102,0,73,213,178);
            else blit("ex_pattern_access_terminal",0,102,0,138,213,99);
        }else if(!a.texture.isEmpty()) {
            String path=a.texture.substring("ae2:textures/".length());
            Blitter.texture(path).src(0,0,a.width,a.height).dest(0,0).blit();
        }else BackgroundGenerator.draw(a.width,a.height,0,0);
    }

    private void toolbar(Appearance a) {
        int n=a.toolbar.size();if(n==0)return;
        var bg=Blitter.texture("guis/sprites/vertical_buttons_bg.png",21,26);
        int h=n*22+6;
        bg.copy().src(0,0,21,2).dest(-19,0,21,2).blit();
        bg.copy().src(0,2,21,20).dest(-19,2,21,h-6).blit();
        bg.copy().src(0,22,21,4).dest(-19,h-4,21,4).blit();
        for(int i=0;i<n;i++)iconButton(a.toolbar.get(i),-15,3+i*22,16,16);
    }

    private void upgrades(Appearance a) {
        var bg=Blitter.texture("guis/extra_panels.png",128,128);
        for(int i=0;i<a.upgrades;i++) {
            int sy=i==0?0:5,sh=18+(i==0?5:0)+(i==a.upgrades-1?7:0);
            bg.copy().src(0,sy,29,sh).dest(a.width+1,i*18+(i==0?0:5)).blit();
        }
    }

    private void drawWidget(Appearance a,GuiStyle style,GuiDemoState session,String id,Widget w) {
        int x=w.x,y=w.y,width=w.width,height=w.height;
        String value=session.demoValue("widget."+id);
        switch(w.kind) {
            case "canvas" -> { }
            case "number" -> {
                var demo=numbers.computeIfAbsent(session.tutorial().id()+"/"+id,k->{
                    var number=new NumberEntryWidget(style,NumberEntryType.UNITLESS);
                    number.setPosition(new Point(x,y));number.setSize(width,height);
                    if(id.equals("upperLevel")||id.equals("lowerLevel"))number.setShowIncrementButtons(false);
                    number.setTextFieldStyle(style.getWidget(id+"Input"));
                    var buttons=new ArrayList<net.minecraft.client.gui.GuiButton>();
                    // NumberEntryWidget only needs bounds to populate its passive child buttons.
                    number.populateScreen(buttons::add,new Rectangle(0,0,a.width,a.height),null);
                    return new NumberDemo(number,buttons);
                });
                try{demo.widget().setLongValue(value.isEmpty()?1:Long.parseLong(value));}catch(NumberFormatException ignored){}
                demo.widget().setFocused(false);demo.widget().updateBeforeRender();
                for(var b:demo.buttons())b.drawButton(mc,-10000,-10000,0);
                demo.widget().drawAbsoluteLayer(new Rectangle(0,0,a.width,a.height),new Point(-10000,-10000));
                GlStateManager.disableDepth();
            }
            case "field" -> {
                if(value.isEmpty()&&id.endsWith("Input"))value=session.demoValue("widget."+id.substring(0,id.length()-5));
                if(value.isEmpty()&&!id.toLowerCase(Locale.ROOT).contains("search"))value=id.equals("name")?"ME":id.equals("playerPinRowsField")?"1":"0";
                if(id.matches("(?:default|shift|ctrl|alt)[0-3]"))value=Integer.toString(new int[]{1,10,100,1000}[id.charAt(id.length()-1)-'0']);
                var field=fields.computeIfAbsent(session.tutorial().id()+"/"+id,k->new AETextField(style,mc.fontRenderer,x,y,width,height));
                field.setText(value);field.setFocused(false);field.drawTextBox();
            }
            case "label" -> text(value.isEmpty()?"1":value,x,y,width,0xff404040);
            case "checkbox" -> {
                var checkbox=new AECheckbox(x,y,width,height,style,new TextComponentString(label(w,id)));
                checkbox.setRadio(id.endsWith("Radio"));
                checkbox.setSelected(!id.equals("useExternalSearchRadio")&&!id.equals("pinDisplayLockedGridRadio"));
                if(id.equals("useExternalSearchRadio"))checkbox.enabled=ae2.integration.abstraction.ItemListMod.isEnabled();
                checkbox.drawButton(mc,-10000,-10000,0);
            }
            case "scrollbar" -> {
                Blitter.texture("guis/sprites/big_scroller.png",12,15).src(0,0,12,15).dest(x,y).blit();
            }
            case "progress" -> {
                if(style!=null) {
                    var image=style.getImage(id).copy();String p=session.demoValue("progress");
                    float fraction=p.isEmpty()?.45f:p.startsWith("100")?1:.5f;
                    int h=Math.max(1,(int)(image.getSrcHeight()*fraction));
                    image.srcHeight(h).dest(x,y+image.getSrcHeight()-h).blit();
                }
            }
            case "encoding" -> {
                Blitter.texture("guis/pattern_modes.png").src(0,session.tutorial().id().getPath().equals("pattern_processing")?66:0,124,66).dest(x,y).blit();
            }
            case "panel" -> style.getImage(id).copy().dest(x,y).blit();
            case "viewcells" -> {
                var bg=Blitter.texture("guis/view_cells_panel.png",24,30);
                bg.copy().src(0,0,24,6).dest(x,y).blit();
                for(int i=0;i<5;i++)bg.copy().src(0,6,24,18).dest(x,y+6+i*18).blit();
                bg.copy().src(0,24,24,6).dest(x,y+96).blit();
            }
            case "cpulist" -> {
                style.getImage("cpuList").copy().dest(x,y,width,height).blit();
                text(I18n.format("gui.ae2.CPUs"),x+7,y+6,width-25,0xff404040);
                for(int i=0;i<3;i++)text((i+1)+" · 16k",x+7,y+32+i*31,width-25,0xff404040);
            }
            case "color" -> Gui.drawRect(x,y,x+width,y+height,DEMO_COLORS[Integer.parseInt(id.substring(6))]);
            case "colorwindow" -> colorWindow(a,style,x,y);
            case "celltab" -> {
                int index=Integer.parseInt(id.substring(7));
                icon(index==0?"CELL_TERMINAL_TAB_SELECTED":"CELL_TERMINAL_TAB",x,y,22,22);
                String[] items={"cell_terminal","chest","cell_workbench","item_storage_cell_64k","storage_bus","storage_bus","interface","network_tool"};
                item(new GuiTutorial.Stack("ae2:"+items[index],1),x+3,y+3);
            }
            case "memory" -> {
                for(int i=0;i<3;i++) {
                    int rowY=y+i*42;
                    item(new GuiTutorial.Stack("ae2:me_p2p_tunnel",1),x+3,rowY+3);
                    icon("ADVANCED_MEMORY_CARD_STATUS_INPUT",x+3,rowY+21,12,12);
                    text("P2P "+(i+1),x+24,rowY+3,130,0xffe0e0e0);
                    text("ME · "+String.format("%04X",0x120+i),x+24,rowY+14,130,0xffa8a8a8);
                    text("64, 6, "+(64+i),x+24,rowY+26,130,0xffa8a8a8);
                    button(x+169,rowY+14,50,20,I18n.format("gui.ae2.advanced_memory_card.bind"));
                }
            }
            case "keytypes" -> {
                for(int i=0;i<2;i++){icon("SLOT_BACKGROUND",x,y+i*24,18,18);item(new GuiTutorial.Stack(i==0?"minecraft:iron_ingot":"minecraft:water_bucket",1),x+1,y+1+i*24);text(I18n.format(i==0?"gui.ae2.Items":"gui.ae2.Fluids"),x+25,y+5+i*24,100,0xff404040);}
            }
            default -> {
                String icon=ICONS_OVERRIDES.getOrDefault(id,w.icon);
                if(a.screen.equals("GuiPatternModifier")&&id.equals("mode"))icon="SCHEDULING_DEFAULT";
                if(icon!=null&&!icon.isEmpty()&&width<=24&&height<=24) {
                    if(Set.of("openPriority","back","craftingStatus","returnToParent","craftTree","numberEntryButtonConfig").contains(id)||id.startsWith("modeTabButton")) {
                        var b=new TabButton(resolveIcon(icon),new TextComponentString(""),null);b.x=x;b.y=y;b.width=width;b.height=height;
                        if(id.startsWith("modeTabButton"))b.setStyle(TabButton.Style.HORIZONTAL);
                        b.drawButton(mc,-10000,-10000,0);
                    }else iconButton(icon,x,y,width,height);
                }
                else button(x,y,width,height,value.isEmpty()?label(w,id):value);
            }
        }
    }

    private String label(Widget w,String id) {
        if(w.text!=null&&!w.text.isEmpty())return w.text;
        if(w.label!=null&&!w.label.isEmpty())try{return GuiText.valueOf(w.label).text(new TextComponentString("HEI")).getFormattedText();}catch(IllegalArgumentException ignored){}
        if(id.matches("amount_[0-7]")){int index=Integer.parseInt(id.substring(7));return (index<4?"×":"÷")+new int[]{2,3,5,8}[index%4];}
        if(id.startsWith("amount")||id.startsWith("processingAmount"))return "×2";
        if(id.endsWith("Mode"))return "+/−";
        if(id.startsWith("priorityButton"))return id.substring(14);
        if(id.startsWith("previous")||id.equals("mode_previous")||id.equals("size_decrease"))return "<";
        if(id.startsWith("next")||id.equals("mode_next")||id.equals("size_increase"))return ">";
        return "";
    }

    private void drawTextEntry(Appearance a,GuiStyle style,GuiDemoState session,String key,Text spec) {
        String value=displayText(a,spec,key,session);var p=spec.getPosition().resolve(new Rectangle(0,0,a.width,a.height));
        List<String> lines=spec.getMaxWidth()>0?mc.fontRenderer.listFormattedStringToWidth(value,spec.getMaxWidth()):List.of(value);
        float scale=spec.getScale();int y=p.y();
        for(String line:lines) {
            int width=mc.fontRenderer.getStringWidth(line),offset=spec.getAlign()==TextAlignment.RIGHT?width:spec.getAlign()==TextAlignment.CENTER?width/2:0;
            GlStateManager.pushMatrix();
            try{GlStateManager.translate(p.x(),y,0);GlStateManager.scale(scale,scale,1);mc.fontRenderer.drawString(line,-offset,0,style.getColor(spec.getColor()).toARGB());}
            finally{GlStateManager.popMatrix();}
            y+=Math.round(mc.fontRenderer.FONT_HEIGHT*scale);
        }
    }

    private String displayText(Appearance a,Text spec,String key,GuiDemoState session) {
        String s=spec.getText().getFormattedText();if(s.isEmpty())s=dynamicText(key,session);
        if(a.screen.equals("GuiTerminalSettings")&&key.equals("dialog_title"))s=(session.stepIndex()%3==0?GuiText.SearchSettingsTitle:session.stepIndex()%3==2?GuiText.WirelessTerminalSettingsTitle:GuiText.TerminalSettingsTitle).text().getFormattedText();
        var p=spec.getPosition().resolve(new Rectangle(0,0,a.width,a.height));
        if(spec.getMaxWidth()>0)return s;
        int max=spec.getAlign()==TextAlignment.RIGHT?p.x()-8:spec.getAlign()==TextAlignment.CENTER?2*Math.min(p.x()-8,a.width-p.x()-8):a.width-p.x()-8;
        if(key.equals("dialog_title")&&a.widgets.containsKey("search"))max=Math.max(16,a.widgets.get("search").x-p.x()-4);
        return mc.fontRenderer.trimStringToWidth(s,Math.max(1,(int)(max/spec.getScale())));
    }

    private String dynamicText(String key,GuiDemoState session) {
        String value=session.demoValue("text."+key);if(!value.isEmpty())return value;
        if(key.equals("dialog_title"))return GuiTutorialDrawing.text(session.tutorial().title()).split("[:：]",2)[0];
        if(key.equals("entriesShown"))return "8 / 8";
        return switch(key){
            case "stored_power" -> GuiText.StoredPower.text("8,000 AE").getFormattedText();
            case "max_power" -> GuiText.MaxPower.text("25,000 AE").getFormattedText();
            case "power_usage_rate","used_power" -> "8 AE/t";
            case "power_input_rate" -> "16 AE/t";
            case "channel_power_rate" -> "1 AE/t";
            case "required_power" -> GuiText.RequiredPower.text("4,096 AE").getFormattedText();
            case "efficiency" -> GuiText.Efficiency.text(0.8f).getFormattedText();
            case "scs_size" -> GuiText.SCSSize.text(3,3,3).getFormattedText();
            case "loaded_chunks" -> GuiText.SpatialAnchorLoadedChunks.text(4).getFormattedText();
            case "statistics_loaded" -> GuiText.SpatialAnchorAllLoaded.text(4,4).getFormattedText();
            case "statistics_total" -> GuiText.SpatialAnchorAll.text(4,4).getFormattedText();
            case "range" -> "16 m";
            case "energy_use" -> "8 AE/t";
            case "cpu_status" -> "16k · 0 B";
            case "page_info" -> "1 / 1";
            case "errorText" -> GuiText.CraftErrorMissingIngredient.text().getFormattedText();
            case "mode_value" -> GuiText.NetworkAnalyserModeFull.text().getFormattedText();
            case "node_size_value" -> "4";
            case "normal_nodes" -> GuiText.NetworkAnalyserStateNormalNodes.text(8).getFormattedText();
            case "dense_nodes" -> GuiText.NetworkAnalyserStateDenseNodes.text(2).getFormattedText();
            case "missing_nodes" -> GuiText.NetworkAnalyserStateMissingNodes.text(0).getFormattedText();
            case "channel_mode" -> GuiText.NetworkAnalyserChannelDefault.text().getFormattedText();
            case "recursive_reserve_label" -> GuiText.TerminalSettingsRecursiveIngredientReserve.text().getFormattedText();
            case "player_pin_rows_label" -> GuiText.TerminalSettingsPlayerPinRows.text().getFormattedText();
            default -> nativeDynamicText(key);
        };
    }

    private String nativeDynamicText(String key) {
        if(key.startsWith("color_label_")) {
            GuiText[] labels={GuiText.NetworkAnalyserLinkNormal,GuiText.NetworkAnalyserLinkDense,GuiText.NetworkAnalyserLinkCompressed,GuiText.NetworkAnalyserNodeNormal,GuiText.NetworkAnalyserNodeDense,GuiText.NetworkAnalyserNodeMissing};
            return labels[Integer.parseInt(key.substring(12))].text().getFormattedText();
        }
        return "0";
    }

    private void colorWindow(Appearance a,GuiStyle style,int x,int y) {
        Blitter.texture("guis/color_configer.png",200,200).src(0,0,110,95).dest(x,y).blit();
        String[] names={"red","green","blue","alpha"};int[] colors={0xffdc5050,0xff50d060,0xff5080dc,0xffc0c0c0};
        var bounds=new Rectangle(0,0,a.width,a.height);
        for(int i=0;i<4;i++) {
            var spec=style.getWidget("color_"+names[i]);var p=spec.resolve(bounds);
            Gui.drawRect(p.x(),p.y(),p.x()+spec.getWidth(),p.y()+spec.getHeight(),0xff202020);
            Gui.drawRect(p.x(),p.y(),p.x()+spec.getWidth()*3/4,p.y()+spec.getHeight(),colors[i]);
        }
        var preview=style.getWidget("color_preview");var p=preview.resolve(bounds);
        Gui.drawRect(p.x(),p.y(),p.x()+preview.getWidth(),p.y()+preview.getHeight(),DEMO_COLORS[0]);
        for(String id:List.of("color_apply","color_cancel")){var s=style.getWidget(id);var pos=s.resolve(bounds);iconButton(id.equals("color_apply")?"ENTER":"CLEAR",pos.x(),pos.y(),16,16);}
    }

    private void dynamicContent(Appearance a,GuiDemoState session) {
        String screen=a.screen;
        if(screen.equals("GuiCraftConfirm")||screen.equals("GuiCraftingCPU")||screen.equals("GuiCraftingStatus")||screen.equals("GuiNetworkStatus")) {
            int x=8,y=screen.equals("GuiNetworkStatus")?41:24;
            for(int i=0;i<6;i++) {
                int px=x+(i%3)*54,py=y+(i/3)*34;
                String[] machines={"ae2:controller","ae2:drive","ae2:terminal","ae2:energy_acceptor","ae2:fluix_glass_cable","ae2:storage_bus"};
                item(new GuiTutorial.Stack(screen.equals("GuiNetworkStatus")?machines[i]:SAMPLE_ITEMS[i],1),px,py);
                text(i%2==0?"64":"16",px+18,py+5,34,0xff404040);
            }
        }else if(screen.equals("GuiRequester")||screen.equals("GuiRequesterTerm")) {
            for(int i=0;i<5;i++) {
                int y=20+i*19;item(new GuiTutorial.Stack(SAMPLE_ITEMS[i],1),27,y+2);
                text("64",48,y+3,44,0xffe0e0e0);text("1",102,y+3,44,0xffe0e0e0);
                icon("ENABLED",9,y,16,16);icon("ENABLED",151,y,16,16);
            }
        }else if(screen.equals("GuiCellTerminal")) {
            text(GuiText.CellTerminal.getLocal(),8,6,83,0xff404040);
            for(int i=0;i<4;i++){item(new GuiTutorial.Stack("ae2:item_storage_cell_1k",1),8,20+i*18);text("1k · 128 / 1,024 B",29,25+i*18,150,0xffe0e0e0);}
        }else if(screen.equals("GuiCraftingTree")) {
            Gui.drawRect(127,58,129,122,0xff7a7a7a);Gui.drawRect(57,120,199,122,0xff7a7a7a);
            for(int i=0;i<3;i++){int x=48+i*70;Gui.drawRect(x+8,120,x+10,144,0xff7a7a7a);item(new GuiTutorial.Stack(SAMPLE_ITEMS[i],1),x,144);}
            item(new GuiTutorial.Stack("ae2:engineering_processor",1),120,43);
        }else if(screen.equals("GuiPatternModifier")) {
            text(GuiText.PatternModifier.getLocal((session.stepIndex()==2?GuiText.PatternModifierReplace:GuiText.PatternModifierMultiply).getLocal()),8,6,160,0xff404040);
        }else if(screen.equals("GuiCellRestriction")) {
            GuiText[] labels={GuiText.CellRestrictionMaxAmount,GuiText.CellRestrictionMaxType,GuiText.CellRestrictionMaxByte,GuiText.CellRestrictionAmountPerByte,GuiText.CellRestrictionTypePerByte,GuiText.CellRestrictionAllocatedByte,GuiText.CellRestrictionFreeByte};
            long[] values={8192,63,1024,8,8,128,896};
            for(int i=0;i<labels.length;i++)text(labels[i].getLocal(values[i]),12,62+i*10,152,0xff404040);
        }else if(screen.equals("GuiPatternImportPrioritySettings")) {
            var priorities=ae2.api.client.PatternImportPriorities.getRegistered();
            for(int i=0;i<Math.min(6,priorities.size());i++)text(priorities.get(i).getDisplayName().getFormattedText(),44,34+i*24,138,0xff404040);
        }else if(screen.equals("GuiCraftingPattern")) {
            text(I18n.format("gui.pattern_view.craft.substitute",ae2.core.localization.Tooltips.Off.getLocal()),8,6,160,0xff303030);
            text(I18n.format("gui.pattern_view.craft.fluid_substitute",ae2.core.localization.Tooltips.Off.getLocal()),8,19,160,0xff303030);
            for(int i=0;i<9;i++)item(new GuiTutorial.Stack("minecraft:iron_ingot",1),29+i%3*18,35+i/3*18);
            item(new GuiTutorial.Stack("minecraft:iron_block",1),121,53);
        }else if(screen.equals("GuiProcessingPattern")) {
            item(new GuiTutorial.Stack("minecraft:iron_ore",1),8,9);
            item(new GuiTutorial.Stack("minecraft:iron_ingot",1),8,189);
        }
    }

    private void cpuListContent(GuiDemoLayout.Group content) {
        var rows=content.group(8,31).clip(new GuiTutorial.Rect(0,0,203,132));
        rows.region("view.body",new GuiTutorial.Rect(0,0,203,132));
        for(int row=0;row<6;row++) {
            int y=row*22,index=row;
            rows.node("cpu.row."+row,new GuiTutorial.Rect(0,y,203,21),GuiDemoLayout.CONTENT,()->{
                Gui.drawRect(0,y,203,y+21,0x22000000);
                if(index<4) {
                    text("CPU "+(index+1),4,y+3,111,0xffffffff);
                    text("16384 bytes",4,y+12,111,0xffd8dce8);
                    icon("S_STORAGE",127,y+6,8,8);text("16k",139,y+7,29,0xffffffff);
                    icon("S_PROCESSOR",170,y+6,8,8);text("4",182,y+7,21,0xffffffff);
                }
            });
        }
    }

    private void patternAccessContent(GuiDemoLayout.Group content,Appearance a) {
        String title=(a.screen.equals("GuiPEATerm")?GuiText.PatternEncodingAccessTerminalShort:GuiText.PatternAccessTerminalShort).text().getFormattedText();
        content.node("access.title",new GuiTutorial.Rect(17,6,93,9),GuiDemoLayout.TEXT,()->text(title,17,6,93,0xff404040));
        // Native access lists alternate group headers and provider inventories. All rows,
        // their backgrounds and their highlight viewport use the same clipped group.
        var rows=content.group(17,30).clip(new GuiTutorial.Rect(0,0,174,72));
        rows.region("view.body",new GuiTutorial.Rect(0,0,174,72));
        for(int row=0;row<4;row++) {
            int y=row*18;
            if(row%2==0) {
                rows.node("access.group."+row,new GuiTutorial.Rect(2,y+1,171,16),GuiDemoLayout.CONTENT,()->{
                    item(new GuiTutorial.Stack("ae2:pattern_provider",1),2,y+1);
                    text(I18n.format("tile.ae2.pattern_provider.name"),20,y+6,151,0xff404040);
                });
            } else for(int col=0;col<9;col++) {
                int x=col*18;
                rows.node("access.pattern."+row+"."+col,new GuiTutorial.Rect(x,y+1,16,16),GuiDemoLayout.CONTENT,()->{
                    if(x<72)item(new GuiTutorial.Stack("ae2:crafting_pattern",1),x,y+1);
                });
            }
        }
    }

    private static final String[] SAMPLE_ITEMS={"minecraft:iron_ingot","minecraft:gold_ingot","minecraft:redstone","ae2:certus_quartz_crystal","minecraft:quartz","ae2:fluix_crystal","ae2:silicon","minecraft:diamond"};
    private static final Map<String,String> ICONS_OVERRIDES=Map.of("openPriority","PRIORITY","back","BACK");
    private static final int[] DEMO_COLORS={0xffa0a0a0,0xfff0c050,0xffa050c0,0xff50b070,0xff40b8c0,0xffd04848};
    private Icon resolveIcon(String name){return icons.computeIfAbsent(name,n->{try{return (Icon)Icon.class.getField(n).get(null);}catch(ReflectiveOperationException e){return Icon.COG;}});}
    private void icon(String name,int x,int y,int width,int height) {
        resolveIcon(name).getBlitter().copy().colorArgb(0xffffffff).dest(x,y,width,height).blit();
    }
    private void iconButton(String name,int x,int y,int width,int height) {
        var b=new SimpleIconButton(resolveIcon(name),new TextComponentString(""),null);b.x=x;b.y=y;b.width=width;b.height=height;
        if(width<=10){b.setHalfSize(true);b.setDisableBackground(true);}
        b.drawButton(mc,-10000,-10000,0);
    }
    private void button(int x,int y,int width,int height,String label) {
        String s=mc.fontRenderer.trimStringToWidth(label,Math.max(1,width-4));
        new AE2Button(x,y,width,height,new TextComponentString(s),null).drawButton(mc,Integer.MIN_VALUE/4,Integer.MIN_VALUE/4,0);
        GlStateManager.disableDepth();
    }
    private void text(String s,int x,int y,int width,int color){mc.fontRenderer.drawString(mc.fontRenderer.trimStringToWidth(s,Math.max(1,width)),x,y,color);}
    private void item(GuiTutorial.Stack stack,int x,int y) {
        if(stack.item().isEmpty()||stack.count()<=0)return;
        ResourceLocation key=new ResourceLocation(stack.item());
        if(!Item.REGISTRY.containsKey(key))throw new IllegalStateException("Missing AE2S GUI demonstration item: "+key);
        Item item=Item.REGISTRY.getObject(key);
        ItemStack rendered=new ItemStack(item,stack.count());
        GlStateManager.color(1,1,1,1);RenderHelper.enableGUIStandardItemLighting();GlStateManager.enableDepth();
        mc.getRenderItem().renderItemAndEffectIntoGUI(rendered,x,y);
        mc.getRenderItem().renderItemOverlayIntoGUI(mc.fontRenderer,rendered,x,y,null);
        RenderHelper.disableStandardItemLighting();GlStateManager.disableDepth();GlStateManager.color(1,1,1,1);
    }
    private void blit(String texture,int x,int y,int sx,int sy,int width,int height){Blitter.texture("guis/"+texture+".png").src(sx,sy,width,height).dest(x,y).blit();}
}
