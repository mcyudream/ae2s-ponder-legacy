---
id: ae2s_ponder:wireless
title: "无线终端配对与供能"
item_ids: [ae2:wireless_access_point, ae2:wireless_terminal, ae2:wireless_crafting_terminal, ae2:wireless_booster]
structure: ae2s_ponder:wireless
tags: [ae2s_ponder:networks]
categories: [网络工程]
presentation: both
step_ticks: 180
---
# 无线终端配对与供能

## 连接无线访问点

将无线访问点接入拥有目标存储的网络，配对前确认供电与频道正常。无线访问点不会自动合并彼此独立的网络。

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

## 通过槽位配对

打开无线访问点，将无线终端放入配对输入槽，再从输出槽取出已配对的终端。AE2S 1.1.0 使用这个界面完成配对。

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

<GuiTutorial id="ae2s_ponder:wireless_access_point" duration={400} side="right" />

## 充电并保持在覆盖范围内

用充能器或其他支持的方式给终端充电，并在访问点覆盖范围内打开。无线增程器会同时提高覆盖与耗电，不代表无限距离。

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

<GuiTutorial id="ae2s_ponder:wireless_terminal" duration={400} side="right" />

## 排查无法连接

检查终端电量、绑定访问点、当前维度、距离和区块加载状态。移动或拆除绑定的访问点后，可能需要重新配对。

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
