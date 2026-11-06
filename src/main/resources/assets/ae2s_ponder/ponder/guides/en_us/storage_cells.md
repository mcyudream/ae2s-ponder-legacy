---
id: ae2s_ponder:storage_cells
title: "Storage Cells and Partitioning"
item_ids: [ae2:drive, ae2:cell_workbench, ae2:item_storage_cell_1k, ae2:item_storage_cell_64k]
scene: ae2s_ponder:storage_cells
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Storage Cells and Partitioning

## 1

Put a storage cell into the ME Drive. Keep the drive powered and connected to a terminal.

<GameScene scene="ae2s_ponder:storage_cells" tick={45} />

## 2

Bytes and type capacity are separate limits. A larger cell is not unlimited; inspect its tooltip. Use a cell that supports the resource you want to store.

<GameScene scene="ae2s_ponder:storage_cells" tick={215} />

## 3

Take the cell to a Cell Workbench. Add filter entries to partition which resources it may accept; partitioning does not create items or erase existing contents.

<GameScene scene="ae2s_ponder:storage_cells" tick={385} />

## 4

Return the configured cell to the drive. Test inserting an allowed item and a different item to check your filter.

<GameScene scene="ae2s_ponder:storage_cells" tick={587} />

## 5

Removing a cell keeps its contents on that cell. Keep valuable cells safe and check the remaining network storage before removing one.

<GameScene scene="ae2s_ponder:storage_cells" tick={757} />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
