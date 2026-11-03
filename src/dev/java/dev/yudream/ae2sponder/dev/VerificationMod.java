package dev.yudream.ae2sponder.dev;

import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import java.nio.file.Files;
import java.nio.file.Path;
import net.minecraftforge.fml.common.FMLCommonHandler;
import net.minecraftforge.fml.common.Loader;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.SidedProxy;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLServerStartedEvent;

/** An external development jar, never included in the tutorial addon. */
@Mod(modid = "ae2s_ponder_verification", name = "AE2S Ponder verification", version = "1",
    dependencies = "required-after:ae2;after:ae2s-ponder-legacy", acceptableRemoteVersions = "*")
public final class VerificationMod {
    @SidedProxy(clientSide = "dev.yudream.ae2sponder.dev.ClientVerification",
        serverSide = "dev.yudream.ae2sponder.dev.VerificationMod$CommonVerification")
    public static CommonVerification proxy;

    @Mod.EventHandler public void init(FMLInitializationEvent event) {
        if (Boolean.getBoolean("ae2sponder.smoke")) proxy.init();
    }

    @Mod.EventHandler public void serverStarted(FMLServerStartedEvent event) throws Exception {
        if (!Boolean.getBoolean("ae2sponder.smoke") || FMLCommonHandler.instance().getSide().isClient()) return;
        var checks = new JsonArray();
        if (!Loader.isModLoaded("ae2")) throw new IllegalStateException("AE2S missing on dedicated server");
        verifyCleanroom();
        checks.add("Actual Cleanroom " + cleanroomVersion() + " matches the configured verification baseline");
        checks.add("Dedicated server reached FMLServerStarted with AE2S and tutorial addon installed");
        checks.add("Ponder present: " + Loader.isModLoaded("ponder-legacy"));
        report(Path.of("ae2s-ponder-smoke"), "PASS", checks, null);
        FMLCommonHandler.instance().getMinecraftServerInstance().initiateShutdown();
    }

    public static void report(Path output, String result, JsonArray checks, Throwable failure) {
        try {
            Files.createDirectories(output);
            var json = new JsonObject();
            json.addProperty("result", result);
            json.addProperty("cleanroom", cleanroomVersion());
            json.addProperty("java", System.getProperty("java.version"));
            json.addProperty("artifacts", Boolean.getBoolean("ae2sponder.packaged") ? "installation" : "development");
            json.addProperty("ae2s", Loader.instance().getIndexedModList().get("ae2").getVersion());
            json.addProperty("ponder", Loader.isModLoaded("ponder-legacy"));
            json.add("checks", checks);
            if (failure != null) {
                var trace = new java.io.StringWriter();
                failure.printStackTrace(new java.io.PrintWriter(trace));
                json.addProperty("failure", trace.toString());
            }
            Files.writeString(output.resolve("report.json"), new GsonBuilder().setPrettyPrinting().create().toJson(json));
        } catch (Exception exception) { throw new RuntimeException(exception); }
    }

    static String cleanroomVersion() {
        return Loader.instance().getIndexedModList().get("cleanroom").getVersion();
    }

    static void verifyCleanroom() {
        String expected = System.getProperty("ae2sponder.expectedCleanroom");
        if (expected == null || !expected.equals(cleanroomVersion()))
            throw new IllegalStateException("Unexpected Cleanroom: " + cleanroomVersion() + ", expected " + expected);
    }

    public static class CommonVerification { public void init() {} }
}
