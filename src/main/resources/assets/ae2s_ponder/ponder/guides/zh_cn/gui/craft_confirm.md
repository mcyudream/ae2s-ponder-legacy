---
id: ae2s_ponder:gui/craft_confirm
title: "发起合成：计划确认"
item_ids: [ae2:crafting_terminal]
structure: ae2s_ponder:gui/craft_confirm
tags: [ae2s_ponder:crafting]
categories: [自动合成]
presentation: both
step_ticks: 180
---
# 发起合成：计划确认

## 找到设备

打开对应 AE2S 设备或相关子页面。结构展示其网络上下文，使用 GUI 演示查看控件与操作。

## 界面操作

跟随演示中的光标、高亮控件与资源条目。回放使用独立数据。

<GuiTutorial id="ae2s_ponder:craft_confirm" duration={324} side="right" />

## 实机跟随

在真实设备中，离开输入框后长按 W 进入引导。原生操作仍由你执行，引导观察控件，不会代发机器操作。

## 核对结果

检查真实库存、所选设置与目标去向。扩大规模前，先测试一次传输或一批加工。

<GuideOnly>

### 检查材料

搜索计划，核对已有、可合成与缺失资源，缺料可能导致任务无法启动。

### 选择 CPU

为计划选择空闲且存储容量足够的 CPU，忙碌或容量不足的 CPU 不能作为有效目标。

### 依赖树

打开合成树，跟踪嵌套依赖并定位缺料分支。

### 确认后启动

核对计划与目标 CPU 后再启动，实机引导只观察按钮，不会替你发起任务。

</GuideOnly>
