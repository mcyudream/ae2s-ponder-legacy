---
id: ae2s_ponder:wireless
title: "Wireless Terminal Pairing"
item_ids: [ae2:wireless_access_point, ae2:wireless_terminal, ae2:wireless_crafting_terminal, ae2:wireless_booster]
structure: ae2s_ponder:wireless
tags: [ae2s_ponder:networks]
categories: [Network Engineering]
presentation: both
step_ticks: 180
---
# Wireless Terminal Pairing

## Connect an access point

Connect the Wireless Access Point to the network that owns your storage. Confirm power and channels before pairing a terminal. An access point does not merge independent networks.

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

## Pair through its slot

Open the access point. Insert the wireless terminal in its link input slot, then take the paired item from the output slot. AE2S 1.1.0 pairs through this GUI.

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

## Charge and stay in range

Charge the terminal with a Charger or another supported charging method. Open it within access-point range. Range boosters increase coverage and power use; they do not give unlimited range.

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

## Diagnose disconnection

Check the terminal charge, its linked access point, current dimension, distance, and loaded chunks. Moving or removing the bound access point can require pairing again.

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
