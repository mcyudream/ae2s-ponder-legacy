---
id: ae2s_ponder:gui/stock_export_bus
title: "库存输出总线"
item_ids: [ae2:stock_export_bus]
structure: ae2s_ponder:gui/stock_export_bus
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 库存输出总线

## 找到设备

打开对应 AE2S 设备或相关子页面。结构展示其网络上下文，使用 GUI 演示查看控件与操作。

## 界面操作

跟随演示中的光标、高亮控件与资源条目。回放使用独立数据。

<GuiTutorial id="ae2s_ponder:stock_export_bus" duration={324} side="right" />

## 实机跟随

在真实设备中，离开输入框后长按 W 进入引导。原生操作仍由你执行，引导观察控件，不会代发机器操作。

## 核对结果

检查真实库存、所选设置与目标去向。扩大规模前，先测试一次传输或一批加工。

<GuideOnly>

### 资源过滤

设置目标容器应保有的数量，配置项不是已提供的实物；总线会尝试维持指定本地库存。

### 运行设置

检查当前总线支持的红石、匹配、调度与访问设置，可用项取决于总线类型和升级卡。

### 升级卡

只安装兼容升级卡，部分过滤槽会在安装容量升级前保持禁用。

### 资源过滤

先用少量物品确认方向、目标剩余空间和供电，避免对同一容器构成直接输入输出循环。

</GuideOnly>
