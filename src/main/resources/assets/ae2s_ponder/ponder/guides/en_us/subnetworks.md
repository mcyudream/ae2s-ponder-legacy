---
id: ae2s_ponder:subnetworks
title: "Independent Networks and Shared Power"
item_ids: [ae2:quartz_fiber, ae2:storage_bus, ae2:interface]
structure: ae2s_ponder:subnetworks
tags: [ae2s_ponder:networks]
categories: [Network Engineering]
presentation: both
step_ticks: 180
---
# Independent Networks and Shared Power

## Split the connections

A subnet is a genuinely separate ME network. Leave a physical gap or use cable colors that do not connect. Check full-block machines too: they can accidentally bridge the gap.

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

## Share only energy

Join the sides with Quartz Fiber to transfer energy without transferring channels or storage access. Each side must still satisfy its own channel limits.

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
        4
      ]
    },
    "duration": 175
  }
]
```

## Give transport a destination

A transport subnet can use an Import Bus at the source and a Storage Bus at the target inventory. Avoid adding an unintended drive that captures the transported items.

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

## Expose storage deliberately

A Storage Bus facing an Interface can expose another network through a controlled inventory boundary. Keep the two cable grids separate and avoid a storage path that loops back to its origin.

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

<GuiTutorial id="ae2s_ponder:storage_bus" duration={400} side="right" />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
