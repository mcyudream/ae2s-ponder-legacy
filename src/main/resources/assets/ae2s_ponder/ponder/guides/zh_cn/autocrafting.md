---
id: ae2s_ponder:autocrafting
title: "使用样板供应器自动合成"
item_ids: [ae2:pattern_provider, ae2:cable_pattern_provider, ae2:molecular_assembler, ae2:pattern_encoding_terminal, ae2:blank_pattern, ae2:crafting_pattern, ae2:1k_crafting_storage, ae2:crafting_accelerator]
scene: ae2s_ponder:autocrafting
tags: [ae2s_ponder:crafting]
categories: [自动合成]
presentation: both
step_ticks: 180
---
# 使用样板供应器自动合成

## 1

在样板编码终端中放入空白样板，选择合成模式。编码一条实际配方，例如 9 个铁锭合成 1 个铁块。

<GameScene scene="ae2s_ponder:autocrafting" tick={45} />

## 2

把编码后的合成样板放入样板供应器，让它紧贴分子装配室，并将供应器接入有电的 ME 网络。

<GameScene scene="ae2s_ponder:autocrafting" tick={215} />

## 3

搭建实心长方体合成 CPU，至少包含一个合成存储器。并行处理单元用于增加并行操作，不能代替合成存储器。

<GameScene scene="ae2s_ponder:autocrafting" tick={385} />

## 4

确保网络中有足够原料。打开合成终端，选中可合成的产物，填写数量并确认合成计划。

<GameScene scene="ae2s_ponder:autocrafting" tick={555} />

## 5

样板供应器向装配室提供原料。装配室按样板合成，再通过供应器把成品送回网络。

<GameScene scene="ae2s_ponder:autocrafting" tick={789} />

## 6

AE2S 使用独立的样板供应器。此结构中的供应器不能直接用 ME 接口代替。箭头用于说明物品流向。

<GameScene scene="ae2s_ponder:autocrafting" tick={959} />

<GuideOnly>

[排查与索引](troubleshooting.md)

</GuideOnly>
