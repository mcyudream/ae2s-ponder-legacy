---
id: ae2s_ponder:import_export
title: "Importing and Exporting Items"
item_ids: [ae2:import_bus, ae2:export_bus, ae2:level_emitter]
scene: ae2s_ponder:import_export
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Importing and Exporting Items

## 1

An Import Bus pulls items from the inventory it faces into ME storage. The arrow points from the source chest toward the network.

<GameScene scene="ae2s_ponder:import_export" tick={77} />

<GuiTutorial id="ae2s_ponder:import_bus" />

## 2

An Export Bus pushes selected items from ME storage into its target. Open it and add a filter item first.

<GameScene scene="ae2s_ponder:import_export" tick={648} />

<GuiTutorial id="ae2s_ponder:export_bus" />

## 3

The export arrow points from the network into the destination chest. The target must accept the item and have free space.

<GameScene scene="ae2s_ponder:import_export" tick={1251} />

## 4

Imports need available ME storage. Both buses need power and channels. A Storage Bus exposes an inventory instead of continuously moving all its items.

<GameScene scene="ae2s_ponder:import_export" tick={1421} />

## 5

An unregulated Export Bus keeps exporting while space is available. Use redstone control and an appropriate upgrade to control transfers; test with a small batch.

<GameScene scene="ae2s_ponder:import_export" tick={1591} />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
