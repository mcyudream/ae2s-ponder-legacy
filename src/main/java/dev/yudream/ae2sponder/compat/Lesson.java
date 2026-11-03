package dev.yudream.ae2sponder.compat;

import java.util.ArrayList;
import java.util.List;
import net.createmod.ponder.api.scene.PonderStoryBoard;

/** One stable scene ID per lesson, shared by all relevant real AE2S items. */
public enum Lesson {
    FIRST_NETWORK("first_network", "basics", AE2SScenes::firstNetwork, 420,
        "vibration_chamber", "energy_acceptor", "energy_cell", "drive", "terminal", "crafting_terminal"),
    STORAGE_CELLS("storage_cells", "basics", AE2SScenes::storageCells, 400,
        "drive", "cell_workbench", "item_storage_cell_1k", "item_storage_cell_4k", "item_storage_cell_16k",
        "item_storage_cell_64k", "item_storage_cell_256k", "fluid_storage_cell_1k"),
    CHANNELS("channels", "basics", AE2SScenes::channels, 220,
        "controller", "fluix_glass_cable", "fluix_smart_cable", "fluix_smart_dense_cable", "quartz_fiber"),
    STORAGE_BUS("storage_bus", "automation", AE2SScenes::storageBus, 230,
        "storage_bus", "interface"),
    IMPORT_EXPORT("import_export", "automation", AE2SScenes::importExport, 230,
        "import_bus", "export_bus", "level_emitter"),
    AUTOCRAFTING("autocrafting", "crafting", AE2SScenes::autocrafting, 400,
        "pattern_provider", "cable_pattern_provider", "molecular_assembler", "pattern_encoding_terminal",
        "blank_pattern", "crafting_pattern", "1k_crafting_storage", "crafting_accelerator", "crafting_unit"),
    PROCESSING("processing", "crafting", AE2SScenes::processing, 400,
        "pattern_provider", "processing_pattern", "pattern_encoding_terminal", "import_bus"),
    P2P("p2p", "networks", AE2SScenes::p2p, 560,
        "me_p2p_tunnel", "memory_card", "advanced_memory_card");

    public final String id, category;
    public final PonderStoryBoard board;
    public final int previewTick;
    private final List<String> components;

    Lesson(String id, String category, PonderStoryBoard board, int previewTick, String... components) {
        this.id = id;
        this.category = category;
        this.board = board;
        this.previewTick = previewTick;
        this.components = List.of(components);
    }

    public List<String> components() {
        if (this != CHANNELS) return components;
        var all = new ArrayList<>(components);
        String[] colors = {"white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray",
            "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black", "fluix"};
        for (String color : colors)
            for (String type : new String[]{"glass_cable", "covered_cable", "smart_cable", "covered_dense_cable", "smart_dense_cable"}) {
                String cable = color + "_" + type;
                if (!all.contains(cable)) all.add(cable);
            }
        return List.copyOf(all);
    }
}
