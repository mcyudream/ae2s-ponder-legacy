---
id: ae2s_ponder:gui/crafting_cpu
title: "Crafting CPU: running job"
item_ids: [ae2:1k_crafting_storage, ae2:crafting_monitor, ae2:crafting_terminal]
structure: ae2s_ponder:gui/crafting_cpu
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Crafting CPU: running job

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:crafting_cpu" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Follow a product

Search the active job to find the resource currently required or being crafted.

### Read task progress

Distinguish stored ingredients, active crafts and expected returned outputs. A processing job can wait for an exact product.

### Pause a task

Inspect the suspend control and its current state before pausing production. Pausing does not undo items already delivered to machines.

### Cancel a task

Cancel only when intended. Inspect machines and intermediate items before submitting a replacement job.

</GuideOnly>
