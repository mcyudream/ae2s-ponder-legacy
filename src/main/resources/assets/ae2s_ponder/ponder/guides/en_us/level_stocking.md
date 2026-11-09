---
id: ae2s_ponder:level_stocking
title: "Stock Control with a Level Emitter"
item_ids: [ae2:level_emitter, ae2:redstone_card, ae2:export_bus]
structure: ae2s_ponder:level_stocking
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Stock Control with a Level Emitter

## Choose the observed item

Configure a Level Emitter with the desired item and a threshold, such as 64 iron ingots. Choose whether it emits above or below that amount. Test the boundary with a small stock.

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

## Enable bus redstone control

Install a Redstone Card in the bus when required, then select its redstone mode. An emitter only supplies a signal; the receiving device must be configured to use it.

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

## Return the product

For production stocking, use the signal to enable ingredient export or the machine, then import finished goods into the same monitored storage. Exporting the finished item merely moves stock elsewhere.

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

## Allow for in-flight items

Machines and pipes can still contain ingredients when the threshold is crossed. Expect some overproduction; use buffers, batch limits, or interface stocking when an exact local amount is needed.

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

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
