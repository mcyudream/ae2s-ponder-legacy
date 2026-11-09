---
id: ae2s_ponder:gui/stock_amount
title: "设置备货数量"
item_ids: [ae2:interface, ae2:stock_export_bus]
structure: ae2s_ponder:gui/stock_amount
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 设置备货数量

## 找到设备

打开对应 AE2S 设备或相关子页面。结构展示其网络上下文，使用 GUI 演示查看控件与操作。

## 界面操作

跟随演示中的光标、高亮控件与资源条目。回放使用独立数据。

<GuiTutorial id="ae2s_ponder:stock_amount" duration={320} side="right" />

## 实机跟随

在真实设备中，离开输入框后长按 W 进入引导。原生操作仍由你执行，引导观察控件，不会代发机器操作。

## 核对结果

检查真实库存、所选设置与目标去向。扩大规模前，先测试一次传输或一批加工。

<GuideOnly>

### 目标数量

输入期望本地数量，核对单位与上限，零在上级设备中可能表示清空或停用。

### 保存目标

确认目标资源后再保存，数量是目标值，不是已提供的库存堆叠。

### 返回设备

修改目标后检查上级配置，并测试真实补货。

</GuideOnly>
