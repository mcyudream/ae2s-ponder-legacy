package dev.yudream.ae2sponder.dev;

import ae2.core.definitions.AEBlocks;
import ae2.parts.p2p.MEP2PTunnelPart;
import ae2.tile.networking.TileCableBus;
import ae2.tile.networking.TileController;
import ae2.tile.storage.TileDrive;
import dev.yudream.ae2sponder.compat.PonderAE2SPlugin;
import java.util.concurrent.CompletableFuture;
import net.createmod.ponder.foundation.structure.PonderStructure;
import net.createmod.ponder.foundation.structure.PonderStructureLoader;
import net.minecraft.client.Minecraft;
import net.minecraft.init.Blocks;
import net.minecraft.inventory.EntityEquipmentSlot;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.util.EnumFacing;
import net.minecraft.util.EnumHand;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.math.Vec3d;

/** Prove that the illustrated P2P topology works in an actual server world, including Quartz Fiber power. */
final class P2PNetworkVerification {
    private final Minecraft mc = Minecraft.getMinecraft();
    private final BlockPos origin = new BlockPos(12, 5, 12);
    private CompletableFuture<Void> pending;
    private int phase, settling;

    boolean tick(ClientVerification host) throws Exception {
        if (pending != null) {
            if (!pending.isDone()) return false;
            pending.join(); pending = null;
        }
        if (phase == 0) {
            var structure = new PonderStructureLoader().load(PonderAE2SPlugin.id("p2p"));
            server(() -> place(mc, origin, structure));
            phase++; return false;
        }
        if (phase == 1) {
            if (++settling < 100) return false;
            settling = 0;
            server(() -> {
                var input = tunnel(2, EnumFacing.WEST);
                var output = tunnel(6, EnumFacing.EAST);
                host.check(input.getMainNode().isOnline() && output.getMainNode().isOnline(),
                    "Real P2P carrier powers both tunnels through Quartz Fiber and supplies their channels"
                        + " [input powered=" + input.getMainNode().isPowered() + ", booted=" + input.getMainNode().hasGridBooted()
                        + "; output powered=" + output.getMainNode().isPowered() + ", booted=" + output.getMainNode().hasGridBooted() + "]");
                var player = mc.getIntegratedServer().getPlayerList().getPlayers().get(0);
                var card = new ItemStack(Item.REGISTRY.getObject(PonderAE2SPlugin.ae2("memory_card")));
                player.setItemStackToSlot(EntityEquipmentSlot.MAINHAND, card);
                player.setSneaking(true);
                host.check(input.onUseItemOn(card, player, EnumHand.MAIN_HAND, Vec3d.ZERO),
                    "Actual Memory Card sneak interaction saves the P2P input");
                player.setSneaking(false);
                host.check(output.onUseItemOn(card, player, EnumHand.MAIN_HAND, Vec3d.ZERO),
                    "Actual Memory Card use binds the P2P output");
                host.check(output.isOutput() && output.getFrequency() == input.getFrequency() && output.getFrequency() != 0,
                    "Real P2P tunnel roles and frequencies match the demonstrated sequence");
            });
            phase++; return false;
        }
        if (phase == 2) {
            if (++settling < 100) return false;
            server(() -> {
                var world = mc.getIntegratedServer().getWorld(0);
                var controller = (TileController) world.getTileEntity(origin.add(1, 1, 3));
                var drive = (TileDrive) world.getTileEntity(origin.add(8, 1, 3));
                var input = tunnel(2, EnumFacing.WEST);
                host.check(input.getMainNode().getGrid() != controller.getMainNode().getGrid(),
                    "Quartz Fiber keeps the P2P carrier separate from the source controller network");
                host.check(drive.getMainNode().isOnline() && drive.getMainNode().getGrid() == controller.getMainNode().getGrid(),
                    "P2P output connects the illustrated remote drive to the source ME network");
            });
            phase++; return false;
        }
        return true;
    }

    private MEP2PTunnelPart tunnel(int x, EnumFacing side) {
        var world = mc.getIntegratedServer().getWorld(0);
        return (MEP2PTunnelPart) ((TileCableBus) world.getTileEntity(origin.add(x, 1, 3))).getPart(side);
    }

    private void server(Runnable action) {
        pending = new CompletableFuture<>();
        mc.getIntegratedServer().addScheduledTask(() -> {
            try { action.run(); pending.complete(null); }
            catch (Throwable failure) { pending.completeExceptionally(failure); }
        });
    }

    static void place(Minecraft mc, BlockPos origin, PonderStructure structure) {
        var world = mc.getIntegratedServer().getWorld(0);
        var player = mc.getIntegratedServer().getPlayerList().getPlayers().get(0);
        player.connection.setPlayerLocation(origin.getX() + 4, origin.getY() + 5, origin.getZ() + 7, 180, 15);
        for (BlockPos pos : BlockPos.getAllInBox(origin, origin.add(8, 4, 8))) world.setBlockToAir(pos);
        for (var block : structure.getBlocks())
            world.setBlockState(origin.add(block.getPosition()), block.getState(), 3);
        for (var block : structure.getBlocks()) {
            var nbt = block.getTileData();
            if (nbt == null) continue;
            BlockPos pos = origin.add(block.getPosition());
            nbt.setInteger("x", pos.getX()); nbt.setInteger("y", pos.getY()); nbt.setInteger("z", pos.getZ());
            world.getTileEntity(pos).readFromNBT(nbt);
        }
        // A deterministic external power source for verification, replacing the diagram's charged energy cell.
        world.setBlockState(origin.add(1, 1, 2), AEBlocks.CREATIVE_ENERGY_CELL.block().getDefaultState(), 3);
    }
}
