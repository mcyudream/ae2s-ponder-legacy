---
id: ae2s_ponder:crafting_cpu
title: "合成 CPU 容量与并行"
item_ids: [ae2:1k_crafting_storage, ae2:4k_crafting_storage, ae2:16k_crafting_storage, ae2:64k_crafting_storage, ae2:crafting_accelerator, ae2:crafting_unit]
structure: ae2s_ponder:crafting_cpu
tags: [ae2s_ponder:crafting]
categories: [自动合成]
presentation: both
step_ticks: 180
---
# 合成 CPU 容量与并行

## 搭建实心长方体

将合成存储器、并行处理单元及可选合成单元组成实心长方体。需要执行独立任务的多个 CPU，应在物理上分隔。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        3,
        1,
        1
      ]
    },
    "duration": 175
  }
]
```

## 提供足够任务容量

合成存储器提供任务计划需要的字节容量。并行处理单元和普通合成单元不能代替存储器；任务放不下时查看合成计划的容量需求。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        2,
        1,
        1
      ]
    },
    "duration": 175
  }
]
```

## 同时扩展生产路径

并行处理单元使同一个 CPU 能同时发出更多操作，但机器、样板供应器、原料库存与产物回网路线也必须有对应吞吐能力。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        4,
        1,
        1
      ]
    },
    "duration": 175
  }
]
```

## 检查依赖关系

递归合成需要完整的样板依赖链和可用基础原料。任务等待时，检查正在等待的材料和准确回网数量，不能只靠扩大 CPU 解决。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        4,
        1,
        3
      ]
    },
    "duration": 175
  }
]
```

<GuiTutorial id="ae2s_ponder:crafting_status" duration={400} side="right" />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
