---
id: ae2s_ponder:charger
title: "Charging Certus Quartz"
item_ids: [ae2:charger, ae2:crank, ae2:charged_certus_quartz_crystal]
structure: ae2s_ponder:charger
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Charging Certus Quartz

## Power the charger

Place the Charger beside the powered cable. Early on, attach a Wooden Crank and turn it by hand; an Energy Cell only buffers energy.

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

## Insert a crystal

Open the Charger and insert Certus Quartz Crystal. Wait for the Charged Certus Quartz Crystal, then remove the result. Use the installed recipe viewer if the pack changes the input.

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
  },
  {
    "op": "world.create_item",
    "handle": "item1",
    "x": 3,
    "y": 2.4,
    "z": 2.5,
    "mx": 0,
    "my": 0,
    "mz": 0,
    "item": "ae2:certus_quartz_crystal",
    "count": 1,
    "meta": 0
  },
  {
    "op": "world.move_item",
    "handle": "item1",
    "x": 4.5,
    "y": 2.4,
    "z": 2.5,
    "duration": 25
  },
  {
    "op": "scene.idle",
    "ticks": 30
  },
  {
    "op": "world.remove_item",
    "handle": "item1"
  }
]
```

## Automate input and output

Use a processing pattern for the charging recipe and a Pattern Provider to deliver the input. Return the charged result with an Import Bus or a separate transport subnet.

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

## Check a full cycle

Request one charged crystal before scaling up. Confirm power, allowed machine sides, and product return to the requesting network. The diagram illustrates the sequence; it does not run machine recipes.

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
