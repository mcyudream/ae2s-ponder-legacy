---
id: ae2s_ponder:condenser
title: "Condenser and Matter Conversion"
item_ids: [ae2:condenser, ae2:matter_ball, ae2:singularity]
structure: ae2s_ponder:condenser
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Condenser and Matter Conversion

## Keep valuables out

The Matter Condenser consumes inserted resources for matter power. Feed it only resources you intend to destroy; keep it off unrestricted main-network export paths.

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

## Select the output mode

Choose the required output mode in the GUI. Matter Balls and Singularities have different matter-power requirements; read the current interface rather than assuming one input item makes one output.

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

<GuiTutorial id="ae2s_ponder:condenser" duration={400} side="right" />

## Install supported storage

Insert a supported storage component when the selected output needs accumulated matter power. A normal filled storage cell is not a safe substitute for checking the accepted component slot.

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

## Extract and verify

Route the produced item to a separate collection inventory, then verify the next cycle. For a quantum link, the Singularity still needs the installed entangling recipe to become a paired set.

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

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
