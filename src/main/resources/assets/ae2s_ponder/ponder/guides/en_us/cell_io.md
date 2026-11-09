---
id: ae2s_ponder:cell_io
title: "Moving Storage Cell Contents"
item_ids: [ae2:io_port, ae2:item_storage_cell_1k, ae2:fluid_storage_cell_1k]
structure: ae2s_ponder:cell_io
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Moving Storage Cell Contents

## Prepare destination storage

Connect the ME IO Port and a drive with suitable destination cells. Before emptying a valuable source cell, check free bytes, remaining types, partitions, and resource support.

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

## Choose direction

Use the direction control in the IO Port to choose cell-to-network or network-to-cell transfer. Insert the source or destination cell in the input side after checking the arrow.

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

<GuiTutorial id="ae2s_ponder:io_port" duration={400} side="right" />

## Choose completion behavior

Choose when the processed cell moves to the output side: empty, full, or work complete. Speed Cards improve transfer throughput; Redstone Cards add redstone controls.

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

## Verify the result

Remove the output cell and inspect both its tooltip and terminal inventory. Filters or a full destination can stop progress. Never discard a source cell until you have verified its contents were transferred.

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
