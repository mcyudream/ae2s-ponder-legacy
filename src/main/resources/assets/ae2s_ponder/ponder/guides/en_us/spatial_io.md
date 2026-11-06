---
id: ae2s_ponder:spatial_io
title: "Spatial IO and Region Exchange"
item_ids: [ae2:spatial_pylon, ae2:spatial_io_port, ae2:spatial_storage_cell_2, ae2:spatial_storage_cell_16, ae2:spatial_storage_cell_128]
structure: ae2s_ponder:spatial_io
tags: [ae2s_ponder:networks]
categories: [Network Engineering]
presentation: both
step_ticks: 180
---
# Spatial IO and Region Exchange

## Define a region

Build a connected Spatial Pylon frame that bounds the target region. Keep the IO Port, energy supply and essential control wiring outside the volume being moved. Confirm the visible field and its dimensions.

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

## Match the spatial cell

Insert a Spatial Storage Cell that supports the field dimensions. Normal item storage cells cannot hold a region. Keep spare space in the cell and use a small test area first.

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        1,
        1,
        4
      ]
    },
    "duration": 175
  }
]
```

## Supply the operation energy

Read the IO Port energy requirement and efficiency. Charge enough network energy cells before triggering; a powered frame alone does not guarantee sufficient stored energy for the exchange.

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        1,
        1,
        3
      ]
    },
    "duration": 175
  }
]
```

## Trigger and exchange

Apply the required redstone trigger to the Spatial IO Port. It exchanges the bounded world contents with the cell contents. Remove players and irreplaceable objects before your first practical test.

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        1,
        1,
        4
      ]
    },
    "duration": 175
  }
]
```

## Verify support and restore

Some modded blocks or entities may not support spatial movement. Verify with a copied setup, then trigger the same field and cell again to restore the exchanged contents. Check chunk loading and energy each time.

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
        3,
        4
      ]
    },
    "duration": 175
  }
]
```

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
