---
id: ae2s_ponder:first_network
title: "搭建第一个 ME 网络"
item_ids: [ae2:vibration_chamber, ae2:energy_acceptor, ae2:energy_cell, ae2:drive, ae2:terminal, ae2:crafting_terminal]
scene: ae2s_ponder:first_network
tags: [ae2s_ponder:basics]
categories: [基础入门]
presentation: both
step_ticks: 180
---
# 搭建第一个 ME 网络

## 1

将振动仓接入网络并放入燃料。能量元件用于储能，本身不会发电。

<GameScene scene="ae2s_ponder:first_network" tick={45} />

## 2

也可以通过能量接收器接入外部电源。规模较小的网络只需供电，并不一定需要 ME 控制器。

<GameScene scene="ae2s_ponder:first_network" tick={215} />

## 3

用福鲁伊克斯线缆连接 ME 驱动器，再放入物品存储元件。空的驱动器不能存储物品。

<GameScene scene="ae2s_ponder:first_network" tick={385} />

## 4

在线缆表面安装 ME 终端。打开终端，即可存入、搜索并取出网络中存储的物品。

<GameScene scene="ae2s_ponder:first_network" tick={587} />

## 5

终端离线时，依次检查供电、线缆连接与剩余频道。演示中的物品移动用于说明传输路径。

<GameScene scene="ae2s_ponder:first_network" tick={757} />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
