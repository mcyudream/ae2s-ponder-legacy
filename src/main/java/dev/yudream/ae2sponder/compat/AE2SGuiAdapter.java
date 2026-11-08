package dev.yudream.ae2sponder.compat;

import ae2.client.gui.AEBaseGui;
import ae2.client.gui.me.common.RepoSlot;
import ae2.client.gui.me.patternencode.GuiPatternEncodingTerm;
import ae2.client.gui.widgets.ITextFieldGui;
import ae2.container.SlotSemantics;
import ae2.container.implementations.ContainerCellWorkbench;
import ae2.container.implementations.ContainerInscriber;
import ae2.container.me.patternencode.ContainerPatternEncodingTerm;
import ae2.parts.encoding.EncodingMode;
import java.util.List;
import net.createmod.ponder.api.gui.GuiTutorial;
import net.createmod.ponder.api.gui.GuiTutorial.Rect;
import net.createmod.ponder.api.gui.GuiTutorial.Stack;
import net.createmod.ponder.api.gui.GuiTutorialAdapter;
import net.createmod.ponder.client.guitutorial.StandardGuiAdapter;
import net.minecraft.client.gui.GuiScreen;
import net.minecraft.client.gui.GuiTextField;
import net.minecraft.inventory.Slot;

/** AE2S 1.1.0 semantic slots and widgets. All reads stay on the client; no container actions are sent. */
public final class AE2SGuiAdapter implements GuiTutorialAdapter {
    private final StandardGuiAdapter generic = new StandardGuiAdapter();

    @Override public boolean matches(GuiScreen screen, GuiTutorial tutorial) {
        if (!(screen instanceof AEBaseGui<?>) || !generic.matches(screen, tutorial)) return false;
        if (screen instanceof GuiPatternEncodingTerm gui) {
            if (tutorial.id().getPath().equals("pattern_crafting")) return gui.getContainer().getMode() == EncodingMode.CRAFTING;
            if (tutorial.id().getPath().equals("pattern_processing")) return gui.getContainer().getMode() == EncodingMode.PROCESSING;
        }
        // Specialized pattern tutorials have their own selection in W guidance.
        return !tutorial.id().getPath().equals("terminal") || !(screen instanceof GuiPatternEncodingTerm);
    }

    @Override public Rect window(GuiScreen screen, GuiTutorial tutorial) {
        if (screen instanceof AEBaseGui<?> gui) {
            var r = new java.awt.Rectangle(gui.getBounds(true));
            for (var zone : gui.getExclusionZones()) r.add(zone);
            return new Rect(r.x, r.y, r.width, r.height);
        }
        return generic.window(screen, tutorial);
    }

    private Slot nativeSlot(AEBaseGui<?> gui, String key) {
        if (key.startsWith("repo.")) {
            int index = index(key.substring(5));
            return gui.getContainer().inventorySlots.stream()
                .filter(s -> s instanceof RepoSlot repo && repo.getRepoViewIndex() == index)
                .findFirst().orElse(null);
        }
        if (!key.startsWith("slot.")) return null;
        int dot = key.lastIndexOf('.');
        if (dot <= 5) return null;
        var semantic = SlotSemantics.get(key.substring(5, dot));
        if (semantic == null) return null;
        List<Slot> slots = gui.getContainer().getSlots(semantic);
        int index = index(key.substring(dot + 1));
        return index >= 0 && index < slots.size() ? slots.get(index) : null;
    }

    private static int index(String value) {
        try { return Integer.parseInt(value); }
        catch (NumberFormatException ignored) { return -1; }
    }

    @Override public Rect target(GuiScreen screen, GuiTutorial tutorial, String key) {
        if (!(screen instanceof AEBaseGui<?> gui)) return null;
        if (key.startsWith("slot.") || key.startsWith("repo.")) {
            Slot slot = nativeSlot(gui, key);
            return slot != null && slot.isEnabled()
                ? new Rect(gui.getGuiLeft() + slot.xPos, gui.getGuiTop() + slot.yPos, 16, 16) : null;
        }
        if (key.startsWith("widget.")) {
            String id = key.substring(7);
            var text = gui.getWidgets().getTextField(id);
            if (text != null) {
                if (!text.getVisible()) return null;
                var r = text.getTooltipArea();
                return new Rect(r.x, r.y, r.width, r.height);
            }
            var button = gui.getWidgets().get(id);
            return button != null && button.visible ? new Rect(button.x, button.y, button.width, button.height) : null;
        }
        return generic.target(screen, tutorial, key);
    }

    @Override public boolean enabled(GuiScreen screen, GuiTutorial tutorial, String key) {
        if (screen instanceof AEBaseGui<?> gui && key.startsWith("widget.")) {
            var button = gui.getWidgets().get(key.substring(7));
            return button != null ? button.visible && button.enabled : target(screen, tutorial, key) != null;
        }
        return target(screen, tutorial, key) != null;
    }

    @Override public Stack slot(GuiScreen screen, GuiTutorial tutorial, String key) {
        if (!(screen instanceof AEBaseGui<?> gui)) return null;
        Slot slot = nativeSlot(gui, key);
        if (slot == null || !slot.isEnabled()) return null;
        var stack = slot.getStack();
        if (stack.isEmpty()) return Stack.EMPTY;
        int count = slot instanceof RepoSlot repo ? (int) Math.min(Integer.MAX_VALUE, repo.getStoredAmount()) : stack.getCount();
        return new Stack(stack.getItem().getRegistryName().toString(), count);
    }

    @Override public String value(GuiScreen screen, String key) {
        if (!(screen instanceof AEBaseGui<?> gui)) return "";
        if (key.startsWith("widget.")) {
            var text = gui.getWidgets().getTextField(key.substring(7));
            return text != null ? text.getText() : "";
        }
        if (gui.getContainer() instanceof ContainerInscriber container) {
            return switch (key) {
                case "inscriber.progress" -> Integer.toString(container.getCurrentProgress());
                case "inscriber.max_progress" -> Integer.toString(container.getMaxProgress());
                case "inscriber.work_observed" -> container.getCurrentProgress()>0
                    || container.getSlots(SlotSemantics.MACHINE_OUTPUT).stream().anyMatch(Slot::getHasStack) ? "1" : "0";
                default -> "";
            };
        }
        if (gui.getContainer() instanceof ContainerPatternEncodingTerm container && key.equals("pattern.mode"))
            return container.getMode().name();
        if (gui.getContainer() instanceof ContainerCellWorkbench container && key.equals("workbench.page"))
            return Integer.toString(container.getCurrentPage());
        return "";
    }

    @Override public boolean textFocused(GuiScreen screen) {
        if (screen instanceof AEBaseGui<?> gui && gui.getWidgets().getTextFields().stream().anyMatch(GuiTextField::isFocused)) return true;
        if (screen instanceof ITextFieldGui gui && gui.getTextFields().stream().anyMatch(GuiTextField::isFocused)) return true;
        return generic.textFocused(screen);
    }
}
