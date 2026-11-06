---
id: ae2s_ponder:quartz_growth
title: "石英生长与福鲁伊克斯材料"
item_ids: [ae2:flawless_budding_quartz, ae2:flawed_budding_quartz, ae2:chipped_budding_quartz, ae2:damaged_budding_quartz, ae2:quartz_cluster, ae2:growth_accelerator, ae2:fluix_crystal]
structure: ae2s_ponder:quartz_growth
tags: [ae2s_ponder:basics]
categories: [基础入门]
presentation: both
step_ticks: 180
---
# 石英生长与福鲁伊克斯材料

## 为晶芽留出空间

赛特斯石英母岩在裸露面生长晶芽。为这些面留出空间，等到完整晶簇再采收，避免把母岩本体一起破坏。

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

## 留意母岩损耗

检查母岩等级，有瑕疵、碎裂和损坏的母岩存在降级过程。按 AE2S 实际配方准备替换母岩或使用其专用晶体机器。

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
        2,
        2
      ]
    },
    "duration": 175
  }
]
```

## 为生长加速供能

在生长面旁放置并供能给生长加速器，同时避免线缆占用晶芽空间；没有供电的加速器不会提供帮助。

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
        2
      ]
    },
    "duration": 175
  }
]
```

## 区分福鲁伊克斯工序

启用经典水中转换配方时，需要充能赛特斯石英、红石和下界石英。先核对整合包配方，再收集福鲁伊克斯水晶，并将这条工序与晶芽农场分开。

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

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
