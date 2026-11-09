---
id: ae2s_ponder:gui/export_bus
title: "Export Bus"
item_ids: [ae2:export_bus]
structure: ae2s_ponder:gui/export_bus
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Export Bus

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:export_bus" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Resource filter

Select items to send from ME storage into the adjacent inventory. An empty filter does not specify a desired item.

### Operation settings

Read the supported redstone, matching, scheduling and access settings. Availability depends on this bus and installed cards.

### Upgrade cards

Install only compatible cards. Extra filter slots can remain disabled until the required capacity upgrade is present.

### Resource filter

Use a small amount to confirm direction, free destination space and network power. Avoid a direct import/export loop on the same inventory.

</GuideOnly>
