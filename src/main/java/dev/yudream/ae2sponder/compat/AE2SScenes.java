package dev.yudream.ae2sponder.compat;

import net.createmod.catnip.math.Pointing;
import net.createmod.ponder.api.PonderPalette;
import net.createmod.ponder.api.scene.SceneBuilder;
import net.createmod.ponder.api.scene.SceneBuildingUtil;
import net.minecraft.init.Items;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.tileentity.TileEntity;
import net.minecraft.util.EnumFacing;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.math.Vec3d;

/** Scripted explanations in a virtual world; production recipes still run in the player's ME network. */
public final class AE2SScenes {
    private AE2SScenes() {}

    private static void begin(SceneBuilder scene, String id, String title, int size) {
        scene.title(id, title);
        scene.configureBasePlate(0, 0, size);
        scene.scaleSceneView(1.12f);
        scene.setSceneOffsetY(.15f);
        scene.showBasePlate();
        scene.idle(15);
    }

    private static void show(SceneBuilder scene, SceneBuildingUtil util, int x, int y, int z) {
        scene.world().showSection(util.select().position(x, y, z), EnumFacing.DOWN);
    }

    private static void explain(SceneBuilder scene, SceneBuildingUtil util, String key, int x, int y, int z) {
        scene.overlay().showText(160).sharedText(key).independent(45).attachKeyFrame();
        scene.overlay().showOutline(PonderPalette.WHITE, "narration", util.select().position(x, y, z), 160);
        scene.idle(170);
    }

    private static void use(SceneBuilder scene, SceneBuildingUtil util, String item, int x, int y, int z) {
        scene.overlay().showControls(util.vector().topOf(x, y, z), Pointing.DOWN, 75)
            .rightClick().withItem(stack(item));
    }

    private static void gui(SceneBuilder scene, String tutorial, int x, int y, int z) {
        scene.overlay().showGui(400, PonderAE2SPlugin.id(tutorial)).onRight()
            .pointAt(new Vec3d(x + .5, y + .5, z + .5));
        scene.idle(401);
    }

    private static ItemStack stack(String item) {
        return new ItemStack(Item.REGISTRY.getObject(PonderAE2SPlugin.ae2(item)));
    }

    private static void highlight(SceneBuilder scene, SceneBuildingUtil util, PonderPalette color,
                                  int x1, int y1, int z1, int x2, int y2, int z2) {
        scene.overlay().showOutline(color, new BlockPos(x1, y1, z1),
            util.select().fromTo(x1, y1, z1, x2, y2, z2), 100);
    }

    /** Reversible scripted item motion; no ticking machine or recipe assumptions in Ponder's virtual level. */
    private static void flow(SceneBuilder scene, SceneBuildingUtil util, ItemStack item,
                             int x1, int z1, int x2, int z2) {
        Vec3d start = util.vector().topOf(x1, 1, z1).add(0, .3, 0);
        Vec3d end = util.vector().topOf(x2, 1, z2).add(0, .3, 0);
        var entity = scene.world().createItemEntity(start, Vec3d.ZERO, item);
        scene.world().modifyEntity(entity, e -> e.setNoGravity(true));
        scene.overlay().showBigLine(PonderPalette.OUTPUT, start, end, 32);
        for (int tick = 0; tick < 24; tick++) {
            Vec3d point = start.add(end.subtract(start).scale((tick + 1) / 24.0));
            scene.world().modifyEntity(entity, e -> e.setPosition(point.x, point.y, point.z));
            scene.idle(1);
        }
        scene.world().modifyEntity(entity, e -> e.setDead());
        scene.idle(8);
    }

    public static void firstNetwork(SceneBuilder scene, SceneBuildingUtil util) {
        begin(scene, "first_network", "Your First ME Network", 7);
        show(scene, util, 1, 1, 2);
        show(scene, util, 1, 1, 3);
        scene.overlay().showControls(util.vector().topOf(1, 1, 2), Pointing.DOWN, 75)
            .rightClick().withItem(new ItemStack(Items.COAL));
        explain(scene, util, "first.power", 1, 1, 2);
        gui(scene, "vibration_chamber", 1, 1, 2);
        show(scene, util, 1, 1, 4);
        explain(scene, util, "first.acceptor", 1, 1, 4);
        scene.world().showSection(util.select().fromTo(2, 1, 3, 5, 1, 3), EnumFacing.DOWN);
        use(scene, util, "item_storage_cell_1k", 5, 1, 3);
        explain(scene, util, "first.storage", 5, 1, 3);
        gui(scene, "drive", 5, 1, 3);
        highlight(scene, util, PonderPalette.GREEN, 3, 1, 3, 3, 1, 3);
        use(scene, util, "terminal", 3, 1, 3);
        flow(scene, util, new ItemStack(Items.IRON_INGOT), 3, 3, 5, 3);
        explain(scene, util, "first.terminal", 3, 1, 3);
        gui(scene, "terminal", 3, 1, 3);
        explain(scene, util, "first.check", 2, 1, 3);
        scene.markAsFinished();
    }

