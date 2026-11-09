---
id: ae2s_ponder:gui/cell_restriction
title: "Storage cell restrictions"
item_ids: [ae2:cell_workbench]
structure: ae2s_ponder:gui/cell_restriction
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Storage cell restrictions

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:cell_restriction" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Amount limit

Set the amount limit supported by the selected cell. Check whether you intend a restrictive cap before applying it.

### Type limit

Set the allowed number of resource types without confusing types with stored item count.

### Apply restrictions

Apply only to the intended cell, then inspect the cell tooltip and test one insertion.

### Release restrictions

Use release when you intend to remove the restriction. It does not delete or supply stored resources.

</GuideOnly>
