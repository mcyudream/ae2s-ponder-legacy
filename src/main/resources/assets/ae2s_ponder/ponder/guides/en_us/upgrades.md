---
id: ae2s_ponder:upgrades
title: "Bus Filters and Upgrade Cards"
item_ids: [ae2:speed_card, ae2:capacity_card, ae2:fuzzy_card, ae2:inverter_card, ae2:crafting_card, ae2:redstone_card]
structure: ae2s_ponder:upgrades
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Bus Filters and Upgrade Cards

## Start with the filter

Configure one desired resource and test the bus direction before installing upgrades. Filter icons are ghost entries, so placing a filter does not provide the items that an Export Bus will send.

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

## Increase capacity or speed

Capacity Cards add filter capacity on supported devices; Speed Cards raise transfer throughput. Their allowed count and behavior depend on the device. Use only the slots accepted by its GUI.

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

## Use fuzzy and inversion carefully

Fuzzy and Inverter Cards change matching behavior where supported. Test with similar damaged or tagged items; a reversed filter can send a much broader set than intended.

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

## Crafting and redstone need setup

A Crafting Card requests craftable resources and still needs patterns and a CPU. A Redstone Card exposes control modes; select the desired high, low or pulse behavior after installation.

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
