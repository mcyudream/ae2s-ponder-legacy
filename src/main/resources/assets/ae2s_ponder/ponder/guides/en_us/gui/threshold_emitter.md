---
id: ae2s_ponder:gui/threshold_emitter
title: "Threshold Level Emitter"
item_ids: [ae2:threshold_level_emitter]
structure: ae2s_ponder:gui/threshold_emitter
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Threshold Level Emitter

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:threshold_emitter" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Observed resource

Choose the resource to count; the ghost entry is a filter, not stored inventory.

### Threshold

Configure the upper and lower thresholds. Test both boundaries so the controlled machine does not rapidly oscillate.

### Lower threshold

Set a lower threshold below the upper threshold, then test replenishment and consumption.

### Signal condition

Choose the intended signal mode and test the receiving device. The emitter supplies a redstone signal; it does not move or craft resources.

</GuideOnly>
