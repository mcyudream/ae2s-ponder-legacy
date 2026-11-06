---
id: ae2s_ponder:processors
title: "压印器与处理器生产"
item_ids: [ae2:inscriber, ae2:silicon_press, ae2:logic_processor_press, ae2:calculation_processor_press, ae2:engineering_processor_press, ae2:logic_processor, ae2:calculation_processor, ae2:engineering_processor]
structure: ae2s_ponder:processors
tags: [ae2s_ponder:crafting]
categories: [自动合成]
presentation: both
step_ticks: 180
---
# 压印器与处理器生产

## 保留压印模板

用对应的压印模板制作电路，用硅压印模板制作硅板。模板作为工具保留在指定压印器内，当前原料以 JEI 为准。

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
        2
      ]
    },
    "duration": 175
  }
]
```

## 合成处理器

第二道工序将电路、硅板和红石组合为处理器。使用独立的组装压印器，可避免反复移动模板。

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

## 按槽位布线

压印器自动化取决于各个面能访问的槽位。逐条管线或总线测试一个物品，必要时旋转机器，并只从成品输出处提取。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        5,
        1,
        2
      ]
    },
    "duration": 175
  }
]
```

## 分阶段编码样板

将压印和最终组装分别编码为处理样板，填写消耗的原料和准确产物，不把留在机器里的模板写成每次消耗的材料。中间产物与最终成品都要回网。

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

## 排查停滞任务

若任务一直等待，依次检查原料、供电、槽位路线、印刷电路种类和成品提取。先跑通一个处理器，再增加并行机器或加速升级。

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
  },
  {
    "op": "world.create_item",
    "handle": "item4",
    "x": 3,
    "y": 2.4,
    "z": 3.5,
    "mx": 0,
    "my": 0,
    "mz": 0,
    "item": "ae2:logic_processor",
    "count": 1,
    "meta": 0
  },
  {
    "op": "world.move_item",
    "handle": "item4",
    "x": 4.5,
    "y": 2.4,
    "z": 3.5,
    "duration": 25
  },
  {
    "op": "scene.idle",
    "ticks": 30
  },
  {
    "op": "world.remove_item",
    "handle": "item4"
  }
]
```

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
