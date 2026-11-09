# AE2S 1.1.0 GUI 覆盖清单

本目录包含 **84 套操作教程、78 种原生界面类型**。共用实现基类 `GuiUpgradeable`、`GuiSpecialExportBus`、`GuiSpecialStorageBus` 不作为玩家独立入口重复计数。多个设备共用同一 Java 界面时，通过实际宿主和当前编码模式匹配教程。

每套定义都用于 GUI 独立演示、W 实机引导、独立 Markdown 页面和时间轴动画。所有页面加入教程索引，并关联原生物品。控件或槽位只有在当前原生界面可用时才显示高亮；不会伪造已禁用或不存在的配置项。

覆盖数量表示已编写并接入的教程范围。运行验收范围由 [安装包验收](../LEGACY-VERIFICATION.md) 单独记录，不能把资源存在当作已对每种操作跑完真实生产任务。

## 基础入门

| 教程 | 原生界面 | 上下文／入口 |
| --- | --- | --- |
| ME 驱动器：安装存储 | `GuiDrive` | `ae2:drive`, `ae2:item_storage_cell_1k`, `ae2:item_storage_cell_64k` |
| ME 终端：检索与存取 | `GuiMEStorage` | `ae2:terminal`, `ae2:crafting_terminal` |
| 存储元件工作台：配置分区 | `GuiCellWorkbench` | `ae2:cell_workbench` |
| ME 箱子：单元存储 | `GuiMEChest` | `ae2:chest` |
| 陨石箱 | `GuiSkyChest` | `ae2:sky_stone_chest`, `ae2:smooth_sky_stone_chest` |
| 振动仓：燃料发电 | `GuiVibrationChamber` | `ae2:vibration_chamber` |
| 存储元件终端：检查元件 | `GuiCellTerminal` | `ae2:cell_terminal`, `ae2:wireless_cell_terminal` |
| 便携物品存储元件 | `GuiMEStorage` | `item:portable_item_cell_`；`ae2:portable_item_cell_1k`, `ae2:portable_item_cell_4k` |
| 便携流体存储元件 | `GuiMEStorage` | `item:portable_fluid_cell_`；`ae2:portable_fluid_cell_1k` |
| 便携存储元件工作台 | `GuiCellWorkbench` | `PortableCellWorkbenchGuiHost`；`ae2:portable_cell_workbench` |
| 存储元件限制 | `GuiCellRestriction` | `ae2:cell_workbench` |
| 便携元件拾取过滤 | `GuiPortableCellPickupFilter` | `ae2:portable_item_cell_1k` |
| 石英切割刀：命名 | `GuiQuartzKnife` | `ae2:certus_quartz_cutting_knife`, `ae2:nether_quartz_cutting_knife` |
| 终端设置 | `GuiTerminalSettings` | `ae2:terminal`, `ae2:crafting_terminal`, `ae2:wireless_terminal` |
| 选择资源类型 | `GuiKeyTypeSelection` | `ae2:terminal`, `ae2:storage_bus` |
| 数值输入快捷设置 | `GuiNumberEntryButtonSettings` | `ae2:crafting_terminal`, `ae2:interface` |
## 存储与自动化

