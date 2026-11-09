---
id: ae2s_ponder:storage_bus
title: "接入外部容器"
item_ids: [ae2:storage_bus, ae2:interface]
scene: ae2s_ponder:storage_bus
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 接入外部容器

## 1

在线缆朝向容器的一面安装存储总线。这里用它把箱子接入 ME 网络。

<GameScene scene="ae2s_ponder:storage_bus" tick={45} />

## 2

终端通过总线访问箱内物品。物品仍保存在箱子中，总线不会把它们自动复制到存储元件。

<GameScene scene="ae2s_ponder:storage_bus" tick={215} />

<GuiTutorial id="ae2s_ponder:storage_bus" />

## 3

如果希望新存入的匹配物品优先进入这个容器，将它的存储优先级设得高于其他存储设备。

<GameScene scene="ae2s_ponder:storage_bus" tick={818} />

## 4

配置总线的过滤条目与访问模式，同时确认箱子有空间，所选模式允许需要的存入或取出操作。

<GameScene scene="ae2s_ponder:storage_bus" tick={988} />

## 5

避免通过多条存储路径，把同一个容器重复暴露给同一个网络。ME 接口和存储总线的作用也不同。

<GameScene scene="ae2s_ponder:storage_bus" tick={1158} />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
