package dev.yudream.ae2sponder.dev;

import ae2.api.parts.IPartItem;
import ae2.client.gui.AEBaseGui;
import ae2.client.gui.widgets.NumberEntryWidget;
import ae2.container.GuiIds.GuiKey;
import ae2.core.gui.GuiOpener;
import ae2.core.network.InitNetwork;
import ae2.core.network.serverbound.SwitchGuisPacket;
import ae2.tile.networking.TileCableBus;
import dev.yudream.ae2sponder.compat.AE2SGuiCatalog;
import dev.yudream.ae2sponder.compat.PonderAE2SPlugin;
import java.util.concurrent.CompletableFuture;
import net.createmod.ponder.api.gui.GuiTutorial;
import net.createmod.ponder.client.guitutorial.*;
import net.createmod.ponder.foundation.structure.PonderStructureLoader;
import net.minecraft.block.Block;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiTextField;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.util.EnumFacing;
import net.minecraft.util.math.BlockPos;

/** Real FML item/tile/part GUI openers, not manufactured screen or container mocks. */
final class ExtendedGuiLiveVerification {
    private record Fixture(String id,String component,GuiKey key,String kind,String sub) {}
    private static Fixture block(String id,String component,GuiKey key){return new Fixture(id,component,key,"block","");}
    private static Fixture part(String id,String component,GuiKey key){return new Fixture(id,component,key,"part","");}
    private static Fixture item(String id,String component,GuiKey key){return new Fixture(id,component,key,"item","");}
    private static final Fixture[] FIXTURES={
        block("me_chest","chest",GuiKey.ME_CHEST),block("sky_chest","sky_stone_chest",GuiKey.SKY_CHEST),
        block("io_port","io_port",GuiKey.IO_PORT),block("condenser","condenser",GuiKey.CONDENSER),
        block("vibration_chamber","vibration_chamber",GuiKey.VIBRATION_CHAMBER),
        block("crystal_assembler","crystal_assembler",GuiKey.CRYSTAL_ASSEMBLER),
        block("ingredient_buffer","ingredient_buffer",GuiKey.INGREDIENT_BUFFER),block("caner","caner",GuiKey.CANER),
        block("molecular_assembler","molecular_assembler",GuiKey.MOLECULAR_ASSEMBLER),
        block("wireless_access_point","wireless_access_point",GuiKey.WIRELESS_ACCESS_POINT),
        block("quantum_bridge","quantum_link",GuiKey.QNB),block("spatial_io","spatial_io_port",GuiKey.SPATIAL_IO_PORT),
        block("spatial_anchor","spatial_anchor",GuiKey.SPATIAL_ANCHOR),block("requester","requester",GuiKey.REQUESTER),
        part("import_bus","import_bus",GuiKey.IMPORT_BUS),part("export_bus","export_bus",GuiKey.EXPORT_BUS),
        part("storage_bus","storage_bus",GuiKey.STORAGE_BUS),part("precise_export_bus","precise_export_bus",GuiKey.PRECISE_EXPORT_BUS),
        part("threshold_export_bus","threshold_export_bus",GuiKey.THRESHOLD_EXPORT_BUS),
        part("stock_export_bus","stock_export_bus",GuiKey.STOCK_EXPORT_BUS),part("import_export_bus","import_export_bus",GuiKey.IMPORT_EXPORT_BUS),
        part("advanced_io_bus","advanced_io_bus",GuiKey.ADVANCED_IO_BUS),part("precise_storage_bus","precise_storage_bus",GuiKey.PRECISE_STORAGE_BUS),
        part("od_export_bus","od_export_bus",GuiKey.OD_EXPORT_BUS),part("od_storage_bus","od_storage_bus",GuiKey.OD_STORAGE_BUS),
        part("mod_export_bus","mod_export_bus",GuiKey.MOD_EXPORT_BUS),part("mod_storage_bus","mod_storage_bus",GuiKey.MOD_STORAGE_BUS),
        part("level_emitter","level_emitter",GuiKey.STORAGE_LEVEL_EMITTER),part("energy_emitter","energy_level_emitter",GuiKey.ENERGY_LEVEL_EMITTER),
        part("threshold_emitter","threshold_level_emitter",GuiKey.THRESHOLD_LEVEL_EMITTER),
        part("formation_plane","formation_plane",GuiKey.FORMATION_PLANE),part("annihilation_plane","annihilation_plane",GuiKey.ANNIHILATION_PLANE),
        part("pattern_access","pattern_access_terminal",GuiKey.PATTERN_ACCESS_TERMINAL),
        part("pea_terminal","pattern_encoding_access_terminal",GuiKey.PEA_TERMINAL),part("cell_terminal","cell_terminal",GuiKey.CELL_TERMINAL),
        part("requester_terminal","requester_terminal",GuiKey.REQUESTER_TERMINAL),part("crafting_terminal","crafting_terminal",GuiKey.CRAFTING_TERMINAL),
        item("network_tool","network_tool",GuiKey.NETWORK_TOOL),item("network_analyser","network_analyser",GuiKey.NETWORK_ANALYSER),
        item("tick_analyser","tick_analyser",GuiKey.TICK_ANALYSER),item("priority_tuner","priority_tuner",GuiKey.PRIORITY_TUNER),
        item("config_modifier","config_modifier",GuiKey.CONFIG_MODIFIER),item("pattern_modifier","pattern_modifier",GuiKey.PATTERN_MODIFIER),
        item("advanced_memory_card","advanced_memory_card",GuiKey.ADVANCED_MEMORY_CARD),
        item("portable_void_cell","portable_void_cell",GuiKey.PORTABLE_VOID_CELL),
        item("portable_item_cell","portable_item_cell_1k",GuiKey.PORTABLE_ITEM_CELL),
        item("portable_fluid_cell","portable_fluid_cell_1k",GuiKey.PORTABLE_FLUID_CELL),
        item("portable_workbench","portable_cell_workbench",GuiKey.PORTABLE_CELL_WORKBENCH),
        item("void_cell","void_storage_cell",GuiKey.VOID_CELL),item("quartz_knife","certus_quartz_cutting_knife",GuiKey.QUARTZ_KNIFE),
        block("network_status","controller",GuiKey.CONTROLLER_STATUS),
        new Fixture("priority","drive",GuiKey.DRIVE,"block","PRIORITY"),
        new Fixture("output_sides","inscriber",GuiKey.INSCRIBER,"block","OUTPUT_SIDES")
    };
    private final Minecraft mc=Minecraft.getMinecraft();
    private final BlockPos origin=new BlockPos(64,5,64),target=origin.add(5,1,3);
    private final AE2SGuiCatalog catalog=new AE2SGuiCatalog();
    private CompletableFuture<Void> pending;
    private int index=Integer.getInteger("ae2sponder.fixtureStart",0),phase,wait,attempts;
    private GuiTutorial tutorial;
    private AEBaseGui<?> gui;
    private String inventory;