| 教程 | 原生界面 | 上下文／入口 |
| --- | --- | --- |
| ME 接口：备货与存入 | `GuiInterface` | `ae2:interface`, `ae2:cable_interface` |
| ME IO 端口：转移元件 | `GuiIOPort` | `ae2:io_port` |
| 物质聚合器：物质球与奇点 | `GuiCondenser` | `ae2:condenser`, `ae2:singularity`, `ae2:matter_ball` |
| ME 原料缓存器 | `GuiIngredientBuffer` | `ae2:ingredient_buffer` |
| ME 装罐器：容器转移 | `GuiCaner` | `ae2:caner` |
| 输入总线 | `GuiIOBus` | `ImportBusPart`；`ae2:import_bus` |
| 输出总线 | `GuiIOBus` | `ExportBusPart`；`ae2:export_bus` |
| 存储总线 | `GuiStorageBus` | `ae2:storage_bus` |
| 精确输出总线 | `GuiSpecialPreciseExportBus` | `ae2:precise_export_bus` |
| 阈值输出总线 | `GuiThresholdExportBus` | `ae2:threshold_export_bus` |
| 库存输出总线 | `GuiStockExportBus` | `ae2:stock_export_bus` |
| 输入输出总线 | `GuiImportExportBus` | `ae2:import_export_bus` |
| 高级 IO 总线 | `GuiAdvancedIOBus` | `ae2:advanced_io_bus` |
| 精确存储总线 | `GuiPreciseStorageBus` | `ae2:precise_storage_bus` |
| 矿词输出总线 | `GuiODFilterBus` | `ae2:od_export_bus` |
| 矿词存储总线 | `GuiODStorageBus` | `ae2:od_storage_bus` |
| 模组输出总线 | `GuiModFilterBus` | `ae2:mod_export_bus` |
| 模组存储总线 | `GuiModStorageBus` | `ae2:mod_storage_bus` |
| 存储监控发信器 | `GuiStorageLevelEmitter` | `ae2:level_emitter` |
| 能量监控发信器 | `GuiEnergyLevelEmitter` | `ae2:energy_level_emitter` |
| 阈值发信器 | `GuiThresholdLevelEmitter` | `ae2:threshold_level_emitter` |
| 成形面板 | `GuiFormationPlane` | `ae2:formation_plane` |
| 破坏面板 | `GuiAnnihilationPlane` | `ae2:annihilation_plane` |
| 设置备货数量 | `GuiSetStockAmount` | `ae2:interface`, `ae2:stock_export_bus` |
| 虚空存储元件：处理模式 | `GuiVoidCell` | `ae2:void_storage_cell` |
| 便携虚空存储元件 | `GuiPortableVoidCell` | `ae2:portable_void_cell` |
| 存储优先级 | `GuiPriority` | `ae2:storage_bus`, `ae2:drive`, `ae2:interface`, `ae2:pattern_provider` |
| 优先级调整器 | `GuiPriorityTuner` | `ae2:priority_tuner` |
| 配置修改器：数量运算 | `GuiConfigModifier` | `ae2:config_modifier` |
| 机器输出面 | `GuiOutputSides` | `ae2:inscriber`, `ae2:crystal_assembler`, `ae2:molecular_assembler` |
| 机器工作间隔 | `GuiWorkInterval` | `ae2:advanced_io_bus`, `ae2:import_export_bus`, `ae2:stock_export_bus` |
## 自动合成

| 教程 | 原生界面 | 上下文／入口 |
| --- | --- | --- |
| 压印器：压印硅板 | `GuiInscriber` | `ae2:inscriber`, `ae2:silicon_press` |
| 样板终端：合成样板 | `GuiPatternEncodingTerm` | `ae2:pattern_encoding_terminal`, `ae2:crafting_pattern`, `ae2:blank_pattern` |
| 样板终端：处理样板 | `GuiPatternEncodingTerm` | `ae2:pattern_encoding_terminal`, `ae2:processing_pattern`, `ae2:blank_pattern` |
| 样板供应器：安装与回网 | `GuiPatternProvider` | `ae2:pattern_provider`, `ae2:cable_pattern_provider` |
| 水晶装配器 | `GuiCrystalAssembler` | `ae2:crystal_assembler` |
| 分子装配室 | `GuiMolecularAssembler` | `ae2:molecular_assembler` |
| 合成终端：网格操作 | `GuiCraftingTerm` | `ae2:crafting_terminal`, `ae2:wireless_crafting_terminal` |
| 样板管理终端 | `GuiPatternAccessTerm` | `ae2:pattern_access_terminal`, `ae2:wireless_pattern_access_terminal` |
| 样板编码管理终端 | `GuiPEATerm` | `ae2:pattern_encoding_access_terminal`, `ae2:wireless_pattern_encoding_access_terminal` |
| 请求器：维持合成库存 | `GuiRequester` | `ae2:requester` |
| 请求终端 | `GuiRequesterTerm` | `ae2:requester_terminal`, `ae2:wireless_requester_terminal` |
| 发起合成：数量 | `GuiCraftAmount` | `ae2:crafting_terminal`, `ae2:pattern_encoding_terminal` |
| 发起合成：计划确认 | `GuiCraftConfirm` | `ae2:crafting_terminal` |
| 合成 CPU 选择 | `GuiCraftConfirmCpuList` | `ae2:crafting_terminal`, `ae2:1k_crafting_storage` |
| 合成 CPU：运行任务 | `GuiCraftingCPU` | `ae2:1k_crafting_storage`, `ae2:crafting_monitor`, `ae2:crafting_terminal` |
| 合成状态：全部 CPU | `GuiCraftingStatus` | `ae2:1k_crafting_storage`, `ae2:crafting_monitor`, `ae2:crafting_terminal` |
| 合成依赖树 | `GuiCraftingTree` | `ae2:crafting_terminal` |
| 合成失败详情 | `GuiCraftError` | `ae2:crafting_terminal` |
| 合成任务优先级 | `GuiCraftingTaskPriority` | `ae2:crafting_terminal` |
| 重命名样板条目 | `GuiPatternItemRenamer` | `ae2:network_tool`, `ae2:pattern_encoding_terminal` |
| 样板修改器：批量编辑 | `GuiPatternModifier` | `ae2:pattern_modifier` |
| 配方导入优先级 | `GuiPatternImportPrioritySettings` | `ae2:pattern_encoding_terminal`, `ae2:pattern_encoding_access_terminal` |
| 处理样板数量 | `GuiSetProcessingPatternAmount` | `ae2:pattern_encoding_terminal`, `ae2:processing_pattern` |
| 查看合成样板 | `GuiCraftingPattern` | `ae2:crafting_pattern` |
| 查看处理样板 | `GuiProcessingPattern` | `ae2:processing_pattern` |
## 网络工程

