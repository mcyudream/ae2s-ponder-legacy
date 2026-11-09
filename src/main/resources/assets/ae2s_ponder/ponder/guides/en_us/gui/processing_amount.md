---
id: ae2s_ponder:gui/processing_amount
title: "Processing pattern amounts"
item_ids: [ae2:pattern_encoding_terminal, ae2:processing_pattern]
structure: ae2s_ponder:gui/processing_amount
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Processing pattern amounts

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:processing_amount" duration={320} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Exact resource amount

Set the amount for this processing entry and check the resource unit. Large fluid amounts are not equivalent to the same number of item stacks.

### Check the full recipe

Return and compare all input and output amounts before encoding. The requesting network waits for the exact declared product.

</GuideOnly>
