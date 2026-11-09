package dev.yudream.ae2sponder.compat;

import ae2.client.gui.AEBaseGui;
import ae2.client.gui.style.Text;
import ae2.client.gui.style.TextAlignment;
import java.awt.Rectangle;
import java.lang.reflect.Field;
import java.util.List;
import java.util.Map;
import net.createmod.ponder.api.gui.GuiTutorial.Rect;
import net.minecraft.client.Minecraft;
import net.minecraft.util.text.ITextComponent;

/** AE2S uses private synchronized text overrides. Read their display state without changing it. */
final class AE2SGuiTextGeometry {
    private static final Field OVERRIDES, CONTENT, HIDDEN;
    static {
        try {
            OVERRIDES=AEBaseGui.class.getDeclaredField("textOverrides");OVERRIDES.setAccessible(true);
            Class<?> type=Class.forName("ae2.client.gui.AEBaseGui$TextOverride");
            CONTENT=type.getDeclaredField("content");CONTENT.setAccessible(true);
            HIDDEN=type.getDeclaredField("hidden");HIDDEN.setAccessible(true);
        }catch(ReflectiveOperationException failure){throw new ExceptionInInitializerError(failure);}
    }
    static String content(AEBaseGui<?> gui,String id,Text text) {
        try {
            Object override=((Map<?,?>)OVERRIDES.get(gui)).get(id);
            if(override!=null) {
                if(HIDDEN.getBoolean(override))return null;
                ITextComponent value=(ITextComponent)CONTENT.get(override);
                if(value!=null)return value.getFormattedText();
            }
            return text.getText().getFormattedText();
        }catch(IllegalAccessException failure){throw new IllegalStateException("Cannot read pinned AE2S text display state",failure);}
    }
    static Rect bounds(Text text,Rectangle frame,String value) {
        if(value.isEmpty())return null;
        var font=Minecraft.getMinecraft().fontRenderer;float scale=text.getScale();
        List<String> lines=text.getMaxWidth()>0?font.listFormattedStringToWidth(value,text.getMaxWidth()):List.of(value);
        int width=Math.max(1,Math.round(lines.stream().mapToInt(font::getStringWidth).max().orElse(1)*scale));
        int height=Math.max(1,Math.round(font.FONT_HEIGHT*scale)*lines.size());
        var p=text.getPosition().resolve(frame);
        int x=p.x()-(text.getAlign()==TextAlignment.RIGHT?width:text.getAlign()==TextAlignment.CENTER?width/2:0);
        return new Rect(x,p.y(),width,height);
    }
}
