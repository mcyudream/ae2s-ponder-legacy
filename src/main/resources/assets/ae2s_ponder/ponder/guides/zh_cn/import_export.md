---
id: ae2s_ponder:import_export
title: "物品输入与输出"
item_ids: [ae2:import_bus, ae2:export_bus, ae2:level_emitter]
scene: ae2s_ponder:import_export
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 物品输入与输出

## 1

输入总线从它朝向的容器提取物品，送入 ME 存储。箭头从来源箱子指向网络。

<GameScene scene="ae2s_ponder:import_export" tick={77} />

<GuiTutorial id="ae2s_ponder:import_bus" />

## 2

输出总线把网络中指定的物品送入目标容器。先打开它，添加需要输出的过滤物品。

<GameScene scene="ae2s_ponder:import_export" tick={648} />

<GuiTutorial id="ae2s_ponder:export_bus" />

## 3

输出方向是从网络到目标箱子。目标必须允许接收该物品，而且要有剩余空间。

<GameScene scene="ae2s_ponder:import_export" tick={1251} />

## 4

输入物品需要网络有可用存储。两个总线都需要能量与频道；存储总线则是开放容器访问，不会持续搬空容器。

<GameScene scene="ae2s_ponder:import_export" tick={1421} />

## 5

未加控制的输出总线会在有空间时持续输出。可配合红石控制及相应升级控制传输，先用少量物品验证。

<GameScene scene="ae2s_ponder:import_export" tick={1591} />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
