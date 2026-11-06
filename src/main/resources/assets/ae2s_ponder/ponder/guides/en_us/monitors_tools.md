---
id: ae2s_ponder:monitors_tools
title: "Monitors and Network Diagnostics"
item_ids: [ae2:storage_monitor, ae2:conversion_monitor, ae2:network_tool, ae2:certus_quartz_wrench, ae2:memory_card]
structure: ae2s_ponder:monitors_tools
tags: [ae2s_ponder:basics]
categories: [Basics]
presentation: both
step_ticks: 180
---
# Monitors and Network Diagnostics

## Display one resource

A Storage Monitor displays the configured resource count from its connected network. Configure it with the intended item and lock its selection when appropriate. It does not add storage capacity.

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

## Use a conversion monitor

A Conversion Monitor also provides supported insertion and extraction interactions for the selected resource. Try with a small stack and check the terminal to confirm the result.

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

## Inspect network power

Use the Network Tool on the relevant network to inspect energy and device information. Diagnose one branch at a time: power first, then cable connectivity, channels and storage space.

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

## Rotate and copy carefully

Use the wrench for supported rotation or dismantling. A Memory Card copies supported device settings or tunnel links; aim at the exact face and inspect its tooltip before applying it elsewhere.

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
