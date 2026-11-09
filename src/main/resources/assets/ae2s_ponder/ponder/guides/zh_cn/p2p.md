---
id: ae2s_ponder:p2p
title: "连接 ME P2P 隧道"
item_ids: [ae2:me_p2p_tunnel, ae2:memory_card, ae2:advanced_memory_card]
scene: ae2s_ponder:p2p
tags: [ae2s_ponder:networks]
categories: [网络工程]
presentation: both
step_ticks: 180
---
# 连接 ME P2P 隧道

## 1

把 ME P2P 输入隧道朝向来源控制器。隧道的外侧接收需要传输的频道。

<GameScene scene="ae2s_ponder:p2p" tick={45} />

## 2

把两个隧道背面的线缆接入独立的承载网络，并为其供电。这里用石英纤维传递能量，避免承载网与来源网合并。

<GameScene scene="ae2s_ponder:p2p" tick={215} />

## 3

手持内存卡，潜行并右键输入隧道，保存连接。注意对准隧道表面，而不是背后的线缆。

<GameScene scene="ae2s_ponder:p2p" tick={385} />

## 4

用同一张内存卡右键输出隧道，将它设为同频率输出端。可以继续绑定更多输出端，它们共享输入端可用的频道。

<GameScene scene="ae2s_ponder:p2p" tick={555} />

## 5

正常设置下，ME 隧道最多传输 32 个频道。外侧超过 8 频道时应使用致密线缆；P2P 不会凭空增加控制器容量。

<GameScene scene="ae2s_ponder:p2p" tick={725} />

## 6

每个隧道都需要承载网提供能量与频道。扩建设备前，检查输入输出角色、绑定频率和承载网剩余容量。

<GameScene scene="ae2s_ponder:p2p" tick={895} />

<GuiTutorial id="ae2s_ponder:advanced_memory_card" />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
