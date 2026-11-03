package dev.yudream.ae2sponder.dev;

import ae2.tile.storage.TileDrive;
import dev.yudream.ae2sponder.compat.PonderAE2SPlugin;
import java.util.concurrent.CompletableFuture;
import net.createmod.ponder.foundation.structure.PonderStructureLoader;
import net.minecraft.client.Minecraft;
import net.minecraft.util.math.BlockPos;

/** Check actual power and channels: ME drives do not connect through their front. */
final class MachineNetworkVerification {
    private final Minecraft mc = Minecraft.getMinecraft();
    private final BlockPos origin = new BlockPos(12, 5, 12);
    private final String[] diagrams = {"autocrafting", "processing", "channels"};
    private CompletableFuture<Void> pending;
    private int diagram, ticks;
    private boolean placed;

    boolean tick(ClientVerification host) throws Exception {
        if (pending != null) {
            if (!pending.isDone()) return false;
            pending.join(); pending = null;
        }
        if (diagram == diagrams.length) return true;
        if (!placed) {
            var structure = new PonderStructureLoader().load(PonderAE2SPlugin.id(diagrams[diagram]));
            server(() -> P2PNetworkVerification.place(mc, origin, structure));
            placed = true;
            return false;
        }
        if (++ticks < 100) return false;
        String name = diagrams[diagram];
        server(() -> {
            var position = origin.add("channels".equals(name) ? new BlockPos(4, 1, 2) : new BlockPos(1, 1, 3));
            var drive = (TileDrive) mc.getIntegratedServer().getWorld(0).getTileEntity(position);
            host.check(drive.getMainNode().isOnline(),
                "Real " + name + " diagram powers its drive through connected faces and supplies a channel");
        });
        diagram++; ticks = 0; placed = false;
        return false;
    }

    private void server(Runnable action) {
        pending = new CompletableFuture<>();
        mc.getIntegratedServer().addScheduledTask(() -> {
            try { action.run(); pending.complete(null); }
            catch (Throwable failure) { pending.completeExceptionally(failure); }
        });
    }
}
