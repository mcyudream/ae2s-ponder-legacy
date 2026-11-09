---
id: ae2s_ponder:storage_bus
title: "Using External Inventories"
item_ids: [ae2:storage_bus, ae2:interface]
scene: ae2s_ponder:storage_bus
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Using External Inventories

## 1

Place a Storage Bus on the cable face touching an inventory. Here it connects a chest to the ME network.

<GameScene scene="ae2s_ponder:storage_bus" tick={45} />

## 2

The terminal can access the chest's contents through the bus. Items stay in the chest until inserted or extracted; the bus does not copy them into a cell.

<GameScene scene="ae2s_ponder:storage_bus" tick={215} />

<GuiTutorial id="ae2s_ponder:storage_bus" />

## 3

Set a higher storage priority if new matching items should go into this inventory before lower-priority storage.

<GameScene scene="ae2s_ponder:storage_bus" tick={818} />

## 4

Configure the bus filter and access mode. Check the chest has room and the selected mode allows the operation you want.

<GameScene scene="ae2s_ponder:storage_bus" tick={988} />

## 5

Avoid exposing the same inventory back into the same network through multiple storage paths. Interfaces and Storage Buses have different roles.

<GameScene scene="ae2s_ponder:storage_bus" tick={1158} />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
