---
id: ae2s_ponder:fluid_storage
title: "Fluid Storage and Tank Automation"
item_ids: [ae2:fluid_storage_cell_1k, ae2:fluid_storage_cell_4k, ae2:fluid_storage_cell_16k, ae2:fluid_storage_cell_64k, ae2:import_bus, ae2:export_bus, ae2:storage_bus]
structure: ae2s_ponder:fluid_storage
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Fluid Storage and Tank Automation

## Use fluid-capable storage

Use a fluid-capable cell or a Storage Bus facing a compatible tank. An item-only cell does not become fluid storage when you put buckets in it. Inspect the supported resource types.

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

## Configure the resource

AE2S devices use their supported resource configuration. Select the desired fluid in the bus or interface configuration and test one transfer. Check which tank face exposes the fluid handler.

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

## Distinguish storage and transfer

A Storage Bus exposes a tank in place; an Import Bus pulls from it, while an Export Bus sends a selected fluid to it. Keep source and destination distinct to avoid circulation.

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

## Separate a pipe subnet

For dedicated tank-to-tank transport, isolate a small powered subnet with an Import Bus on the source and a Storage Bus on the destination. Check capacity and resource filters before leaving it unattended.

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
