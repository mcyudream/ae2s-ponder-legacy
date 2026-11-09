---
id: ae2s_ponder:gui/network_status
title: "网络状态：电力与频道"
item_ids: [ae2:controller, ae2:network_tool]
structure: ae2s_ponder:gui/network_status
tags: [ae2s_ponder:networks]
categories: [网络工程]
presentation: both
step_ticks: 180
---
# 网络状态：电力与频道

## 找到设备

打开对应 AE2S 设备或相关子页面。结构展示其网络上下文，使用 GUI 演示查看控件与操作。

## 界面操作

跟随演示中的光标、高亮控件与资源条目。回放使用独立数据。

<GuiTutorial id="ae2s_ponder:network_status" duration={324} side="right" />

## 实机跟随

在真实设备中，离开输入框后长按 W 进入引导。原生操作仍由你执行，引导观察控件，不会代发机器操作。

## 核对结果

检查真实库存、所选设置与目标去向。扩大规模前，先测试一次传输或一批加工。

<GuideOnly>

### 已存能量

比较当前能量与容量，有电不代表发电量能长期跟上需求。

### 能量需求

比较输入、消耗及频道相关耗电，判断是否存在供电缺口。

### 连接设备

滚动查看设备概况，确认目标机器出现在正确网络中。

### 频道检查

机器离线时还应检查线缆容量、控制器拓扑与区块加载，仅有能量并不足够。

</GuideOnly>
