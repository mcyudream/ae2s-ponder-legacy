---
id: ae2s_ponder:gui/work_interval
title: "机器工作间隔"
item_ids: [ae2:advanced_io_bus, ae2:import_export_bus, ae2:stock_export_bus]
structure: ae2s_ponder:gui/work_interval
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 机器工作间隔

## 找到设备

打开对应 AE2S 设备或相关子页面。结构展示其网络上下文，使用 GUI 演示查看控件与操作。

## 界面操作

跟随演示中的光标、高亮控件与资源条目。回放使用独立数据。

<GuiTutorial id="ae2s_ponder:work_interval" duration={320} side="right" />

## 实机跟随

在真实设备中，离开输入框后长按 W 进入引导。原生操作仍由你执行，引导观察控件，不会代发机器操作。

## 核对结果

检查真实库存、所选设置与目标去向。扩大规模前，先测试一次传输或一批加工。

<GuideOnly>

### 工作间隔

按显示单位设置间隔，缩短间隔会增加检查频率，不会创造原料或目标空间。

### 观察结果

为大量设备应用很短间隔前，先测试实际吞吐与服务器负载。

</GuideOnly>
