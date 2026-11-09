package dev.yudream.ae2sponder.dev;

import ae2.client.gui.AEBaseGui;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import java.awt.Rectangle;
import java.nio.file.Files;
import net.createmod.ponder.api.gui.GuiTutorial;
import net.createmod.ponder.client.guitutorial.GuiTutorials;
import net.minecraft.client.Minecraft;

/** Records actual native geometry and checks overlay translation against the native primitives. */
final class NativeGuiGeometryVerification {
    static void verify(ClientVerification host,String id,AEBaseGui<?> gui,GuiTutorial tutorial)throws Exception {
        var result=new JsonObject();var frame=gui.getBounds(true);
        result.addProperty("screen",gui.getClass().getName());result.addProperty("width",frame.width);result.addProperty("height",frame.height);
        var widgets=new JsonObject();var adapter=GuiTutorials.adapter(tutorial);
        for(String key:new dev.yudream.ae2sponder.compat.AE2SGuiCatalog().get(id).widgets()) {
            Rectangle absolute=null;String kind="";
            var field=gui.getWidgets().getTextField(key);var button=gui.getWidgets().get(key);var composite=gui.getWidgets().getComposite(key);
            if(field!=null&&field.getVisible()){absolute=field.getTooltipArea();kind="field";}
            else if(button!=null&&button.visible){absolute=new Rectangle(button.x,button.y,button.width,button.height);kind=button.getClass().getSimpleName();}
            else if(composite!=null&&composite.isVisible()){
                var r=composite.getBounds();if(r.width>0&&r.height>0)absolute=new Rectangle(frame.x+r.x,frame.y+r.y,r.width,r.height);kind=composite.getClass().getSimpleName();
            }
            if(absolute==null||absolute.width<=0||absolute.height<=0)continue;
            var overlay=adapter.target(gui,tutorial,"widget."+key);
            host.check(overlay!=null&&overlay.x()==absolute.x&&overlay.y()==absolute.y&&overlay.width()==absolute.width&&overlay.height()==absolute.height,
                id+": live highlight follows native "+kind+" geometry: "+key);
            var entry=new JsonObject();entry.addProperty("kind",kind);var r=new JsonArray();r.add(absolute.x-frame.x);r.add(absolute.y-frame.y);r.add(absolute.width);r.add(absolute.height);entry.add("bounds",r);widgets.add(key,entry);
        }
        result.add("widgets",widgets);
        var output=Minecraft.getMinecraft().gameDir.toPath().resolve("ae2s-ponder-smoke/native-geometry");Files.createDirectories(output);
        Files.writeString(output.resolve(id+".json"),new GsonBuilder().setPrettyPrinting().create().toJson(result)+"\n");
    }
}
