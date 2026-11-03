package dev.yudream.ae2sponder;

import net.minecraftforge.fml.common.Loader;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLInterModComms;

/** The entry point deliberately has no references to optional Ponder or client classes. */
@Mod(modid = AE2SPonder.LEGACY_MOD_ID, name = "AE2S Ponder Legacy", version = "0.1.0",
    acceptedMinecraftVersions = "[1.12.2]", clientSideOnly = true, acceptableRemoteVersions = "*",
    dependencies = "required-after:cleanroom@[0.4.0,);required-after:ae2@[1.1.0,1.2.0);after:ponder-legacy@[1.4.0-cleanroom-alpha.1,)")
public final class AE2SPonder {
    /** Loader identity; resource and saved registry namespaces remain unchanged. */
    public static final String LEGACY_MOD_ID = "ae2s-ponder-legacy";
    public static final String MOD_ID = "ae2s_ponder";

    @Mod.EventHandler
    public void init(FMLInitializationEvent event) {
        if (event.getSide().isClient() && Loader.isModLoaded("ponder-legacy")) {
            FMLInterModComms.sendMessage("ponder-legacy", "register_ponder_plugin",
                "dev.yudream.ae2sponder.compat.PonderAE2SPlugin");
        }
    }
}
