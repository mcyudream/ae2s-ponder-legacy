---
id: ae2s_ponder:gui/pattern_processing
title: "Pattern Terminal: processing"
item_ids: [ae2:pattern_encoding_terminal, ae2:processing_pattern, ae2:blank_pattern]
structure: ae2s_ponder:gui/pattern_processing
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Pattern Terminal: processing

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:pattern_processing" duration={400} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Processing mode

Choose Processing for an external machine recipe.

### Blank pattern

Insert a blank pattern. The guide observes this real slot and never places an item for you.

### Consumed material

Specify exactly the consumed inputs and expected outputs. Keep reusable presses installed in the machine; do not list them as consumed ingredients.

### Encode

Click Encode after checking mode, ingredients and output. Encoding still requires a valid recipe and a blank pattern.

### Encoded pattern

Take the encoded pattern and install it in a Pattern Provider. Processing outputs must return to the same requesting network.

</GuideOnly>
