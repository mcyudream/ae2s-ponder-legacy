---
id: ae2s_ponder:gui/energy_emitter
title: "Energy Level Emitter"
item_ids: [ae2:energy_level_emitter]
structure: ae2s_ponder:gui/energy_emitter
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Energy Level Emitter

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:energy_emitter" duration={320} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Threshold

Set the network energy threshold using the displayed power unit.

### Signal condition

Choose the intended signal mode and test the receiving device. The emitter supplies a redstone signal; it does not move or craft resources.

</GuideOnly>
