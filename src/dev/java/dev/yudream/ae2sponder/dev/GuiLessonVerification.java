package dev.yudream.ae2sponder.dev;

import ae2.client.gui.AEBaseGui;
import ae2.client.gui.me.patternencode.GuiPatternEncodingTerm;
import ae2.container.GuiIds.GuiKey;
import ae2.container.SlotSemantics;
import ae2.container.implementations.ContainerInscriber;
import ae2.core.gui.GuiOpener;
import ae2.parts.encoding.EncodingMode;
import ae2.parts.encoding.PatternEncodingTerminalPart;
import ae2.tile.networking.TileCableBus;
import dev.yudream.ae2sponder.compat.PonderAE2SPlugin;
import java.util.concurrent.CompletableFuture;
import net.createmod.ponder.api.gui.GuiTutorial;
import net.createmod.ponder.client.guitutorial.*;
import net.createmod.ponder.foundation.structure.PonderStructureLoader;
import net.createmod.ponder.gui.GuiTutorialSession;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiTextField;
import net.minecraft.inventory.ClickType;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.util.EnumFacing;
import net.minecraft.util.math.BlockPos;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;

/** Production-jar acceptance against native AE2S containers, widgets, search focus and shared scenes. */
final class GuiLessonVerification {
    private record Fixture(String id, String structure, GuiKey gui, BlockPos pos, boolean part) {}
    private static final Fixture[] FIXTURES = {
        new Fixture("drive", "first_network", GuiKey.DRIVE, new BlockPos(5,1,3), false),
        new Fixture("terminal", "first_network", GuiKey.ME_STORAGE_TERMINAL, new BlockPos(3,1,3), true),
        new Fixture("cell_workbench", "storage_cells", GuiKey.CELL_WORKBENCH, new BlockPos(4,1,1), false),
        new Fixture("inscriber", "processors", GuiKey.INSCRIBER, new BlockPos(2,1,2), false),
        new Fixture("pattern_crafting", "autocrafting", GuiKey.PATTERN_ENCODING_TERMINAL, new BlockPos(2,1,3), true),
        new Fixture("pattern_processing", "autocrafting", GuiKey.PATTERN_ENCODING_TERMINAL, new BlockPos(2,1,3), true),
        new Fixture("pattern_provider", "autocrafting", GuiKey.PATTERN_PROVIDER, new BlockPos(4,1,3), false),
        new Fixture("interface", "interfaces", GuiKey.INTERFACE, new BlockPos(5,1,3), false)
    };
    private final Minecraft mc = Minecraft.getMinecraft();
    private final BlockPos origin = new BlockPos(32,5,32);
    private CompletableFuture<Void> pending;
    private int index, phase, wait, language;
    private AEBaseGui<?> gui;
    private GuiTutorial tutorial;
    private String before;
    private int window;

