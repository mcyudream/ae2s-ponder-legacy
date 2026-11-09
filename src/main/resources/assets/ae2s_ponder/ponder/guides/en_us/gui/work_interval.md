---
id: ae2s_ponder:gui/work_interval
title: "Machine work interval"
item_ids: [ae2:advanced_io_bus, ae2:import_export_bus, ae2:stock_export_bus]
structure: ae2s_ponder:gui/work_interval
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Machine work interval

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:work_interval" duration={320} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Work interval

Set the interval using the displayed unit. A shorter interval increases checking frequency rather than creating ingredients or destination space.

### Measure the result

Test the actual throughput and server workload before applying a very short interval to many devices.

</GuideOnly>
