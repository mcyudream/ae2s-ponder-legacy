---
id: ae2s_ponder:spatial_io
title: "空间 IO 与区域交换"
item_ids: [ae2:spatial_pylon, ae2:spatial_io_port, ae2:spatial_storage_cell_2, ae2:spatial_storage_cell_16, ae2:spatial_storage_cell_128]
structure: ae2s_ponder:spatial_io
tags: [ae2s_ponder:networks]
categories: [网络工程]
presentation: both
step_ticks: 180
---
# 空间 IO 与区域交换

## 界定空间区域

用相连的空间塔框架界定目标区域，把空间 IO 端口、能量源及必要控制线路放在交换区域之外，并确认可见空间场和尺寸。

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

## 选择合适空间元件

插入能够容纳该空间场尺寸的空间存储元件。普通物品存储元件不能存储区域，首次使用先选择小型测试区域。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        1,
        1,
        4
      ]
    },
    "duration": 175
  }
]
```

## 提供操作所需能量

查看 IO 端口显示的能量需求与效率，并在触发前充足储能。框架处于供电状态不等于已存有完成交换所需的全部能量。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        1,
        1,
        3
      ]
    },
    "duration": 175
  }
]
```

## 触发并完成交换

向空间 IO 端口提供所需红石触发，区域中的世界内容会与元件中的内容交换。首次实测前移走玩家和不可替代的物品。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        1,
        1,
        4
      ]
    },
    "duration": 175
  }
]
```

## 核对可搬移对象并还原

部分模组方块或实体可能不支持空间搬移，先用复制的装置验证，再用同一空间场和元件再次触发还原。每次都检查区块加载与储能。

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
        3,
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