| 教程 | 原生界面 | 上下文／入口 |
| --- | --- | --- |
| 无线终端 | `GuiMEStorage` | `WirelessTerminalGuiHost`；`ae2:wireless_terminal`, `ae2:wireless_universal_terminal` |
| 无线访问点：配对设备 | `GuiWirelessAccessPoint` | `ae2:wireless_access_point`, `ae2:wireless_terminal`, `ae2:wireless_universal_terminal` |
| 量子桥：两端配对 | `GuiQNB` | `ae2:quantum_link`, `ae2:quantum_ring`, `ae2:quantum_entangled_singularity` |
| 空间 IO 端口：传送区域 | `GuiSpatialIOPort` | `ae2:spatial_io_port`, `ae2:spatial_storage_cell_2`, `ae2:spatial_storage_cell_16`, `ae2:spatial_storage_cell_128` |
| 空间锚：区块加载 | `GuiSpatialAnchor` | `ae2:spatial_anchor` |
| 网络状态：电力与频道 | `GuiNetworkStatus` | `ae2:controller`, `ae2:network_tool` |
| 网络工具：升级与诊断 | `GuiNetworkTool` | `ae2:network_tool` |
| 网络分析仪 | `GuiNetworkAnalyser` | `ae2:network_analyser` |
| 运算分析仪 | `GuiTickAnalyser` | `ae2:tick_analyser` |
| 高级内存卡：P2P 管理 | `GuiAdvancedMemoryCard` | `ae2:advanced_memory_card`, `ae2:me_p2p_tunnel` |
| 无线磁铁设置 | `GuiWirelessMagnet` | `ae2:wireless_terminal`, `ae2:wireless_universal_terminal` |
| 重命名网络设备 | `GuiRenamer` | `ae2:network_tool`, `ae2:pattern_encoding_terminal` |

## 同一界面的上下文

- `GuiIOBus`：普通输入与输出总线根据真实宿主区分，精确／高级变种使用各自界面教程。
- `GuiMEStorage`：方块终端、无线终端、便携物品元件和便携流体元件分别匹配；输入搜索时保留 W。
- `GuiCellWorkbench`：放置的工作台与便携工作台分别说明；未插元件时，配置槽保持原生禁用状态。
- 样板编码终端：合成与处理模式分别匹配，样板编码管理终端有自己的教程。
- 方块／部件供应器和接口、无线／放置终端，在控件相同的场合复用相应操作教程。
- 通用无线终端使用原生类型选择器，随后按所选终端界面匹配教程。

## 可复现检查

`tools/gui_catalog.py` 保存原创操作文案。`tools/gui_layouts.py` 读取 dependency-lock.json 固定的 AE2S 1.1.0 生产 jar，扫描实际界面继承关系并解析原生 JSON 布局。`ponder/gui/coverage.json` 记录实际 jar SHA-256、界面清单和教程映射。

```bash
python3 tools/generate-guis.py
python3 tools/generate-structures.py
python3 tools/generate-guides.py
python3 tools/verify-assets.py
```

升级 AE2S 后如果出现尚未编写教程的新原生界面，生成器会报错。每次运行验收还检查物品注册、纹理解码、样式加载、双语文案、演示跳转，以及选定原生机器／部件／物品窗口的 W 与输入焦点行为。
