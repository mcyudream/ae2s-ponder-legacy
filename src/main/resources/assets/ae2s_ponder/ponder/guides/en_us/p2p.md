---
id: ae2s_ponder:p2p
title: "Connecting ME P2P Tunnels"
item_ids: [ae2:me_p2p_tunnel, ae2:memory_card, ae2:advanced_memory_card]
scene: ae2s_ponder:p2p
tags: [ae2s_ponder:networks]
categories: [Network Engineering]
presentation: both
step_ticks: 180
---
# Connecting ME P2P Tunnels

## 1

Place an ME P2P input facing the source controller. The tunnel's outer face receives the channels you want to transport.

<GameScene scene="ae2s_ponder:p2p" tick={45} />

## 2

Connect the backs of both tunnels to a separate powered carrier network. Quartz Fiber supplies power here without merging the carrier with the source network.

<GameScene scene="ae2s_ponder:p2p" tick={215} />

## 3

Use a Memory Card: sneak + right-click the input tunnel to save its connection. Aim at the tunnel face, not the cable behind it.

<GameScene scene="ae2s_ponder:p2p" tick={385} />

## 4

Right-click the output tunnel with that Memory Card. It becomes an output on the same frequency; additional outputs share the input's available channels.

<GameScene scene="ae2s_ponder:p2p" tick={555} />

## 5

With normal settings, an ME tunnel transports up to 32 channels. Use dense cable on the outer side for more than 8; P2P does not create extra controller capacity.

<GameScene scene="ae2s_ponder:p2p" tick={725} />

## 6

Each tunnel needs power and a channel on the carrier. Check input/output roles, matching frequency and carrier capacity before adding more devices.

<GameScene scene="ae2s_ponder:p2p" tick={895} />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
