---
id: ae2s_ponder:gui/interface
title: "ME 接口：备货与存入"
item_ids: [ae2:interface, ae2:cable_interface]
structure: ae2s_ponder:gui/interface
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# ME 接口：备货与存入

## 找到设备

打开对应 AE2S 设备或相关子页面。结构展示其网络上下文，使用 GUI 演示查看控件与操作。

## 界面操作

跟随演示中的光标、高亮控件与资源条目。回放使用独立数据。

<GuiTutorial id="ae2s_ponder:interface" duration={324} side="right" />

## 实机跟随

在真实设备中，离开输入框后长按 W 进入引导。原生操作仍由你执行，引导观察控件，不会代发机器操作。

## 核对结果

检查真实库存、所选设置与目标去向。扩大规模前，先测试一次传输或一批加工。

<GuideOnly>

### 期望库存配置

在配置槽设置物品与期望数量。这是请求库存的标记，不是已经提供的真实物品。

### 本地实物库存

网络具备电力、频道和足够库存时，接口会补充本地实物库存。

### 本地实物库存

让相邻机器从实物库存取用，避免管道将同批物品立即送回接口，形成循环。

### 本地实物库存

接口也可接收机器产物并存入网络。按处理样板投送原料，应使用样板供应器。

</GuideOnly>
