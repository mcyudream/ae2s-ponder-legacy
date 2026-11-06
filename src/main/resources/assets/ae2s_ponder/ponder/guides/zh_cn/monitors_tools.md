---
id: ae2s_ponder:monitors_tools
title: "监视器与网络诊断工具"
item_ids: [ae2:storage_monitor, ae2:conversion_monitor, ae2:network_tool, ae2:certus_quartz_wrench, ae2:memory_card]
structure: ae2s_ponder:monitors_tools
tags: [ae2s_ponder:basics]
categories: [基础入门]
presentation: both
step_ticks: 180
---
# 监视器与网络诊断工具

## 显示单一资源

存储监视器显示所在网络中所选资源的数量。用目标物品配置，按需锁定选择；监视器本身不提供额外存储容量。

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

## 使用转换监视器

转换监视器还提供所选资源的交互存取操作。先用一小叠物品尝试，并通过终端核对存入或取出的结果。

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

## 检查网络供能

用网络工具检查目标网络的能量和设备信息。逐条分支排查，顺序为供电、线缆连接、频道和存储空间。

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

## 正确使用扳手与存储卡

用扳手执行设备支持的旋转或拆卸。存储卡可复制支持的设置或隧道连接，操作时对准准确部件面，并在应用前查看卡片提示。

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
