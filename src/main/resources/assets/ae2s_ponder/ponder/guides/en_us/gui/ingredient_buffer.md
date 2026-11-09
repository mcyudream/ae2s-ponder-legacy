---
id: ae2s_ponder:gui/ingredient_buffer
title: "Ingredient Buffer"
item_ids: [ae2:ingredient_buffer]
structure: ae2s_ponder:gui/ingredient_buffer
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Ingredient Buffer

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:ingredient_buffer" duration={320} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Ingredient inventory

Use the buffer as an intermediate inventory between delivery and the processing machine.

### Keep batches traceable

Test one batch and verify which adjacent side inserts and extracts. A buffer does not turn an incorrect pattern into a valid recipe.

### Ingredient inventory

Keep product return separate from ingredient delivery so the crafting CPU receives the expected output.

</GuideOnly>
