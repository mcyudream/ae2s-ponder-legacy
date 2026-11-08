package dev.yudream.ae2sponder;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.versioning.ArtifactVersion;
import net.minecraftforge.fml.common.versioning.DefaultArtifactVersion;
import net.minecraftforge.fml.common.versioning.VersionParser;
import org.junit.Test;

/** Use the loader's version ordering, including its handling of unknown qualifiers. */
public class PonderDependencyTest {
    private static String declaration() {
        return Arrays.stream(AE2SPonder.class.getAnnotation(Mod.class).dependencies().split(";"))
            .filter(value -> value.contains(":ponder-legacy@"))
            .findFirst().orElseThrow();
    }

    private static boolean accepts(String version) {
        ArtifactVersion requirement = VersionParser.parseVersionReference(declaration().split(":", 2)[1]);
        return requirement.containsVersion(new DefaultArtifactVersion("ponder-legacy", version));
    }

    @Test public void acceptsPublishedStablePonder() {
        assertTrue("Ponder Legacy 1.7.0 must load", accepts("1.7.0"));
    }

    @Test public void acceptsNewerPresentationCompatiblePonder() {
        assertTrue(accepts("1.7.1"));
    }

    @Test public void rejectsVersionsBeforeTheSupportedApi() {
        assertFalse(accepts("1.3.9"));
        assertFalse(accepts("1.4.1"));
        assertFalse(accepts("1.6.2"));
    }

    @Test public void ponderRemainsOptional() {
        assertTrue("Use an optional ordering dependency", declaration().startsWith("after:"));
    }
}