    public static void storageCells(SceneBuilder scene, SceneBuildingUtil util) {
        begin(scene, "storage_cells", "Storage Cells and Partitioning", 7);
        scene.world().showSection(util.select().fromTo(1, 1, 3, 4, 1, 3), EnumFacing.DOWN);
        use(scene, util, "item_storage_cell_1k", 2, 1, 3);
        explain(scene, util, "cells.insert", 2, 1, 3);
        gui(scene, "drive", 2, 1, 3);
        use(scene, util, "item_storage_cell_64k", 2, 1, 3);
        explain(scene, util, "cells.capacity", 2, 1, 3);
        show(scene, util, 4, 1, 1);
        use(scene, util, "item_storage_cell_1k", 4, 1, 1);
        explain(scene, util, "cells.partition", 4, 1, 1);
        gui(scene, "cell_workbench", 4, 1, 1);
        flow(scene, util, stack("item_storage_cell_1k"), 4, 1, 2, 3);
        explain(scene, util, "cells.return", 2, 1, 3);
        explain(scene, util, "cells.safety", 2, 1, 3);
        scene.markAsFinished();
    }

    public static void channels(SceneBuilder scene, SceneBuildingUtil util) {
        begin(scene, "channels", "Channels and Cable Capacity", 9);
        scene.world().showSection(util.select().layersFrom(1), EnumFacing.DOWN);
        highlight(scene, util, PonderPalette.GREEN, 1, 1, 3, 1, 1, 3);
        explain(scene, util, "channels.controller", 1, 1, 3);
        gui(scene, "network_status", 1, 1, 3);
        highlight(scene, util, PonderPalette.INPUT, 2, 1, 3, 4, 1, 3);
        explain(scene, util, "channels.eight", 3, 1, 3);
        highlight(scene, util, PonderPalette.OUTPUT, 5, 1, 3, 7, 1, 3);
        explain(scene, util, "channels.dense", 5, 1, 3);
        highlight(scene, util, PonderPalette.RED, 3, 1, 5, 5, 1, 5);
        explain(scene, util, "channels.color", 4, 1, 5);
        highlight(scene, util, PonderPalette.WHITE, 3, 1, 7, 5, 1, 7);
        explain(scene, util, "channels.fiber", 4, 1, 7);
        scene.markAsFinished();
    }

    public static void storageBus(SceneBuilder scene, SceneBuildingUtil util) {
        begin(scene, "storage_bus", "Using External Inventories", 7);
        scene.world().showSection(util.select().fromTo(1, 1, 3, 4, 1, 3), EnumFacing.DOWN);
        show(scene, util, 5, 1, 3);
        highlight(scene, util, PonderPalette.INPUT, 4, 1, 3, 5, 1, 3);
        explain(scene, util, "storage.attach", 4, 1, 3);
        use(scene, util, "storage_bus", 4, 1, 3);
        explain(scene, util, "storage.access", 4, 1, 3);
        gui(scene, "storage_bus", 4, 1, 3);
        flow(scene, util, new ItemStack(Items.IRON_INGOT), 3, 3, 5, 3);
        explain(scene, util, "storage.priority", 5, 1, 3);
        explain(scene, util, "storage.filter", 4, 1, 3);
        explain(scene, util, "storage.loop", 4, 1, 3);
        scene.markAsFinished();
    }

    public static void importExport(SceneBuilder scene, SceneBuildingUtil util) {
        begin(scene, "import_export", "Importing and Exporting Items", 7);
        scene.world().showSection(util.select().layersFrom(1), EnumFacing.DOWN);
        highlight(scene, util, PonderPalette.INPUT, 1, 1, 1, 2, 1, 1);
        flow(scene, util, new ItemStack(Items.IRON_INGOT), 1, 1, 3, 3);
        explain(scene, util, "io.import", 2, 1, 1);
        gui(scene, "import_bus", 2, 1, 1);
        use(scene, util, "export_bus", 4, 1, 5);
        highlight(scene, util, PonderPalette.OUTPUT, 4, 1, 5, 5, 1, 5);
        explain(scene, util, "io.filter", 4, 1, 5);
        gui(scene, "export_bus", 4, 1, 5);
        flow(scene, util, new ItemStack(Items.IRON_INGOT), 3, 3, 5, 5);
        explain(scene, util, "io.export", 4, 1, 5);
        explain(scene, util, "io.storage", 3, 1, 3);
        explain(scene, util, "io.control", 4, 1, 5);
        scene.markAsFinished();
    }

