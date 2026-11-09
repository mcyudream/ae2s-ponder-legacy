---
id: ae2s_ponder:gui/stock_amount
title: "Configure stock amount"
item_ids: [ae2:interface, ae2:stock_export_bus]
structure: ae2s_ponder:gui/stock_amount
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Configure stock amount

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:stock_amount" duration={320} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Target amount

Enter the desired local amount and check its unit and maximum. Zero can have a special clearing or disabling meaning on the parent device.

### Save the target

Save only after confirming the intended resource. The amount is a target, not a supplied inventory stack.

### Return to the device

Inspect the parent configuration and test actual replenishment after changing a target.

</GuideOnly>
