---
id: ae2s_ponder:autocrafting
title: "Autocrafting with a Pattern Provider"
item_ids: [ae2:pattern_provider, ae2:cable_pattern_provider, ae2:molecular_assembler, ae2:pattern_encoding_terminal, ae2:blank_pattern, ae2:crafting_pattern, ae2:1k_crafting_storage, ae2:crafting_accelerator]
scene: ae2s_ponder:autocrafting
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Autocrafting with a Pattern Provider

## 1

In a Pattern Encoding Terminal, insert a Blank Pattern and select crafting mode. Encode a real recipe, such as 9 iron ingots into 1 iron block.

<GameScene scene="ae2s_ponder:autocrafting" tick={45} />

<GuiTutorial id="ae2s_ponder:pattern_crafting" />

## 2

Put the encoded Crafting Pattern in a Pattern Provider touching a Molecular Assembler. Connect the provider to the powered ME network.

<GameScene scene="ae2s_ponder:autocrafting" tick={616} />

<GuiTutorial id="ae2s_ponder:pattern_provider" />

## 3

Build a solid cuboid Crafting CPU containing Crafting Storage. A Co-Processing Unit adds parallel operations; it does not replace Crafting Storage.

<GameScene scene="ae2s_ponder:autocrafting" tick={1187} />

<GuiTutorial id="ae2s_ponder:crafting_cpu" />

## 4

Store enough ingredients on the network. Open a Crafting Terminal, select the craftable result, choose an amount and confirm the crafting plan.

<GameScene scene="ae2s_ponder:autocrafting" tick={1758} />

<GuiTutorial id="ae2s_ponder:craft_amount" />

<GuiTutorial id="ae2s_ponder:craft_confirm" />

## 5

The provider supplies the assembler. The assembler crafts the encoded recipe and returns its result through the provider to the network.

<GameScene scene="ae2s_ponder:autocrafting" tick={2794} />

## 6

AE2S has a dedicated Pattern Provider. An ME Interface is not a substitute for the provider used in this layout. These arrows illustrate the item path.

<GameScene scene="ae2s_ponder:autocrafting" tick={2964} />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
