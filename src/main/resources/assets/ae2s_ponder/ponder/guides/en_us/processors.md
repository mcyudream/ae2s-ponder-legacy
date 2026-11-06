---
id: ae2s_ponder:processors
title: "Inscriber and Processor Production"
item_ids: [ae2:inscriber, ae2:silicon_press, ae2:logic_processor_press, ae2:calculation_processor_press, ae2:engineering_processor_press, ae2:logic_processor, ae2:calculation_processor, ae2:engineering_processor]
structure: ae2s_ponder:processors
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Inscriber and Processor Production

## Keep the presses

Use the matching press to print a circuit, and the Silicon Press to print silicon. Presses are tools; keep them in their assigned Inscribers. Check JEI for the current materials.

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

## Assemble the processor

A second operation combines the printed circuit, printed silicon and redstone into a processor. Use a separate assembly Inscriber so presses stay in place.

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

## Route to correct slots

Inscriber automation depends on the accessible slot on each face. Test one item from each pipe or bus, rotate the machine when needed, and extract only the product.

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
        2
      ]
    },
    "duration": 175
  }
]
```

## Encode the stages

Encode printing and final assembly as separate processing patterns. List consumed materials and exact products; do not include a press that remains installed. Return every intermediate and final product.

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

## Diagnose a stalled job

If crafting waits forever, inspect material stock, power, slot routing, the printed item variant, and extraction. Start with one processor before adding parallel machines or speed upgrades.

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
  },
  {
    "op": "world.create_item",
    "handle": "item4",
    "x": 3,
    "y": 2.4,
    "z": 3.5,
    "mx": 0,
    "my": 0,
    "mz": 0,
    "item": "ae2:logic_processor",
    "count": 1,
    "meta": 0
  },
  {
    "op": "world.move_item",
    "handle": "item4",
    "x": 4.5,
    "y": 2.4,
    "z": 3.5,
    "duration": 25
  },
  {
    "op": "scene.idle",
    "ticks": 30
  },
  {
    "op": "world.remove_item",
    "handle": "item4"
  }
]
```

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
