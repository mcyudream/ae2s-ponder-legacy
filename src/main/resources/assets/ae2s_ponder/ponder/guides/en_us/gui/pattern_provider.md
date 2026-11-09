---
id: ae2s_ponder:gui/pattern_provider
title: "Pattern Provider: install and return"
item_ids: [ae2:pattern_provider, ae2:cable_pattern_provider]
structure: ae2s_ponder:gui/pattern_provider
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Pattern Provider: install and return

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:pattern_provider" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Encoded patterns

Insert a matching encoded pattern. A crafting pattern uses a Molecular Assembler; a processing pattern delivers ingredients to the adjacent machine.

### Return buffer

The return buffer receives products for the network. A separate Import Bus can also return products to the same network.

### Priority

Set priority only when several providers offer the recipe. Check target orientation and blocking mode before increasing parallel work.

### Return buffer

Request one batch and confirm the exact product returns. The task waits until the requesting network receives it.

</GuideOnly>
