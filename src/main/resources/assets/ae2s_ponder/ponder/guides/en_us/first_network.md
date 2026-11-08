---
id: ae2s_ponder:first_network
title: "Your First ME Network"
item_ids: [ae2:vibration_chamber, ae2:energy_acceptor, ae2:energy_cell, ae2:drive, ae2:terminal, ae2:crafting_terminal]
scene: ae2s_ponder:first_network
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Your First ME Network

## 1

Connect a Vibration Chamber to the network and add fuel. An Energy Cell stores energy; it does not generate power.

<GameScene scene="ae2s_ponder:first_network" tick={45} />

## 2

Alternatively, connect an external power source through an Energy Acceptor. A powered small network can work without an ME Controller.

<GameScene scene="ae2s_ponder:first_network" tick={215} />

## 3

Connect an ME Drive with Fluix Cable and insert an item storage cell. An empty drive provides no storage.

<GameScene scene="ae2s_ponder:first_network" tick={385} />

<GuiTutorial id="ae2s_ponder:drive" />

## 4

Place an ME Terminal on a cable face. Open it to insert, find and withdraw items stored on the network.

<GameScene scene="ae2s_ponder:first_network" tick={988} />

<GuiTutorial id="ae2s_ponder:terminal" />

## 5

If the terminal is offline, check power, cable connections and available channels. Item movement here is a schematic animation.

<GameScene scene="ae2s_ponder:first_network" tick={1559} />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
