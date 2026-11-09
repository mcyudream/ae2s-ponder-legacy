---
id: ae2s_ponder:gui/vibration_chamber
title: "Vibration Chamber: generate power"
item_ids: [ae2:vibration_chamber]
structure: ae2s_ponder:gui/vibration_chamber
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Vibration Chamber: generate power

## Find the device

Open the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.

## GUI operation

Follow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.

<GuiTutorial id="ae2s_ponder:vibration_chamber" duration={320} side="right" />

## Follow along in game

On the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.

## Verify the result

Check the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.

<GuideOnly>

### Fuel

Insert a valid furnace fuel. Fuel is consumed to supply AE power to the connected network.

### Generation

Watch generation and demand. An Energy Cell stores surplus energy; it does not generate energy by itself.

### Upgrades and supply

Use only upgrades supported by this machine. Automate fuel supply separately and test that the network stays powered under load.

</GuideOnly>
