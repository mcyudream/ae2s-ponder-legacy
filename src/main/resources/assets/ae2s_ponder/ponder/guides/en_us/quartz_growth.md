---
id: ae2s_ponder:quartz_growth
title: "Quartz Growth and Fluix Materials"
item_ids: [ae2:flawless_budding_quartz, ae2:flawed_budding_quartz, ae2:chipped_budding_quartz, ae2:damaged_budding_quartz, ae2:quartz_cluster, ae2:growth_accelerator, ae2:fluix_crystal]
structure: ae2s_ponder:quartz_growth
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Quartz Growth and Fluix Materials

## Leave room for buds

Budding Certus Quartz grows buds on exposed faces. Leave those faces unobstructed and wait for the full cluster before harvesting. Avoid breaking the budding block.

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

## Plan for wear

Inspect the budding block tier: flawed, chipped and damaged variants can degrade. Use the actual AE2S recipe viewer to plan replacements or its dedicated crystal machines.

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

## Supply growth energy

Place a powered Growth Accelerator next to the growing faces. Keep its cable from blocking the growth space; adding an unpowered accelerator will not help.

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

## Separate fluix processing

Charged Certus Quartz, redstone and Nether Quartz are used by the familiar water conversion recipe when enabled. Check the pack recipe first, collect the Fluix Crystal, and keep the growth farm separate.

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

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
