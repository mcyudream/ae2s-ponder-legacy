package dev.yudream.ae2sponder.compat;

import dev.yudream.ae2sponder.AE2SPonder;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import net.createmod.ponder.api.registration.PonderPlugin;
import net.createmod.ponder.api.registration.PonderSceneRegistrationHelper;
import net.createmod.ponder.api.registration.PonderTagRegistrationHelper;
import net.createmod.ponder.api.registration.SharedTextRegistrationHelper;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.util.ResourceLocation;

/** Loaded by guarded client IMC only; there is intentionally no ServiceLoader descriptor. */
public final class PonderAE2SPlugin implements PonderPlugin {
    @Override public String getModId() { return AE2SPonder.MOD_ID; }

    @Override public void registerTutorials(net.createmod.ponder.api.guide.TutorialRegistrationHelper helper) {
        helper.addMarkdownIndex(id("index"));
    }

    @Override public void registerScenes(PonderSceneRegistrationHelper<ResourceLocation> helper) {
        for (Lesson lesson : Lesson.values()) {
            for (String component : lesson.components()) {
                ResourceLocation item = ae2(component);
                if (!Item.REGISTRY.containsKey(item))
                    throw new IllegalStateException("Missing AE2S 1.1.0 tutorial item: " + item);
                helper.addStoryBoard(item, id(lesson.id), lesson.board, id(lesson.category))
                    .identifiedBy(id(lesson.id));
            }
        }
    }

    @Override public void registerTags(PonderTagRegistrationHelper<ResourceLocation> helper) {
        tag(helper, "basics", "ME Network Basics", "Power, storage cells and channels.", "drive");
        tag(helper, "automation", "Storage and Automation", "External inventories and item transfers.", "import_bus");
        tag(helper, "crafting", "Autocrafting", "Encode patterns, build a CPU and return products.", "pattern_provider");
        tag(helper, "networks", "P2P Networks", "Connect tunnel inputs and outputs using a memory card.", "me_p2p_tunnel");
        for (Lesson lesson : Lesson.values())
            for (String component : lesson.components())
                helper.addTagToComponent(ae2(component), id(lesson.category));
    }

    private static void tag(PonderTagRegistrationHelper<ResourceLocation> helper, String name,
                            String title, String description, String icon) {
        helper.registerTag(id(name)).title(title).description(description)
            .item(new ItemStack(Item.REGISTRY.getObject(ae2(icon))), true, true).addToIndex().register();
    }

    @Override public void registerSharedText(SharedTextRegistrationHelper helper) {
        String prefix = AE2SPonder.MOD_ID + ".ponder.shared.";
        try (var stream = getClass().getResourceAsStream("/assets/ae2s_ponder/lang/en_us.lang")) {
            if (stream == null) throw new IllegalStateException("Missing tutorial source language");
            try (var reader = new BufferedReader(new InputStreamReader(stream, StandardCharsets.UTF_8))) {
                for (String line; (line = reader.readLine()) != null;) {
                    int split = line.indexOf('=');
                    if (split > 0 && line.startsWith(prefix))
                        helper.registerSharedText(line.substring(prefix.length(), split), line.substring(split + 1));
                }
            }
        } catch (java.io.IOException failure) {
            throw new IllegalStateException("Could not read AE2S tutorial text", failure);
        }
    }

    public static ResourceLocation id(String path) { return new ResourceLocation(AE2SPonder.MOD_ID, path); }
    public static ResourceLocation ae2(String path) { return new ResourceLocation("ae2", path); }
}
