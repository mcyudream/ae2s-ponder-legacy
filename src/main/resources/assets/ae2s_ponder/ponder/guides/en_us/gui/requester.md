---
id: ae2s_ponder:gui/requester
title: "Requester: maintain crafted stock"
item_ids: [ae2:requester]
structure: ae2s_ponder:gui/requester
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Requester: maintain crafted stock

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:requester" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Requested resources

Add the resource and amount that should be maintained. Distinguish the requested target from items already in storage.

### Review all requests

Scroll through the request list and check for duplicates or unnecessarily large targets.

### Requested resources

The requesting network still needs the recipe, ingredients and a free crafting CPU. A requester cannot supply a missing recipe.

### Requested resources

Start with a small target and inspect actual crafting status before enabling many standing requests.

</GuideOnly>
