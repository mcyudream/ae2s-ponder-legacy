---
id: ae2s_ponder:crafting_cpu
title: "Crafting CPU Size and Concurrency"
item_ids: [ae2:1k_crafting_storage, ae2:4k_crafting_storage, ae2:16k_crafting_storage, ae2:64k_crafting_storage, ae2:crafting_accelerator, ae2:crafting_unit]
structure: ae2s_ponder:crafting_cpu
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Crafting CPU Size and Concurrency

## Make a solid cuboid

Join Crafting Storage, Co-Processing Units and optional Crafting Units into a solid cuboid. Keep different CPUs physically separate if they should execute separate jobs.

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
        1
      ]
    },
    "duration": 175
  }
]
```

## Add enough job storage

Crafting Storage supplies bytes used by the job plan. A Co-Processing Unit or ordinary Crafting Unit is not a substitute. Read the crafting plan when a task will not fit.

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
        1
      ]
    },
    "duration": 175
  }
]
```

## Parallelize the production path

Co-Processing Units let one CPU issue more operations concurrently, but machines, Pattern Providers, material stock and product-return paths must also support the throughput.

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
        1
      ]
    },
    "duration": 175
  }
]
```

## Watch dependencies

Recursive crafting requires a complete chain of patterns and available base ingredients. If a task waits, inspect the pending ingredient and exact returned quantity instead of only enlarging the CPU.

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

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
