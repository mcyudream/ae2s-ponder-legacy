---
id: ae2s_ponder:channels
title: "Channels and Cable Capacity"
item_ids: [ae2:controller, ae2:fluix_glass_cable, ae2:fluix_smart_cable, ae2:fluix_smart_dense_cable, ae2:quartz_fiber]
scene: ae2s_ponder:channels
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Channels and Cable Capacity

## 1

With normal channel settings, a controllerless network supports up to 8 channels. Add an ME Controller when you need more devices.

<GameScene scene="ae2s_ponder:channels" tick={45} />

<GuiTutorial id="ae2s_ponder:network_status" />

## 2

Ordinary glass, covered and smart cables carry up to 8 channels. Smart cable markings show channel use; they do not increase capacity.

<GameScene scene="ae2s_ponder:channels" tick={616} />

## 3

Dense cable carries up to 32 channels per connection. Branch into ordinary cable near devices; an 8-channel bottleneck still limits that branch.

<GameScene scene="ae2s_ponder:channels" tick={786} />

## 4

Different cable colors do not connect directly. Fluix cable connects to any color. Plan branches to prevent unwanted network connections.

<GameScene scene="ae2s_ponder:channels" tick={956} />

## 5

Quartz Fiber shares power between networks without passing channels or stored items. Channel limits in these examples assume normal settings; packs can change them.

<GameScene scene="ae2s_ponder:channels" tick={1126} />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
