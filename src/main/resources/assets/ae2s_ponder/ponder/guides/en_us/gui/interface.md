---
id: ae2s_ponder:gui/interface
title: "ME Interface: stock and insert"
item_ids: [ae2:interface, ae2:cable_interface]
structure: ae2s_ponder:gui/interface
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# ME Interface: stock and insert

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:interface" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Requested stock

Configure the desired item and amount in a ghost slot. This entry requests stock; it is not an already supplied item.

### Local inventory

With network power, a channel and enough stored items, the interface replenishes its real local inventory.

### Local inventory

Let the adjacent machine consume from the real inventory. Avoid routing those same items straight back into the interface.

### Local inventory

An interface can accept machine output into network storage. Use a Pattern Provider for processing-pattern ingredient delivery.

</GuideOnly>
