---
id: ae2s_ponder:channels
title: "频道与线缆容量"
item_ids: [ae2:controller, ae2:fluix_glass_cable, ae2:fluix_smart_cable, ae2:fluix_smart_dense_cable, ae2:quartz_fiber]
scene: ae2s_ponder:channels
tags: [ae2s_ponder:basics]
categories: [基础入门]
presentation: both
step_ticks: 180
---
# 频道与线缆容量

## 1

正常频道设置下，无控制器网络最多支持 8 个频道。需要接入更多设备时，添加 ME 控制器。

<GameScene scene="ae2s_ponder:channels" tick={45} />

<GuiTutorial id="ae2s_ponder:network_status" />

## 2

普通玻璃、包覆与智能线缆最多承载 8 个频道。智能线缆的亮线显示使用量，并不会提高容量。

<GameScene scene="ae2s_ponder:channels" tick={616} />

## 3

致密线缆每个连接最多承载 32 个频道，在设备附近再分支为普通线缆。分支中的 8 频道瓶颈仍然有效。

<GameScene scene="ae2s_ponder:channels" tick={786} />

## 4

不同颜色的线缆不会直接连接；福鲁伊克斯线缆可以连接所有颜色。规划分支时要避免网络意外相连。

<GameScene scene="ae2s_ponder:channels" tick={956} />

## 5

石英纤维只在网络之间传递能量，不传递频道与存储内容。本演示的频道数量以正常设置为准，整合包可以调整这些规则。

<GameScene scene="ae2s_ponder:channels" tick={1126} />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
