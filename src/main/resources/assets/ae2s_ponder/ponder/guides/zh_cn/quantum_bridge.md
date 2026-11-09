---
id: ae2s_ponder:quantum_bridge
title: "量子网络桥"
item_ids: [ae2:quantum_ring, ae2:quantum_link, ae2:quantum_entangled_singularity, ae2:singularity]
structure: ae2s_ponder:quantum_bridge
tags: [ae2s_ponder:networks]
categories: [网络工程]
presentation: both
step_ticks: 180
---
# 量子网络桥

## 搭建两端框架

在两个地点各搭建一个平面 3×3 结构：八个量子环围绕中央量子链接仓。九个方块须位于同一平面，两端都需要区块加载。

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
        3
      ]
    },
    "duration": 175
  }
]
```

## 准备同一对奇点

按当前整合包配方制作量子缠绕奇点，保留同次生成的一对。分别取得但不属于同一对的奇点不能建立量子连接。

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
        3
      ]
    },
    "duration": 175
  }
]
```

## 安装奇点并为两端供电

将配对奇点分别放入两端中央仓，为两端提供启动能量，再从结构支持的量子环接入 ME 线缆。

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        6,
        2,
        3
      ]
    },
    "duration": 175
  }
]
```

<GuiTutorial id="ae2s_ponder:quantum_bridge" duration={400} side="right" />

## 保留频道容量

量子桥负责传输网络连接，不会生成额外频道。检查频道设置、线缆瓶颈和控制器拓扑，先在远端测试一个终端，再连接整座基地。

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
