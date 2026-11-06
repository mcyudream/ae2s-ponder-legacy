---
id: ae2s_ponder:subnetworks
title: "独立子网络与共享电力"
item_ids: [ae2:quartz_fiber, ae2:storage_bus, ae2:interface]
structure: ae2s_ponder:subnetworks
tags: [ae2s_ponder:networks]
categories: [网络工程]
presentation: both
step_ticks: 180
---
# 独立子网络与共享电力

## 切断网络直连

子网络必须在 ME 连接上实际独立。留出物理间隔或使用互不连接的染色线缆，同时检查完整方块机器是否绕过间隔将两边接通。

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

## 仅共享能量

用石英纤维连接两边，可共享能量而不共享频道和存储访问。每个子网络仍要分别满足自己的频道限制。

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

## 给运输网络指定目的地

运输子网络可在源容器安装输入总线，在目标容器安装存储总线。避免加入不需要的 ME 驱动器，导致搬运物品被截留到磁盘。

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

## 有目的地暴露存储

用存储总线面对接口，可以通过明确的库存边界访问另一网络。两套线缆仍要分离，并避免存储访问路线绕回自身形成循环。

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

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
