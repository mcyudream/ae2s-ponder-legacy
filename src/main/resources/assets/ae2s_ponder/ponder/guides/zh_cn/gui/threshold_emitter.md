---
id: ae2s_ponder:gui/threshold_emitter
title: "阈值发信器"
item_ids: [ae2:threshold_level_emitter]
structure: ae2s_ponder:gui/threshold_emitter
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 阈值发信器

## 找到设备

打开对应 AE2S 设备或相关子页面。结构展示其网络上下文，使用 GUI 演示查看控件与操作。

## 界面操作

跟随演示中的光标、高亮控件与资源条目。回放使用独立数据。

<GuiTutorial id="ae2s_ponder:threshold_emitter" duration={324} side="right" />

## 实机跟随

在真实设备中，离开输入框后长按 W 进入引导。原生操作仍由你执行，引导观察控件，不会代发机器操作。

## 核对结果

检查真实库存、所选设置与目标去向。扩大规模前，先测试一次传输或一批加工。

<GuideOnly>

### 监控资源

选择要统计的资源，幽灵条目是过滤标记，不是实物库存。

### 阈值

配置上下阈值，分别测试两个边界，避免被控制机器频繁启停。

### 下阈值

将下阈值设置为小于上阈值，再测试补货和消耗过程。

### 发信条件

选择正确的发信模式并测试接收设备；发信器只提供红石信号，不会自行搬运或合成资源。

</GuideOnly>
