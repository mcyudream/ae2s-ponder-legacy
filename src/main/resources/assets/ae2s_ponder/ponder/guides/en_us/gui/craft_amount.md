---
id: ae2s_ponder:gui/craft_amount
title: "Request crafting: amount"
item_ids: [ae2:crafting_terminal, ae2:pattern_encoding_terminal]
structure: ae2s_ponder:gui/craft_amount
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Request crafting: amount

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:craft_amount" duration={320} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Requested amount

Enter the desired amount and check the displayed unit. This is a request, not a promise that the network has sufficient materials.

### Calculate the plan

Continue to calculate the recipe plan. Read the material and CPU checks before starting a large task.

### Quantity shortcuts

Configure number-entry increments if needed. Modified-key shortcuts must not be confused with the actual requested amount.

</GuideOnly>
