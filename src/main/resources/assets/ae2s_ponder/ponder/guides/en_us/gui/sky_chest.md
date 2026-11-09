---
id: ae2s_ponder:gui/sky_chest
title: "Sky Stone Chest"
item_ids: [ae2:sky_stone_chest, ae2:smooth_sky_stone_chest]
structure: ae2s_ponder:gui/sky_chest
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Sky Stone Chest

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:sky_chest" duration={320} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Chest inventory

These are real chest slots. Place and retrieve items here; this chest does not require an ME network.

### Transfer items

Move items between the chest and your inventory. Demonstration items are independent of the real inventory.

### Chest inventory

Attach a Storage Bus to expose this inventory to ME storage. Configure access and priority on the bus itself.

</GuideOnly>
