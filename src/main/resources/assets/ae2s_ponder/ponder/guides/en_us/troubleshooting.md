---
id: ae2s_ponder:troubleshooting
title: Tutorial Index and Troubleshooting
item_ids: [ae2:network_tool]
presentation: guide
---
# Tutorial Index and Troubleshooting

These tutorials target AE2S / Supergiant 1.1.0 on Minecraft 1.12.2 / Cleanroom. Resource recipes and channel settings may be changed by the modpack.

## Basics

- [Your First ME Network](first_network.md)
- [Storage Cells and Partitioning](storage_cells.md)
- [Channels and Cable Capacity](channels.md)
- [Charging Certus Quartz](charger.md)
- [Quartz Growth and Fluix Materials](quartz_growth.md)
- [Monitors and Network Diagnostics](monitors_tools.md)

## Storage and Automation

- [Using External Inventories](storage_bus.md)
- [Importing and Exporting Items](import_export.md)
- [Interface Stocking and Insertion](interfaces.md)
- [Stock Control with a Level Emitter](level_stocking.md)
- [Moving Storage Cell Contents](cell_io.md)
- [Formation and Annihilation Planes](planes.md)
- [Bus Filters and Upgrade Cards](upgrades.md)
- [Fluid Storage and Tank Automation](fluid_storage.md)
- [Condenser and Matter Conversion](condenser.md)

## Autocrafting

- [Autocrafting with a Pattern Provider](autocrafting.md)
- [Processing Patterns and Product Return](processing.md)
- [Inscriber and Processor Production](processors.md)
- [Crafting CPU Size and Concurrency](crafting_cpu.md)

## Network Engineering

- [Connecting ME P2P Tunnels](p2p.md)
- [Independent Networks and Shared Power](subnetworks.md)
- [Wireless Terminal Pairing](wireless.md)
- [Quantum Network Bridge](quantum_bridge.md)
- [Spatial IO and Region Exchange](spatial_io.md)

## Check in order

| Symptom | Check |
| - | - |
| Terminal offline | Power, connections, channels, loaded chunks |
| Import stops | Source side, filter, free bytes and types, storage access |
| Crafting waits | Exact pending product, machine power, output side, same-network return |
| Wireless fails | Pairing slot, battery, bound access point, range and dimension |
| IO port stalls | Transfer direction, partitions, full destination, completion mode |
