---
id: ae2s_ponder:quantum_bridge
title: "Quantum Network Bridge"
item_ids: [ae2:quantum_ring, ae2:quantum_link, ae2:quantum_entangled_singularity, ae2:singularity]
structure: ae2s_ponder:quantum_bridge
tags: [ae2s_ponder:networks]
categories: [Network Engineering]
presentation: both
step_ticks: 180
---
# Quantum Network Bridge

## Build both frames

At each location, build a flat 3 by 3 frame with eight Quantum Rings around one Quantum Link Chamber. Use the same plane for all nine blocks and keep both ends loaded.

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
        2,
        3
      ]
    },
    "duration": 175
  }
]
```

## Prepare one linked pair

Follow the installed recipe for Quantum Entangled Singularities. Keep the two items from the same generated pair together; unrelated singularities will not establish a link.

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
        2,
        3
      ]
    },
    "duration": 175
  }
]
```

## Install and power both ends

Place one paired singularity in each central chamber. Provide startup energy at both ends, then connect the ME cables through the supported ring connection points.

```ponder
[
  {
    "op": "overlay.show_outline",
    "color": "green",
    "slot": "focus",
    "selection": {
      "type": "position",
      "pos": [
        6,
        2,
        3
      ]
    },
    "duration": 175
  }
]
```

## Respect channel capacity

A Quantum Bridge transports the network connection; it does not manufacture channels. Check channel settings, cable bottlenecks and controller topology. Test a terminal at the far end before connecting a whole base.

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
