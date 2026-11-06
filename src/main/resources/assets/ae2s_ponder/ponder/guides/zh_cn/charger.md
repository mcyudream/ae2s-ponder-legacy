---
id: ae2s_ponder:charger
title: "赛特斯石英充能"
item_ids: [ae2:charger, ae2:crank, ae2:charged_certus_quartz_crystal]
structure: ae2s_ponder:charger
tags: [ae2s_ponder:basics]
categories: [基础入门]
presentation: both
step_ticks: 180
---
# 赛特斯石英充能

## 为充能器供能

把充能器连接到供能线缆。前期可在充能器上装木制曲柄手动转动；能量元件只能储能。

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
        2
      ]
    },
    "duration": 175
  }
]
```

## 放入石英

打开充能器放入赛特斯石英水晶，等待其变为充能赛特斯石英水晶后取出。整合包改动配方时以实际配方查看器为准。

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
        2
      ]
    },
    "duration": 175
  },
  {
    "op": "world.create_item",
    "handle": "item1",
    "x": 3,
    "y": 2.4,
    "z": 2.5,
    "mx": 0,
    "my": 0,
    "mz": 0,
    "item": "ae2:certus_quartz_crystal",
    "count": 1,
    "meta": 0
  },
  {
    "op": "world.move_item",
    "handle": "item1",
    "x": 4.5,
    "y": 2.4,
    "z": 2.5,
    "duration": 25
  },
  {
    "op": "scene.idle",
    "ticks": 30
  },
  {
    "op": "world.remove_item",
    "handle": "item1"
  }
]
```

## 连接输入输出

用处理样板描述充能配方，由样板供应器投入原料，再用输入总线或独立运输子网络回收充能产物。

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

## 验收一个完整循环

扩大生产前先请求一颗充能水晶，确认供电、机器允许的输入输出面以及产物回到发起任务的网络。演示用于说明流程，不在虚拟场景中执行机器配方。

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
        3
      ]
    },
    "duration": 175
  }
]
```

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
