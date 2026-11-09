---
id: ae2s_ponder:upgrades
title: "总线过滤与升级卡"
item_ids: [ae2:speed_card, ae2:capacity_card, ae2:fuzzy_card, ae2:inverter_card, ae2:crafting_card, ae2:redstone_card]
structure: ae2s_ponder:upgrades
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 总线过滤与升级卡

## 先设置过滤

安装升级前，先配置一种资源并测试总线方向。过滤图标是虚拟标记，为输出总线设置过滤不会自动提供要输出的物品。

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

## 扩展过滤与速度

容量卡在支持的设备上增加过滤容量，加速卡提升传输速度。允许数量和具体行为取决于设备，应以设备界面可接受的升级为准。

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

## 谨慎使用模糊与反相

设备支持时，模糊卡与反相卡会改变匹配方式。用损耗、标签相似的物品测试，反相过滤可能让实际通过的资源远多于预期。

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

## 合成与红石仍需配置

合成卡用于请求可自动合成的资源，仍需样板和 CPU。红石卡提供控制模式，安装后还要选择高电平、低电平或脉冲等所需行为。

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
