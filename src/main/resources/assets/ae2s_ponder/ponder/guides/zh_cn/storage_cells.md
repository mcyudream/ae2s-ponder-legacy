---
id: ae2s_ponder:storage_cells
title: "存储元件与分区"
item_ids: [ae2:drive, ae2:cell_workbench, ae2:item_storage_cell_1k, ae2:item_storage_cell_64k]
scene: ae2s_ponder:storage_cells
tags: [ae2s_ponder:basics]
categories: [基础入门]
presentation: both
step_ticks: 180
---
# 存储元件与分区

## 1

将存储元件放入 ME 驱动器，并保持驱动器供电、连接终端。

<GameScene scene="ae2s_ponder:storage_cells" tick={45} />

<GuiTutorial id="ae2s_ponder:drive" />

## 2

字节容量与类型容量是两个限制。更大的元件也有上限，请查看提示；还要选择支持目标资源的存储元件。

<GameScene scene="ae2s_ponder:storage_cells" tick={616} />

## 3

取出元件并放入元件工作台，添加过滤条目来限制可接收的资源。分区不会生成物品，也不会清空原有内容。

<GameScene scene="ae2s_ponder:storage_cells" tick={786} />

<GuiTutorial id="ae2s_ponder:cell_workbench" />

## 4

把配置好的元件放回驱动器。分别尝试存入允许的物品和其他物品，确认过滤规则生效。

<GameScene scene="ae2s_ponder:storage_cells" tick={1389} />

## 5

取出的存储元件会保留其中的内容。请妥善保管，并在取出前确认网络还有足够的可用存储空间。

<GameScene scene="ae2s_ponder:storage_cells" tick={1559} />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
