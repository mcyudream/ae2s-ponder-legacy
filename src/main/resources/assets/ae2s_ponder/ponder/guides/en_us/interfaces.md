---
id: ae2s_ponder:interfaces
title: "Interface Stocking and Insertion"
item_ids: [ae2:interface, ae2:cable_interface]
structure: ae2s_ponder:interfaces
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Interface Stocking and Insertion

## Connect an interface

Connect an ME Interface to the powered network. Its storage slots can receive items from a pipe or machine and insert them into ME storage. Leave a valid storage destination.

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

## Set desired stock

Put ghost filter entries and quantities in the configuration slots. The interface keeps that local stock available by requesting it from network storage. Configuration entries are not real supplied items.

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

<GuiTutorial id="ae2s_ponder:interface" duration={400} side="right" />

## Consume locally

Let an adjacent machine or pipe consume the stocked items. Verify it reads the intended interface inventory, then watch replenishment. Keep extraction paths from feeding the same items straight back.

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

<GuiTutorial id="ae2s_ponder:stock_amount" duration={400} side="right" />

## Request missing stock

A supported Crafting Card can let the interface request craftable stock. The network still needs valid patterns, available ingredients and a Crafting CPU. Use a Pattern Provider for processing-pattern output.

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
