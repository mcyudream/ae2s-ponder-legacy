---
id: ae2s_ponder:gui/crafting_tree
title: "Crafting dependency tree"
item_ids: [ae2:crafting_terminal]
structure: ae2s_ponder:gui/crafting_tree
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Crafting dependency tree

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:crafting_tree" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Recipe branches

Follow the tree from the requested product down to its ingredients and intermediate crafts.

### Missing branches

Use the missing-only filter to focus on the resources or dependencies blocking the plan.

### Export the view

The native screenshot button exports the tree view. This guide never activates file export on your behalf.

### Return to the plan

Return to the parent branch or crafting plan after diagnosing the missing dependency.

</GuideOnly>
