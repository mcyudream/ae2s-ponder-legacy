package dev.yudream.ae2sponder.dev;

import ae2.tile.networking.TileCableBus;
import dev.yudream.ae2sponder.AE2SPonder;
import dev.yudream.ae2sponder.compat.Lesson;
import dev.yudream.ae2sponder.compat.PonderAE2SPlugin;
import java.util.List;
import java.util.Map;
import java.util.LinkedHashMap;
import net.createmod.ponder.api.registration.StoryBoardEntry;
import net.createmod.ponder.foundation.PonderIndex;
import net.createmod.ponder.foundation.structure.PonderStructureLoader;
import net.createmod.ponder.foundation.ui.PonderUI;
import net.minecraft.client.Minecraft;
import net.minecraft.client.resources.Language;
import net.minecraft.item.Item;
import net.minecraft.tileentity.TileEntity;
import net.minecraft.util.EnumFacing;
import net.minecraft.util.ResourceLocation;

/** Real structures, AE2S multipart reconstruction, full playback, backward seek, languages and rendering. */
public final class PonderVerification implements ClientVerification.OptionalVerification {
    private final Minecraft mc = Minecraft.getMinecraft();
    private final Map<String, StoryBoardEntry> entries = new LinkedHashMap<>();
    private int lesson, language, step;
    private Language previousLanguage;
    private P2PNetworkVerification topology = new P2PNetworkVerification();
    private MachineNetworkVerification wiring = new MachineNetworkVerification();

    @Override public void prepare(ClientVerification host) {
        for (var entry : PonderIndex.getSceneAccess().getRegisteredEntries()) {
            if (!AE2SPonder.MOD_ID.equals(entry.getValue().getNamespace())) continue;
            entries.putIfAbsent(entry.getValue().getDeclaredSceneId().getPath(), entry.getValue());
            host.check(Item.REGISTRY.containsKey(entry.getKey()), "Real AE2S scene subject: " + entry.getKey());
        }
        host.check(entries.size() == Lesson.values().length, "Exactly eight tutorial scenes registered by guarded IMC");
        var diagnostics = PonderIndex.getDiagnosticSnapshot(net.createmod.ponder.api.diagnostic.PonderDiagnosticView.EFFECTIVE);
        host.check(diagnostics.getScenes().stream()
            .filter(scene -> AE2SPonder.MOD_ID.equals(scene.getPluginId()))
            .noneMatch(net.createmod.ponder.api.diagnostic.PonderSceneDiagnostic::hasErrors),
            "All AE2S tutorial registrations are free of Ponder diagnostic errors");
        previousLanguage = mc.getLanguageManager().getCurrentLanguage();
    }

    @Override public boolean next(ClientVerification host) throws Exception {
        if (topology != null) {
            if (!topology.tick(host)) return false;
            topology = null;
        }
        if (wiring != null) {
            if (!wiring.tick(host)) return false;
            wiring = null;
        }
        if (lesson >= Lesson.values().length) {
            mc.gameSettings.language = previousLanguage.getLanguageCode();
            mc.getLanguageManager().setCurrentLanguage(previousLanguage);
            mc.refreshResources();
            mc.displayGuiScreen(null);
            return true;
        }
        Lesson current = Lesson.values()[lesson];
        String code = language == 0 ? "en_us" : "zh_cn";
        if (step == 0) {
            if (!code.equals(mc.getLanguageManager().getCurrentLanguage().getLanguageCode())) {
                mc.gameSettings.language = code;
                mc.getLanguageManager().setCurrentLanguage(mc.getLanguageManager().getLanguage(code));
                mc.refreshResources();
            }
            var source = new PonderStructureLoader().load(PonderAE2SPlugin.id(current.id));
            host.check(source.getDiagnostics().isEmpty(), current.id + ": structure has no unresolved blocks or properties");
            var scenes = PonderIndex.getSceneAccess().compile(List.of(entries.get(current.id)));
            var scene = scenes.get(0);
            host.check(scene.getId().equals(PonderAE2SPlugin.id(current.id)), current.id + ": stable scene identity");
            for (var block : source.getBlocks()) {
                var nbt = block.getTileData();
                if (nbt == null) continue;
                TileEntity tile = scene.getWorld().getTileEntity(block.getPosition());
                host.check(tile != null && nbt.getString("id").equals(TileEntity.getKey(tile.getClass()).toString()),
                    current.id + ": real tile reconstructed at " + block.getPosition());
                if (!(tile instanceof TileCableBus bus)) continue;
                for (String key : new String[]{"cable", "down", "up", "north", "south", "west", "east"}) {
                    if (!nbt.hasKey(key)) continue;
                    var part = bus.getPart("cable".equals(key) ? null : EnumFacing.byName(key));
                    host.check(part != null && nbt.getCompoundTag(key).getString("id")
                        .equals(part.getPartItem().asItem().getRegistryName().toString()),
                        current.id + ": multipart " + key + " restored at " + block.getPosition());
                }
            }
            scene.seek(scene.getTotalTicks());
            host.check(scene.isFinished(), current.id + ": full timeline executes");
            if (current == Lesson.P2P) {
                var output = ((TileCableBus) scene.getWorld().getTileEntity(new net.minecraft.util.math.BlockPos(6, 1, 3)))
                    .getPart(EnumFacing.EAST);
                var nbt = new net.minecraft.nbt.NBTTagCompound();
                output.writeToNBT(nbt);
                host.check(nbt.getBoolean("output") && nbt.getShort("freq") == 4660,
                    "P2P animation applies output role and matching frequency");
            }
            scene.seek(0);
            if (current == Lesson.P2P) {
                var output = ((TileCableBus) scene.getWorld().getTileEntity(new net.minecraft.util.math.BlockPos(6, 1, 3)))
                    .getPart(EnumFacing.EAST);
                var nbt = new net.minecraft.nbt.NBTTagCompound();
                output.writeToNBT(nbt);
                host.check(!nbt.getBoolean("output") && nbt.getShort("freq") == 0,
                    "Backward seek restores the unbound P2P tunnel");
            }
            scene.seek(current.previewTick);
            host.check(scene.getCurrentTick() == current.previewTick, current.id + ": backward seek and replay");
            String title = net.minecraft.client.resources.I18n.format("ae2s_ponder.ponder." + current.id + ".header");
            host.check(title.equals(scene.getTitle()), current.id + ": " + code + " title resolves");
            String first = switch (current) {
                case FIRST_NETWORK -> "first.power";
                case STORAGE_CELLS -> "cells.insert";
                case CHANNELS -> "channels.controller";
                case STORAGE_BUS -> "storage.attach";
                case IMPORT_EXPORT -> "io.import";
                case AUTOCRAFTING -> "craft.encode";
                case PROCESSING -> "processing.encode";
                case P2P -> "p2p.input";
            };
            String text = PonderIndex.getLangAccess().getShared(PonderAE2SPlugin.id(first));
            host.check(text.equals(net.minecraft.client.resources.I18n.format("ae2s_ponder.ponder.shared." + first)),
                current.id + ": " + code + " narration resolves");
            mc.displayGuiScreen(new PonderUI(scenes));
            ((PonderUI) mc.currentScreen).seekToTime(current.previewTick);
            step++;
        } else {
            host.check(mc.currentScreen instanceof PonderUI, current.id + ": Ponder viewer opens");
            host.screenshot(current.id + "-" + code + ".png");
            step = 0;
            if (++lesson == Lesson.values().length && language == 0) { language = 1; lesson = 0; }
        }
        return false;
    }
}