    boolean tick(ClientVerification host) throws Exception {
        if (pending != null) {
            if (!pending.isDone()) return false;
            pending.join(); pending = null;
        }
        if (wait-- > 0) return false;
        if (index == FIXTURES.length) {
            GuiTutorialEvents.stop(); mc.player.closeScreen();
            Display.setDisplayMode(new DisplayMode(1280,720)); mc.resize(1280,720);
            return true;
        }
        Fixture f = FIXTURES[index];
        switch (phase) {
            case 0 -> {
                GuiTutorialEvents.stop(); mc.player.closeScreen();
                String code = language == 0 ? "en_us" : "zh_cn";
                if (!code.equals(mc.getLanguageManager().getCurrentLanguage().getLanguageCode())) {
                    mc.gameSettings.language = code;
                    mc.getLanguageManager().setCurrentLanguage(mc.getLanguageManager().getLanguage(code)); mc.refreshResources();
                }
                tutorial = GuiTutorials.resolve("ae2s_ponder:" + f.id);
                host.check(GuiTutorials.all().stream().filter(t -> t.id().getNamespace().equals("ae2s_ponder")).count() == 8,
                    "Eight shared AE2S GUI lessons register without optional external GUI mods");
                host.check(!GuiTutorialDrawing.text(tutorial.title()).startsWith("ae2s_ponder."), f.id + ": localized GUI title resolves");
                for (var step : tutorial.steps()) host.check(!GuiTutorialDrawing.text(step.text()).startsWith("ae2s_ponder."), f.id + ": localized step resolves");
                for (var target : tutorial.targets().values()) if (!target.item().isEmpty())
                    host.check(Item.REGISTRY.containsKey(new net.minecraft.util.ResourceLocation(target.item())), f.id + ": authored demo item exists");
                for (var step : tutorial.steps()) for (var action : step.demo()) if (!action.item().isEmpty())
                    host.check(Item.REGISTRY.containsKey(new net.minecraft.util.ResourceLocation(action.item())), f.id + ": demo action item exists: " + action.item());
                var structure = new PonderStructureLoader().load(PonderAE2SPlugin.id(f.structure));
                server(() -> {
                    P2PNetworkVerification.place(mc, origin, structure);
                    var player = mc.getIntegratedServer().getPlayerList().getPlayers().get(0);
                    player.inventory.clear(); player.inventory.setItemStack(ItemStack.EMPTY);
                    String item = switch (f.id) {
                        case "drive", "cell_workbench" -> "item_storage_cell_1k";
                        case "inscriber" -> "silicon_press";
                        default -> "blank_pattern";
                    };
                    player.inventory.setInventorySlotContents(0, new ItemStack(Item.REGISTRY.getObject(PonderAE2SPlugin.ae2(item))));
                    player.capabilities.isFlying = true; player.sendPlayerAbilities();
                    var pos = origin.add(f.pos);
                    player.connection.setPlayerLocation(pos.getX()+.5, pos.getY()+1, pos.getZ()+2,180,0);
                });
                phase++; wait = 60;
            }
            case 1 -> {
                server(() -> {
                    var player = mc.getIntegratedServer().getPlayerList().getPlayers().get(0);
                    var tile = mc.getIntegratedServer().getWorld(0).getTileEntity(origin.add(f.pos));
                    if (f.part) {
                        var part = ((TileCableBus)tile).getPart(EnumFacing.SOUTH);
                        if (part instanceof PatternEncodingTerminalPart pattern)
                            pattern.getLogic().setMode(f.id.equals("pattern_processing") ? EncodingMode.PROCESSING : EncodingMode.CRAFTING);
                        GuiOpener.openPartGui(player, f.gui, (TileCableBus)tile, EnumFacing.SOUTH);
                    } else GuiOpener.openGui(player, f.gui, tile);
                }); phase++; wait = 15;
            }
            case 2 -> {
                if (!(mc.currentScreen instanceof AEBaseGui<?> current)) return false;
                gui = current; var adapter = GuiTutorials.adapter(tutorial);
                host.check(adapter.matches(gui,tutorial), f.id + ": real native GUI matches its lesson");
                window = mc.player.openContainer.windowId;
                host.check(window>0, f.id + ": server opened a real synchronized container");
                var outer=adapter.window(gui,tutorial);
                host.check(gui.getExclusionZones().stream().allMatch(r -> outer.x()<=r.x && outer.y()<=r.y
                    && outer.x()+outer.width()>=r.x+r.width && outer.y()+outer.height()>=r.y+r.height),
                    f.id+": guide placement reserves actual AE2S toolbar and side-panel bounds");
                for (var step : tutorial.steps()) {
                    if (f.id.equals("cell_workbench") && step.target().startsWith("slot.CONFIG.")) {
                        host.check(adapter.target(gui,tutorial,step.target()) == null,
                            "Workbench config targets stay unavailable until a real cell is inserted");
                    } else host.check(adapter.target(gui,tutorial,step.target()) != null,
                        f.id + ": actual visible target resolves: " + step.target());
                }
                if (f.id.startsWith("pattern_")) host.check(GuiTutorials.forScreen(gui).stream().allMatch(t -> t.id().getPath().equals(f.id)),
                    f.id + ": current encoding mode selects the matching guide");
                if (gui instanceof ae2.client.gui.me.common.GuiMEStorage<?>) {
                    GuiTextField search = gui.getWidgets().getTextField("search");
                    search.setFocused(true); hold(false); for (int i=0;i<18;i++) hold(true);
                    host.check(GuiTutorialEvents.liveSession()==null && adapter.textFocused(gui), f.id + ": focused search keeps W for native text entry");
                    search.setFocused(false);
                }
                hold(false); for(int i=0;i<18;i++) hold(true);
                host.check(GuiTutorialEvents.liveSession()!=null && mc.currentScreen==gui && mc.player.openContainer.windowId==window,
                    f.id + ": W starts guidance within the same native screen and container");
                before = fingerprint();
                GuiTutorialEvents.preview(tutorial);
                var field = GuiTutorialEvents.class.getDeclaredField("demo"); field.setAccessible(true);
                var demo = (GuiDemoScreen)field.get(null); demo.session().playing(false);
                demo.session().seekAbsolute(demo.session().lastTick());
                host.check(before.equals(fingerprint()), f.id + ": demonstration leaves native inventories and carried items unchanged");
                host.screenshot("gui-"+f.id+"-demo-"+language+".png"); phase++;
            }
            case 3 -> {
                var field=GuiTutorialEvents.class.getDeclaredField("demo");field.setAccessible(true);
                ((GuiDemoScreen)field.get(null)).key('\0',org.lwjgl.input.Keyboard.KEY_ESCAPE);
                host.check(before.equals(fingerprint()) && mc.currentScreen==gui && mc.player.openContainer.windowId==window,
                    f.id+": embedded demo closes back into the original native container");
                host.screenshot("gui-"+f.id+"-live-"+language+".png");
                if (f.id.equals("drive") || f.id.equals("cell_workbench")) {
                    int hotbar=gui.getContainer().inventorySlots.stream().filter(s -> s.inventory==mc.player.inventory&&s.getSlotIndex()==0).findFirst().orElseThrow().slotNumber;
                    int cell=gui.getContainer().getSlots(SlotSemantics.STORAGE_CELL).get(0).slotNumber;
                    mc.playerController.windowClick(window,hotbar,0,ClickType.PICKUP,mc.player);
                    mc.playerController.windowClick(window,cell,0,ClickType.PICKUP,mc.player);
                    wait=15;
                }
                phase++;
            }
            case 4 -> {
                if (f.id.equals("cell_workbench")) {
                    host.check(GuiTutorialEvents.liveSession().stepIndex()==1,"Workbench guide observes real storage-cell insertion");
                    host.check(GuiTutorials.adapter(tutorial).target(gui,tutorial,"slot.CONFIG.0")!=null,
                        "Workbench config highlight becomes available with the native cell slots");
                }
                if (f.id.equals("drive")) {
                    host.check(GuiTutorialEvents.liveSession().stepIndex()==1, "Drive guide advances only after actual storage-cell insertion synchronizes");
                    var slot=gui.getContainer().getSlots(SlotSemantics.STORAGE_CELL).get(0);
                    var rect=GuiTutorials.adapter(tutorial).target(gui,tutorial,"slot.STORAGE_CELL.0");
                    host.check(rect.x()==gui.getGuiLeft()+slot.xPos&&rect.y()==gui.getGuiTop()+slot.yPos,"AE2S semantic target uses native slot geometry");
                    Display.setDisplayMode(new DisplayMode(854,480));mc.resize(854,480);
                    rect=GuiTutorials.adapter(tutorial).target(gui,tutorial,"slot.STORAGE_CELL.0");
                    host.check(rect.x()==gui.getGuiLeft()+slot.xPos&&rect.y()==gui.getGuiTop()+slot.yPos,"AE2S highlights follow native GUI resizing");
                    host.screenshot("gui-drive-small-"+language+".png");
                }
                if (gui.getContainer() instanceof ContainerInscriber inscriber) {
                    inscriber.processingTime=37;
                    host.check(GuiTutorials.adapter(tutorial).value(gui,"inscriber.progress").equals("37"),"Inscriber reads AE2S GuiSync progress rather than vanilla inventory fields");
                    host.check(GuiTutorials.adapter(tutorial).value(gui,"inscriber.work_observed").equals("1"),"Live processing condition observes synchronized work");
                    inscriber.processingTime=0;
                    var output=inscriber.getSlots(SlotSemantics.MACHINE_OUTPUT).get(0);
                    var original=output.getStack().copy();
                    output.putStack(new ItemStack(Item.REGISTRY.getObject(PonderAE2SPlugin.ae2("printed_silicon"))));
                    host.check(GuiTutorials.adapter(tutorial).value(gui,"inscriber.work_observed").equals("1"),"Already completed fast recipes satisfy the live processing condition");
                    output.putStack(original);
                }
                var demo = new GuiTutorialSession(tutorial);demo.seekAbsolute(demo.lastTick());String end=demo.demoSlot(tutorial.steps().get(tutorial.steps().size()-1).target()).toString();
                demo.seekAbsolute(0);demo.seekAbsolute(demo.lastTick());
                host.check(end.equals(demo.demoSlot(tutorial.steps().get(tutorial.steps().size()-1).target()).toString()),f.id+": demo seeking and replay reconstruct the same final state");
                phase++;
            }
            default -> {
                GuiTutorialEvents.stop(); mc.player.closeScreen();
                Display.setDisplayMode(new DisplayMode(1280,720));mc.resize(1280,720);
                phase=0; if(language++==1){language=0;index++;}
            }
        }
        return false;
    }

    private static void hold(boolean held) throws Exception {
        var tick=GuiTutorialEvents.class.getDeclaredMethod("tick",boolean.class);tick.setAccessible(true);tick.invoke(null,held);
    }
    private String fingerprint(){var result=new StringBuilder();for(var slot:mc.player.openContainer.inventorySlots)result.append(slot.getStack().serializeNBT());return result.append(mc.player.inventory.getItemStack().serializeNBT()).toString();}
    private void server(Runnable action){pending=new CompletableFuture<>();mc.getIntegratedServer().addScheduledTask(()->{try{action.run();pending.complete(null);}catch(Throwable e){pending.completeExceptionally(e);}});}
}
