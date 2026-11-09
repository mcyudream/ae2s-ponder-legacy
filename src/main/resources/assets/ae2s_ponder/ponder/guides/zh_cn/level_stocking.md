---
id: ae2s_ponder:level_stocking
title: "用存储监控发信器控制库存"
item_ids: [ae2:level_emitter, ae2:redstone_card, ae2:export_bus]
structure: ae2s_ponder:level_stocking
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 用存储监控发信器控制库存

## 选择监控物品

为存储监控发信器选择目标物品和阈值，例如 64 个铁锭，并选择高于或低于阈值时发信。先用少量库存测试边界。

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

<GuiTutorial id="ae2s_ponder:level_emitter" duration={400} side="right" />

## 启用总线红石控制

按需给总线安装红石卡，并设置红石控制模式。发信器只负责提供信号，接收信号的设备必须配置为按信号工作。

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

<GuiTutorial id="ae2s_ponder:export_bus" duration={400} side="right" />

## 让成品回到网络

生产备货应通过信号启停原料输出或机器，再把成品导回被监控的存储。直接输出成品只是转移现有库存。

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
        5
      ]
    },
    "duration": 175
  }
]
```

## 考虑在途物品

达到阈值时机器和管道里可能仍有原料，因此会继续产出一部分成品。需要精确本地数量时可使用缓冲、批量限制或接口备货。

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
