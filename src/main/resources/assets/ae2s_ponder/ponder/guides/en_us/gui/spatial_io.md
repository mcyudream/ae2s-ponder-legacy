---
id: ae2s_ponder:gui/spatial_io
title: "Spatial IO Port: transfer a region"
item_ids: [ae2:spatial_io_port, ae2:spatial_storage_cell_2, ae2:spatial_storage_cell_16, ae2:spatial_storage_cell_128]
structure: ae2s_ponder:gui/spatial_io
tags: [ae2s_ponder:networks]
categories: [Network Engineering]
presentation: both
step_ticks: 180
---
# Spatial IO Port: transfer a region

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:spatial_io" duration={324} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Spatial cell

Insert a Spatial Storage Cell large enough for the defined region. It stores a spatial region rather than ordinary item stacks.

### Defined region

Verify the displayed spatial dimensions against the Spatial Pylon setup before operating the port.

### Energy and efficiency

Read required energy, available energy and efficiency. The network must have enough stored energy for the transfer.

### Complete and recover

Trigger the port using the intended control and collect the resulting cell. Test with a small nonvaluable region first.

</GuideOnly>
