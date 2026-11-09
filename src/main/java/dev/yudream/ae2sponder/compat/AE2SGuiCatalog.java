package dev.yudream.ae2sponder.compat;

import com.google.gson.JsonParser;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import net.minecraft.client.Minecraft;
import net.minecraft.util.ResourceLocation;

/** Reloaded with the client plugin; keeps shared-screen contexts separate without linking server code. */
public final class AE2SGuiCatalog {
    public record Entry(String id, String screen, String style, String host, List<String> widgets) {}
    private final Map<String, Entry> entries;

    public AE2SGuiCatalog() {
        try (var resource = Minecraft.getMinecraft().getResourceManager().getResource(
                new ResourceLocation("ae2s_ponder", "ponder/gui/coverage.json"));
             var reader = new InputStreamReader(resource.getInputStream(), StandardCharsets.UTF_8)) {
            var root = new JsonParser().parse(reader).getAsJsonObject();
            var result = new LinkedHashMap<String, Entry>();
            for (var element : root.getAsJsonArray("lessons")) {
                var row = element.getAsJsonObject();
                var widgets = new java.util.ArrayList<String>();
                for (var widget : row.getAsJsonArray("widgets")) widgets.add(widget.getAsString());
                String id = row.get("id").getAsString();
                result.put(id, new Entry(id, row.get("screen").getAsString(), row.get("style").getAsString(),
                    row.get("host").getAsString(), List.copyOf(widgets)));
            }
            entries = Map.copyOf(result);
        } catch (java.io.IOException | RuntimeException failure) {
            throw new IllegalStateException("Cannot load the AE2S GUI coverage catalog", failure);
        }
    }

    public Entry get(String id) { return entries.get(id); }
    public java.util.Collection<Entry> all() { return entries.values(); }
}
