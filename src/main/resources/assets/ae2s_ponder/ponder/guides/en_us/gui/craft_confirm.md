---
id: ae2s_ponder:gui/craft_confirm
title: "Request crafting: plan"
item_ids: [ae2:crafting_terminal]
structure: ae2s_ponder:gui/craft_confirm
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Request crafting: plan

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:craft_confirm" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Inspect materials

Search the plan and inspect stored, craftable and missing resources. Missing items can prevent the task from starting.

### Choose a CPU

Choose an available crafting CPU with enough storage for this plan. A busy or undersized CPU is not a valid destination.

### Dependency tree

Open the tree to follow nested crafting dependencies and identify the branch that is missing resources.

### Start deliberately

Start only after reviewing the plan and target CPU. Live guidance observes this button; it does not start the job for you.

</GuideOnly>