    boolean tick(ClientVerification host)throws Exception {
        if(pending!=null){if(!pending.isDone())return false;pending.join();pending=null;}
        if(wait-->0)return false;
        if(index==FIXTURES.length){GuiTutorialEvents.stop();mc.player.closeScreen();return true;}
        var f=FIXTURES[index];
        if(phase==0) {
            GuiTutorialEvents.stop();mc.player.closeScreen();
            tutorial=GuiTutorials.resolve("ae2s_ponder:"+f.id);
            var structure=new PonderStructureLoader().load(PonderAE2SPlugin.id("first_network"));
            server(()->{
                P2PNetworkVerification.place(mc,origin,structure);
                var world=mc.getIntegratedServer().getWorld(0);var player=mc.getIntegratedServer().getPlayerList().getPlayers().get(0);
                player.inventory.clear();player.inventory.setItemStack(ItemStack.EMPTY);
                var item=Item.REGISTRY.getObject(PonderAE2SPlugin.ae2(f.component));
                if(f.kind.equals("item")){player.inventory.currentItem=0;player.inventory.setInventorySlotContents(0,new ItemStack(item));}
                else {
                    world.setBlockToAir(target);
                    if(f.kind.equals("part")) {
                        world.setBlockState(target,Block.REGISTRY.getObject(PonderAE2SPlugin.ae2("cable_bus")).getDefaultState(),3);
                        var bus=(TileCableBus)world.getTileEntity(target);
                        bus.addPart((IPartItem<?>)Item.REGISTRY.getObject(PonderAE2SPlugin.ae2("fluix_glass_cable")),null,player);
                        bus.addPart((IPartItem<?>)item,EnumFacing.SOUTH,player);
                    } else {
                        world.setBlockState(target,Block.REGISTRY.getObject(PonderAE2SPlugin.ae2(f.component)).getDefaultState(),3);
                        if(f.id.equals("output_sides"))((ae2.tile.misc.TileInscriber)world.getTileEntity(target)).getConfigManager()
                            .putSetting(ae2.api.config.Settings.AUTO_EXPORT,ae2.api.config.YesNo.YES);
                    }
                }
                player.capabilities.isFlying=true;player.sendPlayerAbilities();
                player.connection.setPlayerLocation(target.getX()+.5,target.getY()+1,target.getZ()+2,180,0);
            });phase++;wait=25;
        } else if(phase==1) {
            server(()->{
                var player=mc.getIntegratedServer().getPlayerList().getPlayers().get(0);
                var tile=mc.getIntegratedServer().getWorld(0).getTileEntity(target);
                if(f.kind.equals("item")) {
                    var hit=new net.minecraft.util.math.RayTraceResult(new net.minecraft.util.math.Vec3d(target).add(.5,.5,1),EnumFacing.SOUTH,target);
                    var locator=f.key==GuiKey.ADVANCED_MEMORY_CARD?ae2.core.gui.locator.GuiHostLocators.forInventorySlot(0,hit):ae2.core.gui.locator.GuiHostLocators.forInventorySlot(0);
                    GuiOpener.openItemGui(player,f.key,locator);
                }
                else if(f.kind.equals("part"))GuiOpener.openPartGui(player,f.key,(TileCableBus)tile,EnumFacing.SOUTH);
                else GuiOpener.openGui(player,f.key,tile);
            });phase++;wait=10;attempts=0;
        } else if(phase==2) {
            if(!(mc.currentScreen instanceof AEBaseGui<?> current)) {
                if(++attempts>80)throw new IllegalStateException(f.id+": native opener failed, current screen="+mc.currentScreen);
                return false;
            }
            if(!f.sub.isEmpty()&&!current.getClass().getName().equals(tutorial.screen())) {
                InitNetwork.sendToServer(SwitchGuisPacket.openSubGui(GuiKey.valueOf(f.sub)));wait=10;
                if(++attempts>5)throw new IllegalStateException(f.id+": subdialog failed");return false;
            }
            gui=current;var adapter=GuiTutorials.adapter(tutorial);
            host.check(adapter.matches(gui,tutorial),f.id+": native item/tile/part opener selects its authored guide: "+gui.getClass().getSimpleName());
            host.check(GuiTutorials.forScreen(gui).stream().allMatch(t->t.id().equals(tutorial.id())),f.id+": shared GUI class does not select another device's guide");
            var entry=catalog.get(f.id);
            for(String name:entry.widgets())if(gui.getWidgets().getComposite(name) instanceof NumberEntryWidget number)number.setFocused(false);
            gui.getWidgets().getTextFields().forEach(t->t.setFocused(false));
            GuiTextField field=gui.getWidgets().getTextFields().stream().filter(GuiTextField::getVisible).findFirst().orElse(null);
            if(field!=null){field.setFocused(true);hold(false);for(int i=0;i<18;i++)hold(true);host.check(GuiTutorialEvents.liveSession()==null,f.id+": native text input retains W");field.setFocused(false);}
            for(String name:entry.widgets())if(gui.getWidgets().getComposite(name) instanceof NumberEntryWidget number) {
                number.setFocused(true);hold(false);for(int i=0;i<18;i++)hold(true);
                host.check(GuiTutorialEvents.liveSession()==null,f.id+": composite numeric input retains W");number.setFocused(false);
            }
            hold(false);for(int i=0;i<18;i++)hold(true);
            host.check(GuiTutorialEvents.liveSession()!=null&&mc.currentScreen==gui,f.id+": W starts on the actual native screen");
            int resolved=0;
            for(var step:tutorial.steps())if(adapter.target(gui,tutorial,step.target())!=null)resolved++;
            host.check(resolved>0,f.id+": real current controls produce visible guidance targets");
            inventory=fingerprint();
            NativeGuiGeometryVerification.verify(host,f.id,gui,tutorial);
            host.screenshot("native-controls-"+f.id+".png");phase++;
        } else if(phase==3) {
            GuiTutorialEvents.preview(tutorial);
            var demoField=GuiTutorialEvents.class.getDeclaredField("demo");demoField.setAccessible(true);
            var demo=(GuiDemoScreen)demoField.get(null);demo.session().playing(false);demo.session().seekAbsolute(Math.min(180,demo.session().lastTick()));
            host.screenshot("native-expanded-"+f.id+".png");phase++;
        } else {
            var demoField=GuiTutorialEvents.class.getDeclaredField("demo");demoField.setAccessible(true);
            ((GuiDemoScreen)demoField.get(null)).key('\0',org.lwjgl.input.Keyboard.KEY_ESCAPE);
            host.check(inventory.equals(fingerprint())&&mc.currentScreen==gui,f.id+": demo return preserves native inventory and original screen");
            GuiTutorialEvents.stop();mc.player.closeScreen();index++;phase=0;
        }
        return false;
    }
    private static void hold(boolean held)throws Exception{var method=GuiTutorialEvents.class.getDeclaredMethod("tick",boolean.class);method.setAccessible(true);method.invoke(null,held);}
    private String fingerprint(){var result=new StringBuilder();for(var slot:mc.player.openContainer.inventorySlots)result.append(slot.getStack().serializeNBT());return result.append(mc.player.inventory.getItemStack().serializeNBT()).toString();}
    private void server(Runnable action){pending=new CompletableFuture<>();mc.getIntegratedServer().addScheduledTask(()->{try{action.run();pending.complete(null);}catch(Throwable e){pending.completeExceptionally(e);}});}
}
