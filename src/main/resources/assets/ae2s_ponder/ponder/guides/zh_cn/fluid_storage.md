---
id: ae2s_ponder:fluid_storage
title: "流体存储与储罐自动化"
item_ids: [ae2:fluid_storage_cell_1k, ae2:fluid_storage_cell_4k, ae2:fluid_storage_cell_16k, ae2:fluid_storage_cell_64k, ae2:import_bus, ae2:export_bus, ae2:storage_bus]
structure: ae2s_ponder:fluid_storage
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 流体存储与储罐自动化

## 准备流体存储

使用支持流体的存储元件，或用存储总线面对兼容储罐。仅支持物品的元件不会因为存入水桶就变成流体存储，应检查支持的资源种类。

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
        3
      ]
    },
    "duration": 175
  }
]
```

## 配置目标资源

按 AE2S 设备支持的资源配置方式，在总线或接口中选择目标流体并测试一次传输，同时确认储罐哪个面提供流体能力。

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

<GuiTutorial id="ae2s_ponder:storage_bus" duration={400} side="right" />

## 区分访问与搬运

存储总线直接暴露储罐中的内容，输入总线从储罐抽取，输出总线向其发送所选流体。明确源和目标，避免建立无意义的循环。

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

## 建立独立运输子网络

专门的储罐间运输可用独立供能子网络：源罐输入总线、目标罐存储总线。离开前检查目标容量和资源过滤。

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
