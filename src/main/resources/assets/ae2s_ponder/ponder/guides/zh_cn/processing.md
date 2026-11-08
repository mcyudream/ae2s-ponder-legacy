---
id: ae2s_ponder:processing
title: "处理样板与产物回收"
item_ids: [ae2:pattern_provider, ae2:processing_pattern, ae2:pattern_encoding_terminal, ae2:import_bus]
scene: ae2s_ponder:processing
tags: [ae2s_ponder:crafting]
categories: [自动合成]
presentation: both
step_ticks: 180
---
# 处理样板与产物回收

## 1

在样板编码终端中切换到处理模式。本例精确编码“1 个铁矿石 → 1 个铁锭”，再将样板放入供应器。

<GameScene scene="ae2s_ponder:processing" tick={45} />

<GuiTutorial id="ae2s_ponder:pattern_processing" />

## 2

把样板供应器放在熔炉上方，设置为向下输出，对准顶部原料入口。处理样板只描述配方，本身不会执行加工。

<GameScene scene="ae2s_ponder:processing" tick={616} />

<GuiTutorial id="ae2s_ponder:pattern_provider" />

## 3

原版熔炉从上方收原料、侧面收燃料、下方出成品。本例手动补充燃料，必须由真正的机器执行加工。

<GameScene scene="ae2s_ponder:processing" tick={1219} />

## 4

熔炉下方的输入总线朝上，从底部提取铁锭。回收线路必须连回发起任务的同一个 ME 网络。

<GameScene scene="ae2s_ponder:processing" tick={1421} />

## 5

从合成终端发起任务。CPU 会等待样板声明的产物回到 ME 存储，仅投入正确原料还不能完成任务。

<GameScene scene="ae2s_ponder:processing" tick={1591} />

## 6

任务卡住时，检查燃料、机器各面、产物提取、存储空间与样板数量。机器仍有原料时，阻挡模式可帮助避免批次混料。

<GameScene scene="ae2s_ponder:processing" tick={1761} />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
