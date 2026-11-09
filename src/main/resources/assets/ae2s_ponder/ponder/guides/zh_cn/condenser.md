---
id: ae2s_ponder:condenser
title: "物质聚合器与物质转换"
item_ids: [ae2:condenser, ae2:matter_ball, ae2:singularity]
structure: ae2s_ponder:condenser
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 物质聚合器与物质转换

## 隔离贵重资源

物质聚合器会消耗投入资源以积累物质能量。只投入计划销毁的资源，不要将其接到无过滤的主网输出路线。

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

## 选择输出模式

在界面选择所需产出模式。物质球和奇点需要的物质能量不同，应查看当前界面需求，不能假定一个输入直接换一个成品。

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

<GuiTutorial id="ae2s_ponder:condenser" duration={400} side="right" />

## 安装支持的储能组件

需要积累物质能量的输出模式应在指定槽位安装支持的存储组件。先核对槽位要求，不要将装有物品的存储元件当成替代品。

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

## 提取并核对成品

将产物送入独立收集容器，并核对下一个周期。用于量子连接的奇点还需要通过实际缠绕配方，变成配对的量子缠绕奇点。

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
