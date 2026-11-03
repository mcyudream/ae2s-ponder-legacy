package dev.yudream.ae2sponder.dev;

import com.google.gson.JsonArray;
import java.nio.file.Path;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.GuiMainMenu;
import net.minecraft.util.ScreenShotHelper;
import net.minecraft.world.GameType;
import net.minecraft.world.WorldSettings;
import net.minecraft.world.WorldType;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.fml.common.Loader;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;
import net.minecraftforge.fml.common.gameevent.TickEvent;
import org.lwjgl.opengl.GL11;

/** Safe to load without Ponder. Optional verification is loaded by class name only after the guard. */
public final class ClientVerification extends VerificationMod.CommonVerification {
    private final Minecraft mc = Minecraft.getMinecraft();
    private final JsonArray checks = new JsonArray();
    private Path output;
    private int phase, ticks, waitUntil, exitAt = Integer.MAX_VALUE;
    private String capture;
    private OptionalVerification ponder;

    public interface OptionalVerification {
        void prepare(ClientVerification host) throws Exception;
        boolean next(ClientVerification host) throws Exception;
    }

    @Override public void init() {
        output = mc.gameDir.toPath().resolve("ae2s-ponder-smoke");
        mc.gameSettings.pauseOnLostFocus = false;
        mc.gameSettings.renderDistanceChunks = 2;
        mc.gameSettings.guiScale = 2;
        mc.gameSettings.fboEnable = true;
        mc.gameSettings.setSoundLevel(net.minecraft.util.SoundCategory.MASTER, 0);
        mc.getTutorial().setStep(net.minecraft.client.tutorial.TutorialSteps.NONE);
        MinecraftForge.EVENT_BUS.register(this);
        VerificationMod.report(output, "STARTING", checks, null);
    }

    public void check(boolean condition, String description) {
        if (!condition) throw new IllegalStateException(description);
        checks.add(description);
        VerificationMod.report(output, "RUNNING", checks, null);
    }

    public void screenshot(String filename) { capture = filename; waitUntil = ticks + 5; }

    @SubscribeEvent public void tick(TickEvent.ClientTickEvent event) {
        if (event.phase != TickEvent.Phase.END) return;
        ticks++;
        if (ticks >= exitAt) { mc.shutdown(); return; }
        if (exitAt != Integer.MAX_VALUE || ticks < waitUntil || capture != null) return;
        try {
            if (ticks > 4800) throw new IllegalStateException("Client verification timeout at phase " + phase);
            switch (phase) {
                case 0:
                    if (!(mc.currentScreen instanceof GuiMainMenu)) return;
                    VerificationMod.verifyCleanroom();
                    check(true, "Actual Cleanroom " + VerificationMod.cleanroomVersion() + " matches the configured verification baseline");
                    check(Loader.isModLoaded("ae2s-ponder-legacy") && Loader.isModLoaded("ae2"), "FML discovers AE2S and the tutorial addon");
                    check("1.1.0".equals(Loader.instance().getIndexedModList().get("ae2").getVersion()), "Actual AE2S 1.1.0 loaded");
                    var settings = new WorldSettings(1729, GameType.CREATIVE, false, false, WorldType.FLAT);
                    settings.setGeneratorOptions("3;minecraft:bedrock,2*minecraft:dirt,minecraft:grass;1;");
                    settings.enableCommands();
                    String world = Loader.isModLoaded("ponder-legacy") ? "ae2s-ponder-smoke-with" : "ae2s-ponder-smoke-without";
                    mc.launchIntegratedServer(world, "AE2S Ponder verification", settings);
                    phase++; break;
                case 1:
                    if (mc.world == null || mc.player == null || mc.getIntegratedServer() == null) return;
                    check(true, "Client and integrated server enter a world");
                    if (Loader.isModLoaded("ponder-legacy")) {
                        ponder = (OptionalVerification) Class.forName("dev.yudream.ae2sponder.dev.PonderVerification")
                            .getDeclaredConstructor().newInstance();
                        ponder.prepare(this);
                        phase++;
                    } else {
                        check(true, "World starts with AE2S Ponder installed and no Ponder runtime");
                        finish();
                    }
                    break;
                default:
                    if (ponder.next(this)) finish();
            }
        } catch (Throwable failure) {
            failure.printStackTrace();
            VerificationMod.report(output, "FAIL", checks, failure);
            exitAt = ticks + 10;
        }
    }

    private void finish() {
        VerificationMod.report(output, "PASS", checks, null);
        exitAt = ticks + 10;
    }

    @SubscribeEvent public void render(TickEvent.RenderTickEvent event) {
        if (event.phase != TickEvent.Phase.END || capture == null) return;
        try {
            ScreenShotHelper.saveScreenshot(output.toFile(), capture, mc.displayWidth, mc.displayHeight, mc.getFramebuffer());
            check(GL11.glGetError() == GL11.GL_NO_ERROR, "No OpenGL errors: " + capture);
        } catch (Throwable failure) {
            VerificationMod.report(output, "FAIL", checks, failure);
            exitAt = ticks + 10;
        } finally { capture = null; }
    }
}
