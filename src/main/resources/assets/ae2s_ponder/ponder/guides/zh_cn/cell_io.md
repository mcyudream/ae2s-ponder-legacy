---
id: ae2s_ponder:cell_io
title: "用 IO 端口转移存储元件内容"
item_ids: [ae2:io_port, ae2:item_storage_cell_1k, ae2:fluid_storage_cell_1k]
structure: ae2s_ponder:cell_io
tags: [ae2s_ponder:automation]
categories: [存储与自动化]
presentation: both
step_ticks: 180
---
# 用 IO 端口转移存储元件内容

## 准备目标存储

连接 ME IO 端口和装有目标元件的驱动器。清空贵重源元件前，检查目标的可用字节、类型数量、分区和资源支持。

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

## 选择传输方向

在 IO 端口中选择元件到网络，或网络到元件的传输方向。确认方向箭头后，再将源元件或目标元件放入输入侧。

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

## 设置完成条件

设置处理后的元件何时移到输出侧，例如清空、装满或工作完成。加速卡提升转移速度，红石卡增加红石控制。

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

## 核对转移结果

取出输出元件，检查元件提示与终端库存。过滤或目标已满都可能让传输停止，确认内容已转移前不要丢弃源元件。

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
