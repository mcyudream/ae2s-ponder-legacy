---
id: ae2s_ponder:interfaces
title: "接口备货与回网"
item_ids: [ae2:interface, ae2:cable_interface]
structure: ae2s_ponder:interfaces
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 接口备货与回网

## 连接接口

将 ME 接口连接到供能网络，管道或机器可向接口的存储槽投入物品并送入 ME 存储；网络必须存在可接收的存储位置。

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

## 设置期望库存

在配置槽中设置物品和数量，接口会从网络存储补充本地库存。配置槽里的标记不是已经提供的真实物品。

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

<GuiTutorial id="ae2s_ponder:interface" duration={400} side="right" />

## 从本地库存取用

让相邻机器或管道消耗备货物品，确认其读取的是目标接口库存，再观察补货。避免取出路线将同批物品立即送回而形成循环。

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

<GuiTutorial id="ae2s_ponder:stock_amount" duration={400} side="right" />

## 按需合成缺货物品

接口支持的合成卡可用于请求能够自动合成的备货物品。网络仍需有效样板、可用原料和合成 CPU；向机器发送处理样板原料应使用样板供应器。

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
