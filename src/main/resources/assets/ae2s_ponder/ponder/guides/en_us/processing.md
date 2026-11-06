---
id: ae2s_ponder:processing
title: "Processing Patterns and Product Return"
item_ids: [ae2:pattern_provider, ae2:processing_pattern, ae2:pattern_encoding_terminal, ae2:import_bus]
scene: ae2s_ponder:processing
tags: [ae2s_ponder:crafting]
categories: [Autocrafting]
presentation: both
step_ticks: 180
---
# Processing Patterns and Product Return

## 1

Select processing mode in the Pattern Encoding Terminal. For this example, encode exactly 1 iron ore into 1 iron ingot, then store the pattern in the provider.

<GameScene scene="ae2s_ponder:processing" tick={45} />

## 2

Place the Pattern Provider above the furnace and configure it to output downward into the top input. Processing patterns describe a recipe but do not perform it.

<GameScene scene="ae2s_ponder:processing" tick={215} />

## 3

A vanilla furnace accepts smelting input from above, fuel from a side and output from below. Add fuel manually for this example; a real machine must process the ingredients.

<GameScene scene="ae2s_ponder:processing" tick={417} />

## 4

The Import Bus below the furnace faces upward and extracts the ingot from its bottom output. Keep this return path connected to the same crafting network.

<GameScene scene="ae2s_ponder:processing" tick={619} />

## 5

Start the job from a Crafting Terminal. The CPU waits for the declared result to return to ME storage; correct input alone does not complete the job.

<GameScene scene="ae2s_ponder:processing" tick={789} />

## 6

If a job stalls, check fuel, machine sides, output extraction, storage space and exact pattern amounts. Blocking mode can help prevent mixing batches when a machine still contains ingredients.

<GameScene scene="ae2s_ponder:processing" tick={959} />

<GuideOnly>

[Troubleshooting and topic index](troubleshooting.md)

</GuideOnly>
