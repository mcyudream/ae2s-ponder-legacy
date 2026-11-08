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
    private GuiLessonVerification guis = new GuiLessonVerification();

    @Override public void prepare(ClientVerification host) {
        for (var entry : PonderIndex.getSceneAccess().getRegisteredEntries()) {
            if (!AE2SPonder.MOD_ID.equals(entry.getValue().getNamespace())) continue;
            entries.putIfAbsent(entry.getValue().getDeclaredSceneId().getPath(), entry.getValue());
            host.check(Item.REGISTRY.containsKey(entry.getKey()), "Real AE2S scene subject: " + entry.getKey());
        }
        host.check(entries.size() == 24, "All 24 AE2S tutorial animations registered by guarded IMC");
        var diagnostics = PonderIndex.getDiagnosticSnapshot(net.createmod.ponder.api.diagnostic.PonderDiagnosticView.EFFECTIVE);
        host.check(diagnostics.getScenes().stream()
            .filter(scene -> AE2SPonder.MOD_ID.equals(scene.getPluginId()))
            .noneMatch(net.createmod.ponder.api.diagnostic.PonderSceneDiagnostic::hasErrors),
            "All AE2S tutorial registrations are free of Ponder diagnostic errors");
        previousLanguage = mc.getLanguageManager().getCurrentLanguage();
    }

    private int guideIndex, guideLanguage, guidePhase;
    private net.createmod.ponder.api.guide.Tutorial currentGuide;
    private boolean verifyGuides(ClientVerification host) throws Exception {
        String code = guideLanguage == 0 ? "en_us" : "zh_cn";
        if (!code.equals(mc.getLanguageManager().getCurrentLanguage().getLanguageCode())) {
            mc.gameSettings.language = code;
            mc.getLanguageManager().setCurrentLanguage(mc.getLanguageManager().getLanguage(code));
            mc.refreshResources();
        }
        var pages = PonderIndex.getTutorials().all().stream().filter(p -> p.id().getNamespace().equals(AE2SPonder.MOD_ID)).toList();
        host.check(pages.size() == 25, "All 25 bilingual AE2S guide pages register");
        var generated = pages.stream().filter(p -> !p.scenes().isEmpty()).toList();
        if (guideIndex >= generated.size()) {
            if (guideLanguage++ == 0) { guideIndex = 0; return false; }
            return true;
        }
        currentGuide = generated.get(guideIndex);
        if (guidePhase == 0) {
            for (var component : currentGuide.components()) host.check(Item.REGISTRY.containsKey(component), "Markdown subject exists in AE2S: " + component);
            var definition = currentGuide.scenes().get(0);
            var source = new PonderStructureLoader().load(definition.getStructure());
            host.check(source.getDiagnostics().isEmpty(), currentGuide.id()+": native Markdown structure resolves");
            var scene = net.createmod.ponder.client.guide.Tutorials.compile(definition);
            for (var block : source.getBlocks()) if (block.getTileData() != null) {
                var tile = scene.getWorld().getTileEntity(block.getPosition());
                host.check(tile != null && block.getTileData().getString("id").equals(TileEntity.getKey(tile.getClass()).toString()), currentGuide.id()+": real native tile " + block.getPosition());
            }
            scene.seek(scene.getTotalTicks());host.check(scene.isFinished(), currentGuide.id()+": full Markdown animation executes");
            if (currentGuide.id().getPath().equals("processors") || currentGuide.id().getPath().equals("interfaces"))
                verifyGuiClips(host,scene,currentGuide.id().getPath());
            scene.seek(0);host.check(scene.getCurrentTick()==0,currentGuide.id()+": Markdown animation can rewind");
            host.check(scene.getNarration().size()>=4,currentGuide.id()+": every authored section has animation narration");
            host.check(scene.getTitle().equals(currentGuide.title()),currentGuide.id()+": " + code + " shared title resolves");
            mc.displayGuiScreen(new PonderUI(List.of(scene)));((PonderUI)mc.currentScreen).seekToTime(70);guidePhase=1;
        } else if (guidePhase == 1) {
            host.screenshot(currentGuide.id().getPath()+"-markdown-"+code+".png");
            if (guideIndex==0 || currentGuide.id().getPath().equals("spatial_io")) {
                mc.displayGuiScreen(new net.createmod.ponder.client.guide.GuideScreen(currentGuide.components().get(0),currentGuide.id()));guidePhase=2;
            } else {guideIndex++;guidePhase=0;}
        } else {
            host.screenshot(currentGuide.id().getPath()+"-guide-"+code+".png");guideIndex++;guidePhase=0;
        }
        return false;
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
        if (guis != null) {
            if (!guis.tick(host)) return false;
            guis = null;
        }
        if (lesson >= Lesson.values().length) {
            if (!verifyGuides(host)) return false;
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
            if (current==Lesson.FIRST_NETWORK||current==Lesson.STORAGE_CELLS||current==Lesson.AUTOCRAFTING||current==Lesson.PROCESSING)
                verifyGuiClips(host,scene,current.id);
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
            if (language == 0 && (current == Lesson.FIRST_NETWORK || current == Lesson.P2P)) {
                var plan = net.createmod.ponder.api.projection.ProjectionPlan.capture(scene);
                var projection = new net.createmod.ponder.client.projection.ProjectionSession(plan, new net.minecraft.util.math.BlockPos(200,80,200));
                host.check(projection.unknown.isEmpty(), current.id + ": native AE2S construction materials resolve");
                String part = current == Lesson.P2P ? "ae2:me_p2p_tunnel" : "ae2:terminal";
                host.check(projection.rows.stream().anyMatch(r -> r.target().item().toString().equals(part)), current.id + ": composite cable bus counts actual face parts");
                host.check(projection.rows.stream().anyMatch(r -> r.target().item().getPath().endsWith("_cable")), current.id + ": composite cable bus counts cable items");
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

    private void verifyGuiClips(ClientVerification host, net.createmod.ponder.foundation.PonderScene scene, String name) {
        host.check(!scene.getGuiAnimations().isEmpty(),name+": machine animation includes authored GUI clips");
        for(var clip:scene.getGuiAnimations()) {
            var tutorial=net.createmod.ponder.client.guitutorial.GuiTutorials.resolve(clip.tutorial().toString());
            host.check(tutorial.id().equals(clip.tutorial()),name+": GUI clip resolves the same live/demo definition");
            scene.seek(clip.start()+100);
            host.check(scene.getActiveGuiAnimations().contains(clip),name+": seeking activates its GUI segment");
            int frame=clip.tutorialTick(scene,new net.createmod.ponder.gui.GuiTutorialSession(tutorial).lastTick());
            scene.seek(0);scene.seek(clip.start()+100);
            host.check(frame==clip.tutorialTick(scene,new net.createmod.ponder.gui.GuiTutorialSession(tutorial).lastTick()),name+": GUI replay uses the same scene clock");
        }
    }
}
