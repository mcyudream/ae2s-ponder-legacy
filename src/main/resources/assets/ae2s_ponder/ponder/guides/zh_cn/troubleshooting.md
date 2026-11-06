---
id: ae2s_ponder:troubleshooting
title: 教程索引与故障排查
item_ids: [ae2:network_tool]
presentation: guide
---
# 教程索引与故障排查

本教程面向 Minecraft 1.12.2 / Cleanroom 的 AE2S / Supergiant 1.1.0，资源配方与频道设置可被整合包改动。

## 基础入门

- [搭建第一个 ME 网络](first_network.md)
- [存储元件与分区](storage_cells.md)
- [频道与线缆容量](channels.md)
- [赛特斯石英充能](charger.md)
- [石英生长与福鲁伊克斯材料](quartz_growth.md)
- [监视器与网络诊断工具](monitors_tools.md)

## 存储与自动化

- [接入外部容器](storage_bus.md)
- [物品输入与输出](import_export.md)
- [接口备货与回网](interfaces.md)
- [用存储监控发信器控制库存](level_stocking.md)
- [用 IO 端口转移存储元件内容](cell_io.md)
- [成型面板与湮灭面板](planes.md)
- [总线过滤与升级卡](upgrades.md)
- [流体存储与储罐自动化](fluid_storage.md)
- [物质聚合器与物质转换](condenser.md)

## 自动合成

- [使用样板供应器自动合成](autocrafting.md)
- [处理样板与产物回收](processing.md)
- [压印器与处理器生产](processors.md)
- [合成 CPU 容量与并行](crafting_cpu.md)

## 网络工程

- [连接 ME P2P 隧道](p2p.md)
- [独立子网络与共享电力](subnetworks.md)
- [无线终端配对与供能](wireless.md)
- [量子网络桥](quantum_bridge.md)
- [空间 IO 与区域交换](spatial_io.md)

## 按顺序排查

| 症状 | 检查项目 |
| - | - |
| 终端离线 | 电力、连接、频道、区块加载 |
| 输入停止 | 源容器侧面、过滤、字节与类型空间、访问权限 |
| 合成等待 | 准确的待回网产物、机器供电、输出面、是否回到同一网络 |
| 无线失效 | 配对槽、电量、绑定访问点、距离与维度 |
| IO 端口停滞 | 转移方向、分区、目标已满、完成模式 |