    public static void autocrafting(SceneBuilder scene, SceneBuildingUtil util) {
        begin(scene, "autocrafting", "Autocrafting with a Pattern Provider", 7);
        scene.world().showSection(util.select().fromTo(1, 1, 3, 3, 1, 4), EnumFacing.DOWN);
        show(scene, util, 1, 1, 2);
        use(scene, util, "blank_pattern", 2, 1, 3);
        explain(scene, util, "craft.encode", 2, 1, 3);
        gui(scene, "pattern_crafting", 2, 1, 3);
        show(scene, util, 4, 1, 3);
        show(scene, util, 5, 1, 3);
        use(scene, util, "crafting_pattern", 4, 1, 3);
        explain(scene, util, "craft.provider", 4, 1, 3);
        gui(scene, "pattern_provider", 4, 1, 3);
        scene.world().showSection(util.select().fromTo(2, 1, 1, 3, 1, 1), EnumFacing.DOWN);
        show(scene, util, 2, 1, 2);
        highlight(scene, util, PonderPalette.GREEN, 2, 1, 1, 3, 1, 1);
        explain(scene, util, "craft.cpu", 2, 1, 1);
        gui(scene, "crafting_cpu", 2, 1, 1);
        use(scene, util, "crafting_terminal", 2, 1, 3);
        explain(scene, util, "craft.request", 2, 1, 3);
        gui(scene, "craft_amount", 2, 1, 3);
        gui(scene, "craft_confirm", 2, 1, 3);
        flow(scene, util, new ItemStack(Items.IRON_INGOT), 3, 3, 5, 3);
        flow(scene, util, new ItemStack(Item.getItemFromBlock(net.minecraft.init.Blocks.IRON_BLOCK)), 5, 3, 3, 3);
        explain(scene, util, "craft.result", 5, 1, 3);
        explain(scene, util, "craft.interface", 4, 1, 3);
        scene.markAsFinished();
    }

    public static void processing(SceneBuilder scene, SceneBuildingUtil util) {
        begin(scene, "processing", "Processing Patterns and Product Return", 7);
        scene.scaleSceneView(1.08f);
        scene.setSceneOffsetY(.5f);
        scene.world().showSection(util.select().layersFrom(1), EnumFacing.DOWN);
        use(scene, util, "blank_pattern", 2, 1, 3);
        explain(scene, util, "processing.encode", 2, 1, 3);
        gui(scene, "pattern_processing", 2, 1, 3);
        use(scene, util, "processing_pattern", 5, 3, 3);
        highlight(scene, util, PonderPalette.INPUT, 5, 2, 3, 5, 3, 3);
        explain(scene, util, "processing.provider", 5, 3, 3);
        gui(scene, "pattern_provider", 5, 3, 3);
        scene.overlay().showControls(util.vector().topOf(5, 2, 3), Pointing.DOWN, 75)
            .rightClick().withItem(new ItemStack(Items.COAL));
        flow(scene, util, new ItemStack(Item.getItemFromBlock(net.minecraft.init.Blocks.IRON_ORE)), 4, 3, 5, 3);
        explain(scene, util, "processing.machine", 5, 2, 3);
        highlight(scene, util, PonderPalette.OUTPUT, 5, 1, 3, 5, 1, 3);
        flow(scene, util, new ItemStack(Items.IRON_INGOT), 5, 3, 3, 3);
        explain(scene, util, "processing.return", 5, 1, 3);
        explain(scene, util, "processing.wait", 2, 1, 1);
        explain(scene, util, "processing.blocking", 5, 3, 3);
        scene.markAsFinished();
    }

    public static void p2p(SceneBuilder scene, SceneBuildingUtil util) {
        begin(scene, "p2p", "Connecting ME P2P Tunnels", 9);
        scene.world().showSection(util.select().layersFrom(1), EnumFacing.DOWN);
        highlight(scene, util, PonderPalette.INPUT, 1, 1, 3, 2, 1, 3);
        explain(scene, util, "p2p.input", 2, 1, 3);
        highlight(scene, util, PonderPalette.GREEN, 2, 1, 4, 6, 1, 5);
        explain(scene, util, "p2p.carrier", 4, 1, 5);
        scene.overlay().showControls(util.vector().topOf(2, 1, 3), Pointing.DOWN, 80)
            .rightClick().whileSneaking().withItem(stack("memory_card"));
        explain(scene, util, "p2p.save", 2, 1, 3);
        use(scene, util, "memory_card", 6, 1, 3);
        scene.world().modifyBlockEntityNBT(util.select().position(6, 1, 3), TileEntity.class, nbt -> {
            nbt.getCompoundTag("east").setShort("freq", (short) 4660);
            nbt.getCompoundTag("east").setBoolean("output", true);
        });
        scene.overlay().showBigLine(PonderPalette.OUTPUT, util.vector().centerOf(2, 1, 3),
            util.vector().centerOf(6, 1, 3), 100);
        explain(scene, util, "p2p.bind", 6, 1, 3);
        highlight(scene, util, PonderPalette.OUTPUT, 7, 1, 3, 8, 1, 3);
        explain(scene, util, "p2p.capacity", 7, 1, 3);
        explain(scene, util, "p2p.check", 4, 1, 5);
        gui(scene, "advanced_memory_card", 2, 1, 3);
        scene.markAsFinished();
    }
}
