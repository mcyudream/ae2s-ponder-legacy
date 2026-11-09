---
id: ae2s_ponder:planes
title: "Formation and Annihilation Planes"
item_ids: [ae2:formation_plane, ae2:annihilation_plane]
structure: ae2s_ponder:planes
tags: [ae2s_ponder:automation]
categories: [Storage and Automation]
presentation: both
step_ticks: 180
---
# Formation and Annihilation Planes

## Face the work area

Place the panel on a cable face with open space directly in front. A Formation Plane places supported resources in the world; an Annihilation Plane collects or breaks supported targets.

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

## Provide storage access

The plane needs a powered network and usable storage paths. For a collection subnet, route the output to a Storage Bus on the destination inventory, keeping unintended main storage disconnected.

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

## Control what is placed

Configure the Formation Plane filter and any supported upgrades before supplying items. Test with cheap blocks and keep the work area clear so the panel cannot obstruct your control wiring.

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

<GuiTutorial id="ae2s_ponder:formation_plane" duration={400} side="right" />

## Confirm real drops

Check the Annihilation Plane behavior against the target block, collection mode and installed upgrades. Test where the drops go and what happens when destination storage is full.

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
        4
      ]
    },
    "duration": 175
  }
]
```

<GuiTutorial id="ae2s_ponder:annihilation_plane" duration={400} side="right" />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
