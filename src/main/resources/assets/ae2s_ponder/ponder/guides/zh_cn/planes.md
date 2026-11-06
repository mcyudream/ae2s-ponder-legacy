---
id: ae2s_ponder:planes
title: "成型面板与湮灭面板"
item_ids: [ae2:formation_plane, ae2:annihilation_plane]
structure: ae2s_ponder:planes
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 成型面板与湮灭面板

## 朝向工作区域

把面板装在线缆面上，正前方留出工作空间。成型面板将支持的资源放入世界，湮灭面板收集或破坏其支持的目标。

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

## 提供存储访问

面板需要供能网络和可用存储路线。收集子网络可通过面对目标容器的存储总线存放产物，同时与不希望接入的主网存储保持分离。

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
        4
      ]
    },
    "duration": 175
  }
]
```

## 限制成型物品

供料前配置成型面板过滤与支持的升级。用廉价方块测试，保持工作区域清晰，避免面板把控制线或操作通道堵住。

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

## 核对实际掉落

按目标方块、收集模式和已装升级检查湮灭面板行为，并测试掉落流向以及目标存储装满时的结果。

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
        4
      ]
    },
    "duration": 175
  }
]
```

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
