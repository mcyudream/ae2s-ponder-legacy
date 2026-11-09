---
id: ae2s_ponder:gui/network_status
title: "Network status: power and channels"
item_ids: [ae2:controller, ae2:network_tool]
structure: ae2s_ponder:gui/network_status
tags: [ae2s_ponder:networks]
categories: [Network Engineering]
presentation: both
step_ticks: 180
---
# Network status: power and channels

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:network_status" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Stored energy

Compare current energy with capacity. A nonzero battery does not guarantee generation will keep up with demand.

### Energy demand

Compare input, usage and channel-related energy demand to find a power deficit.

### Connected devices

Scroll the device overview and check that expected machines appear in the correct network.

### Channel checks

When a machine is offline, also check cable capacity, controller topology and loaded chunks; energy alone is not enough.

</GuideOnly>
