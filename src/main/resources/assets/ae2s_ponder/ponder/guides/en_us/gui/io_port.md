---
id: ae2s_ponder:gui/io_port
title: "ME IO Port: transfer cells"
item_ids: [ae2:io_port]
structure: ae2s_ponder:gui/io_port
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# ME IO Port: transfer cells

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:io_port" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Input cells

Insert storage cells to be processed. Their contents, not ordinary loose items, are transferred by this machine.

### Transfer direction

Choose cell-to-network or network-to-cell before starting. Check that the destination accepts the stored resource types.

### Completed cells

Completed cells move to the output side. The selected completion rule decides when a cell counts as finished.

### Throughput and stalls

Use supported upgrades after testing one cell. A full network, restrictive partition or wrong direction can stop transfers.

</GuideOnly>
