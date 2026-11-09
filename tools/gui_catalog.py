"""Authored AE2S 1.1.0 GUI operations. Layouts are resolved separately from the pinned jar.

One lesson per distinct operation; wireless/block/part aliases share a lesson when controls agree.
Strings are original explanations. No upstream artwork is copied into the addon.
"""
CATALOG = []


def S(target, label, en, zh, item='', count=1, sample='', wait=None):
    return dict(target=target, label=label.split('|'), text=(en, zh), item=item,
                count=count, sample=sample, wait=wait)


def add(id, title, cls, style, components, category, scene, steps, **extra):
    CATALOG.append(dict(id=id, title=title.split('|'), cls=cls, style=style,
                        components=components.split(), category=category, scene=scene, steps=steps, **extra))


# Storage and material handling.
add('me_chest', 'ME Chest: local storage|ME 箱子：单元存储', 'GuiMEChest', 'me_chest', 'chest', 'basics', 'storage_cells', [
    S('slot.STORAGE_CELL.0', 'Storage cell|存储元件', 'Install one compatible cell. The ME Chest has a cell slot, rather than the ten-cell capacity of a drive.', '安装一块兼容的存储元件。ME 箱子只有一个元件槽，与驱动器的十槽不同。', 'ae2:item_storage_cell_1k'),
    S('view.body', 'Power and access|供电与访问', 'Supply power, then use the storage access button to browse the installed cell. Check access restrictions if insertion fails.', '供能后使用存储访问入口查看元件内容；存入失败时检查元件限制。'),
    S('slot.STORAGE_CELL.0', 'Keep the contents|保管数据', 'The contents remain on the removed cell. Before replacing it, finish any active transfer and keep the original cell safe.', '取出的元件仍保存原有数据。更换前先结束传输，并妥善保留旧元件。')])
add('sky_chest', 'Sky Stone Chest|陨石箱', 'GuiSkyChest', 'sky_chest', 'sky_stone_chest smooth_sky_stone_chest', 'basics', 'storage_bus', [
    S('slot.STORAGE.0', 'Chest inventory|箱内库存', 'These are real chest slots. Place and retrieve items here; this chest does not require an ME network.', '这里是普通实物槽位，可直接存取物品，陨石箱不需要 ME 网络。', 'minecraft:iron_ingot', 32),
    S('slot.PLAYER_INVENTORY.0', 'Transfer items|转移物品', 'Move items between the chest and your inventory. Demonstration items are independent of the real inventory.', '在箱子与背包之间转移物品，演示中的物品不会改变真实库存。'),
    S('slot.STORAGE.0', 'Expose through a Storage Bus|用存储总线接入', 'Attach a Storage Bus to expose this inventory to ME storage. Configure access and priority on the bus itself.', '接上存储总线可将箱内物品纳入 ME 存储，访问权限和优先级在总线中设置。')])
add('io_port', 'ME IO Port: transfer cells|ME IO 端口：转移元件', 'GuiIOPort', 'io_port', 'io_port', 'automation', 'cell_io', [
    S('slot.MACHINE_INPUT.0', 'Input cells|待处理元件', 'Insert storage cells to be processed. Their contents, not ordinary loose items, are transferred by this machine.', '放入待处理的存储元件。机器转移的是元件内容，不是把散装物品直接投入此槽。', 'ae2:item_storage_cell_1k'),
    S('widget.operationMode', 'Transfer direction|转移方向', 'Choose cell-to-network or network-to-cell before starting. Check that the destination accepts the stored resource types.', '开始前选择元件到网络或网络到元件，确认目标支持对应资源类型。'),
    S('slot.MACHINE_OUTPUT.0', 'Completed cells|已处理元件', 'Completed cells move to the output side. The selected completion rule decides when a cell counts as finished.', '完成的元件移动到输出侧，何时算作完成由所选完成规则决定。', 'ae2:item_storage_cell_1k'),
    S('widget.upgrades', 'Throughput and stalls|吞吐与停滞', 'Use supported upgrades after testing one cell. A full network, restrictive partition or wrong direction can stop transfers.', '先测试一块元件，再安装支持的升级卡。网络已满、分区限制或方向选错都会阻止转移。')])
add('condenser', 'Condenser: matter and singularities|物质聚合器：物质球与奇点', 'GuiCondenser', 'condenser', 'condenser singularity matter_ball', 'automation', 'condenser', [
    S('slot.MACHINE_INPUT.0', 'Consumed resources|消耗的资源', 'Only feed resources you intend to consume. This machine converts supplied resources into accumulated matter.', '只投入确定要消耗的资源，物质聚合器会将输入转换为累计物质。', 'minecraft:cobblestone', 64),
    S('widget.mode', 'Output mode|产出模式', 'Choose deletion, Matter Ball or Singularity mode as appropriate. Read the displayed requirement before feeding valuables.', '按需选择销毁、物质球或奇点模式，投放贵重物品前核对显示的需求量。'),
    S('slot.STORAGE_CELL.0', 'Matter capacity|物质容量', 'Install a compatible storage component when the chosen output requires accumulated capacity.', '所选产出需要累计容量时，在此安装兼容的存储组件。', 'ae2:cell_component_64k'),
    S('slot.MACHINE_OUTPUT.0', 'Collect the product|提取产物', 'Keep the output clear. A Singularity still needs the actual entangling recipe before it can pair two quantum bridges.', '为产物留出空间。奇点还需通过实际缠绕配方，才能用于配对两端量子桥。', 'ae2:singularity')])
add('vibration_chamber', 'Vibration Chamber: generate power|振动仓：燃料发电', 'GuiVibrationChamber', 'vibration_chamber', 'vibration_chamber', 'basics', 'first_network', [
    S('slot.MACHINE_INPUT.0', 'Fuel|燃料', 'Insert a valid furnace fuel. Fuel is consumed to supply AE power to the connected network.', '放入有效的熔炉燃料，燃料被消耗后为相连网络提供 AE 能量。', 'minecraft:coal', 16),
    S('widget.generationRateBar', 'Generation|发电状态', 'Watch generation and demand. An Energy Cell stores surplus energy; it does not generate energy by itself.', '观察发电量与需求，能量元件只能储存多余能量，本身不会发电。'),
    S('widget.upgrades', 'Upgrades and supply|升级与供给', 'Use only upgrades supported by this machine. Automate fuel supply separately and test that the network stays powered under load.', '只安装机器支持的升级卡。单独布置燃料供给，并在网络负载下检查供电是否稳定。')])
add('crystal_assembler', 'Crystal Assembler|水晶装配器', 'GuiCrystalAssembler', 'crystal_assembler', 'crystal_assembler', 'crafting', 'quartz_growth', [
    S('slot.MACHINE_INPUT.0', 'Recipe input|配方输入', 'Look up the installed Crystal Assembler recipe, then supply its input here. Do not assume a modern AE2 recipe applies unchanged.', '先查询当前水晶装配器配方，再向此槽供料，不直接套用现代版 AE2 的配方。', 'ae2:certus_quartz_crystal'),
    S('slot.STORAGE.0', 'Supporting inventory|辅助库存', 'Check the recipe and the machine tooltip for the role of these supporting slots before automating them.', '自动化前，按配方与机器提示确认这些辅助槽的用途。'),
    S('widget.progressBar', 'Powered processing|供能加工', 'Connect power and watch progress. When processing stalls, check the complete recipe, available power and output space.', '连接电力并观察进度，停滞时检查完整配方、供电与输出空间。'),
    S('slot.MACHINE_OUTPUT.0', 'Return products|产物回网', 'Extract only the intended product and return it to the requesting network when using a processing pattern.', '提取目标产物；使用处理样板时，将产物送回发起任务的网络。', 'ae2:charged_certus_quartz_crystal')])
add('ingredient_buffer', 'Ingredient Buffer|ME 原料缓存器', 'GuiIngredientBuffer', 'ingredient_buffer', 'ingredient_buffer', 'automation', 'processing', [
    S('slot.STORAGE.0', 'Ingredient inventory|原料库存', 'Use the buffer as an intermediate inventory between delivery and the processing machine.', '将原料缓存器作为原料投送与加工机器之间的中转库存。', 'minecraft:iron_ore', 8),
    S('slot.STORAGE.1', 'Keep batches traceable|核对批量', 'Test one batch and verify which adjacent side inserts and extracts. A buffer does not turn an incorrect pattern into a valid recipe.', '用一批原料核对邻接侧面的存取方式；缓存器不能修正错误的样板配方。'),
    S('slot.STORAGE.0', 'Return exact outputs|准确回收产物', 'Keep product return separate from ingredient delivery so the crafting CPU receives the expected output.', '将产物回收与原料投送分开，让合成 CPU 能收到预期产物。')])
add('caner', 'ME Caner: container transfer|ME 装罐器：容器转移', 'GuiCaner', 'caner', 'caner', 'automation', 'fluid_storage', [
    S('slot.CANER_CONTAINER.0', 'Container|容器', 'Place a compatible fillable or filled container here. Check its supported resource and capacity.', '放入兼容的空容器或已填充容器，检查它支持的资源与容量。', 'minecraft:bucket'),
    S('slot.CANER_CONTENT.0', 'Contents|容器内容', 'Inspect the resource entry handled by the Caner. Choose the intended fill or empty operation using its native controls.', '查看装罐器处理的资源条目，并通过原生控件选择填充或清空操作。'),
    S('slot.CANER_CONTAINER.0', 'Verify the direction|核对方向', 'Test one container before connecting automation. Ensure both the container destination and resource destination have space.', '连接自动化前先测试一个容器，确认容器去向和资源去向都有可用空间。')])
add('molecular_assembler', 'Molecular Assembler|分子装配室', 'GuiMolecularAssembler', 'molecular_assembler', 'molecular_assembler', 'crafting', 'autocrafting', [
    S('slot.ENCODED_PATTERN.0', 'Crafting patterns|合成样板', 'Use crafting patterns for crafting-grid recipes. Processing patterns belong to machines that perform the described process.', '合成网格配方应使用合成样板，处理样板用于执行对应加工过程的机器。', 'ae2:crafting_pattern'),
    S('widget.upgrades', 'Acceleration|加速升级', 'Install supported acceleration upgrades after a single recipe works. Parallel demand also depends on the available crafting CPUs and ingredient supply.', '单个配方跑通后再安装支持的加速升级，并行需求也受合成 CPU 与原料供应限制。'),
    S('slot.ENCODED_PATTERN.0', 'Provider connection|供应器连接', 'A neighboring Pattern Provider can send crafting work to an assembler. Check adjacency and network power when a job waits.', '相邻样板供应器可向装配室发送合成任务，任务等待时检查邻接关系和供电。'),
    S('widget.openPriority', 'Duplicate recipes|重复配方', 'If several devices offer the same recipe, inspect their priority and availability before scaling the setup.', '多个设备提供同一配方时，扩建前先核对它们的优先级与可用状态。')])

# Standard and AE2S-specific buses. Each variant explains its own matching/stock behavior.
for id, title, cls, scene, explanation, zh in [
    ('import_bus','Import Bus|输入总线','GuiIOBus','import_export','Pull items from the adjacent inventory into ME storage. The target is the inventory on the bus face.','把相邻容器的物品拉入 ME 存储，目标是总线安装面朝向的容器。'),
    ('export_bus','Export Bus|输出总线','GuiIOBus','import_export','Select items to send from ME storage into the adjacent inventory. An empty filter does not specify a desired item.','选择从 ME 网络送往相邻容器的物品，空过滤槽不代表已经指定目标物品。'),
    ('storage_bus','Storage Bus|存储总线','GuiStorageBus','storage_bus','Expose an external inventory as ME storage. Items remain in that external inventory until moved by an actual operation.','把外部容器公开为 ME 存储，物品仍留在外部容器内，直到发生实际存取。'),
    ('precise_export_bus','Precise Export Bus|精确输出总线','GuiSpecialPreciseExportBus','import_export','Select the exact matching resource variants. Verify item identity, NBT-sensitive settings and the receiving inventory.','配置需要精确匹配的资源变种，核对物品身份、NBT 相关设置及接收容器。'),
    ('threshold_export_bus','Threshold Export Bus|阈值输出总线','GuiThresholdExportBus','level_stocking','Configure the desired resource and its threshold behavior. Test stock just below and above the threshold before enabling a large batch.','配置目标资源及其阈值行为，正式投料前，用略低于和略高于阈值的库存分别测试。'),
    ('stock_export_bus','Stock Export Bus|库存输出总线','GuiStockExportBus','level_stocking','Set target inventory amounts rather than treating the entries as supplied items. The bus attempts to maintain the requested local stock.','设置目标容器应保有的数量，配置项不是已提供的实物；总线会尝试维持指定本地库存。'),
    ('import_export_bus','Import/Export Bus|输入输出总线','GuiImportExportBus','import_export','Configure the direction and item entries for the combined bus. Verify which items are exported and which can return to storage.','设置组合总线的方向和物品条目，核对哪些物品应输出，哪些允许回到存储。'),
    ('advanced_io_bus','Advanced IO Bus|高级 IO 总线','GuiAdvancedIOBus','level_stocking','Choose stock regulation when the attached inventory should retain target amounts; inspect the supported scheduling and crafting options.','需要相邻容器保留目标数量时启用库存调节，并检查机器支持的调度与合成选项。'),
    ('precise_storage_bus','Precise Storage Bus|精确存储总线','GuiPreciseStorageBus','storage_bus','Specify exact resource filters and inspect the access permissions of the attached inventory.','设置精确资源过滤，并检查所连接容器的存取权限。')]:
    add(id,title,cls,id,id,'automation',scene,[
        S('slot.CONFIG.0','Resource filter|资源过滤',explanation,zh,'minecraft:iron_ingot'),
        S('widget.verticalToolbar','Operation settings|运行设置','Read the supported redstone, matching, scheduling and access settings. Availability depends on this bus and installed cards.','检查当前总线支持的红石、匹配、调度与访问设置，可用项取决于总线类型和升级卡。'),
        S('widget.upgrades','Upgrade cards|升级卡','Install only compatible cards. Extra filter slots can remain disabled until the required capacity upgrade is present.','只安装兼容升级卡，部分过滤槽会在安装容量升级前保持禁用。'),
        S('slot.CONFIG.0','Test one transfer|测试一次传输','Use a small amount to confirm direction, free destination space and network power. Avoid a direct import/export loop on the same inventory.','先用少量物品确认方向、目标剩余空间和供电，避免对同一容器构成直接输入输出循环。')],
        host='ImportBusPart' if id=='import_bus' else 'ExportBusPart' if id=='export_bus' else '')
for id,title,cls,field in [
    ('od_export_bus','Ore-Dictionary Export Bus|矿词输出总线','GuiODFilterBus','whiteExpression'),
    ('od_storage_bus','Ore-Dictionary Storage Bus|矿词存储总线','GuiODStorageBus','whiteExpression'),
    ('mod_export_bus','Mod Export Bus|模组输出总线','GuiModFilterBus','modExpression'),
    ('mod_storage_bus','Mod Storage Bus|模组存储总线','GuiModStorageBus','modExpression')]:
    ore=id.startswith('od_')
    add(id,title,cls,id,id,'automation','storage_bus' if 'storage' in id else 'import_export',[
        S('widget.'+field,'Matching expression|匹配表达式','Enter an Ore Dictionary expression and inspect the matching result before connecting valuable storage.' if ore else 'Enter the intended mod filter using this field. Verify that the selected mod matches the resources you intend to expose or export.',
          '输入矿物词典表达式，接入贵重库存前先核对匹配结果。' if ore else '在此填写目标模组过滤条件，核对所选模组与要公开或输出的资源一致。',sample='ingotIron' if ore else 'minecraft'),
        S('widget.blackExpression' if ore else 'widget.modExpression','Exclusions|排除条件','Use the blacklist to exclude unwanted matches; a broad whitelist can otherwise match many ore-dictionary equivalents.' if ore else 'Keep the filter narrow. Selecting a mod is broader than selecting one specific item.',
          '使用黑名单排除不需要的匹配，宽泛的白名单可能包含多个矿词等价物。' if ore else '控制过滤范围，选择整个模组比指定单个物品更宽泛。'),
        S('widget.verticalToolbar','Access and control|访问与控制','Review the bus settings and test one resource against the adjacent inventory before enabling automation.','检查总线设置，并对相邻容器测试一种资源，再启用自动化。')])

for id,title,cls,style,components,field,en,zh in [
    ('level_emitter','Storage Level Emitter|存储监控发信器','GuiStorageLevelEmitter','level_emitter','level_emitter','level','Select the monitored resource and set a stock threshold.','选择要监控的资源并设置库存阈值。'),
    ('energy_emitter','Energy Level Emitter|能量监控发信器','GuiEnergyLevelEmitter','energy_level_emitter','energy_level_emitter','level','Set the network energy threshold using the displayed power unit.','按界面显示的能量单位设置网络能量阈值。'),
    ('threshold_emitter','Threshold Level Emitter|阈值发信器','GuiThresholdLevelEmitter','threshold_level_emitter','threshold_level_emitter','upperLevel','Configure the upper and lower thresholds. Test both boundaries so the controlled machine does not rapidly oscillate.','配置上下阈值，分别测试两个边界，避免被控制机器频繁启停。')]:
    steps=[S('widget.'+field,'Threshold|阈值',en,zh,sample='64'),
           S('widget.verticalToolbar','Signal condition|发信条件','Choose the intended signal mode and test the receiving device. The emitter supplies a redstone signal; it does not move or craft resources.','选择正确的发信模式并测试接收设备；发信器只提供红石信号，不会自行搬运或合成资源。')]
    if id!='energy_emitter':steps.insert(0,S('slot.CONFIG.0','Observed resource|监控资源','Choose the resource to count; the ghost entry is a filter, not stored inventory.','选择要统计的资源，幽灵条目是过滤标记，不是实物库存。','minecraft:iron_ingot'))
    if id=='threshold_emitter':steps.insert(2,S('widget.lowerLevel','Lower threshold|下阈值','Set a lower threshold below the upper threshold, then test replenishment and consumption.','将下阈值设置为小于上阈值，再测试补货和消耗过程。',sample='16'))
    add(id,title,cls,style,components,'automation','level_stocking',steps)

for id,title,cls,en,zh in [
    ('formation_plane','Formation Plane|成形面板','GuiFormationPlane','Configure which resources may be placed into the world at the panel face. Leave the target space clear.','配置允许在面板朝向的世界位置放置的资源，并保持目标空间可用。'),
    ('annihilation_plane','Annihilation Plane|破坏面板','GuiAnnihilationPlane','Configure which world drops may be collected at the panel face. Test the exact block and tool behavior before using a valuable structure.','配置面板朝向处允许收集的世界掉落物；用于贵重结构前先测试具体方块和工具行为。')]:
    add(id,title,cls,id,id,'automation','planes',[
        S('slot.CONFIG.0','Placement / collection filter|放置／收集过滤',en,zh,'minecraft:cobblestone'),
        S('widget.verticalToolbar','Operation mode|运行模式','Check matching, redstone and access settings. These control what the plane is allowed to do.','核对匹配、红石与访问设置，它们决定面板允许执行的操作。'),
        S('widget.upgrades','Capacity and throughput|容量与吞吐','Use supported cards and keep network storage available. Test a single block before extending the working area.','使用支持的升级卡并保持网络存储可用，扩大工作范围前先测试一个方块。')])

# Terminals and the complete crafting-request sequence.
add('crafting_terminal', 'Crafting Terminal: grid operations|合成终端：网格操作', 'GuiCraftingTerm', 'terminals/crafting_terminal',
    'crafting_terminal wireless_crafting_terminal', 'crafting', 'autocrafting', [
    S('widget.search','Find ingredients|查找原料','Search the network stock. Search focus keeps W available for text entry.','检索网络库存；搜索框获得焦点时，W 保持用于文字输入。',sample='iron'),
    S('slot.CRAFTING_GRID.0','Crafting grid|合成网格','Arrange the ingredients for a valid crafting recipe. This is the manual crafting grid, distinct from encoding a reusable pattern.','按有效配方排列原料。这里是手动合成网格，与编码可重复使用的样板不同。','minecraft:iron_ingot'),
    S('slot.CRAFTING_RESULT.0','Take the result|取出产物','Check the result before taking it. When recipes conflict, use the available recipe-selection control.','取出前核对产物；存在配方冲突时，使用界面提供的配方选择控件。','minecraft:iron_block'),
    S('widget.clearCraftingGrid','Clear the grid|清理网格','Use the clear controls to return ingredients to storage or your inventory. Rotation and balancing controls help arrange repeated recipes.','使用清理按钮将原料送回存储或背包；旋转、均分按钮可辅助整理重复配方。')])
add('pattern_access', 'Pattern Access Terminal|样板管理终端', 'GuiPatternAccessTerm', 'terminals/pattern_access_terminal',
    'pattern_access_terminal wireless_pattern_access_terminal', 'crafting', 'autocrafting', [
    S('widget.search','Provider search|供应器搜索','Find a provider by its name. Give providers clear names so similar machines can be distinguished.','按名称查找供应器，建议为供应器命名，以区分用途相近的机器。',sample='smelting'),
    S('widget.inputSearch','Ingredient search|输入搜索','Filter the displayed patterns by their inputs rather than only searching the provider name.','可按样板输入过滤显示结果，不必只搜索供应器名称。',sample='iron'),
    S('widget.outputSearch','Product search|产出搜索','Use output search to locate the recipe that produces a missing item. Inspect its provider before replacing a pattern.','按产物查找缺少物品的配方，替换样板前先确认所属供应器。'),
    S('view.body','Manage installed patterns|管理已安装样板','The list represents actual network providers. Move or edit patterns deliberately; removing a required recipe can affect later crafting requests.','列表对应网络中的实际供应器；移动或编辑样板前确认用途，删除配方会影响后续合成请求。')])
add('pea_terminal', 'Pattern Encoding Access Terminal|样板编码管理终端', 'GuiPEATerm', 'terminals/pattern_encoding_access_terminal',
    'pattern_encoding_access_terminal wireless_pattern_encoding_access_terminal', 'crafting', 'autocrafting', [
    S('widget.search','Find the destination|查找目标供应器','Locate a destination provider in the access list before uploading a new pattern.','先在管理列表中找到目标供应器，再上传新的样板。',sample='processor'),
    S('widget.inputSearch','Recipe input filter|配方输入过滤','Combine provider, input and output searches to narrow a large network to the relevant recipes.','组合供应器、输入与输出搜索，在大型网络中缩小配方范围。'),
    S('widget.modeTabButton0','Encoding mode|编码模式','Choose crafting or processing as required. Reusable machine tools must not be listed as consumed processing ingredients.','按需选择合成或处理模式，处理样板不应把机器内重复使用的工具列为消耗原料。'),
    S('widget.encodePattern','Encode and verify|编码并核对','Verify the blank pattern, recipe, amounts and output before encoding. Use the upload control only after confirming the destination.','编码前核对空白样板、配方、数量与产物；确认目标供应器后再使用上传控件。')])
add('cell_terminal', 'Cell Terminal: inspect cells|存储元件终端：检查元件', 'GuiCellTerminal', 'cell_terminal',
    'cell_terminal wireless_cell_terminal', 'basics', 'storage_cells', [
    S('widget.search','Find a cell|查找存储元件','Search the network cell view to locate the storage cell you intend to inspect.','在网络元件视图中搜索，找到需要检查的存储元件。',sample='1k'),
    S('view.body','Cell overview|元件概况','Inspect the displayed cell and usage information before moving or editing it. This view can represent many installed cells.','移动或编辑元件前核对列表中的元件及使用信息，这个视图可以包含多块已安装元件。'),
    S('widget.verticalToolbar','Cell operations|元件操作','Use the native view and cell controls for the selected entry. A partition filter and a real stored item are different things.','针对所选条目使用原生查看与元件操作，注意分区过滤标记和真实库存的区别。'),
    S('view.body','Confirm storage remains available|确认存储可用','After changing a cell, verify the terminal still finds its resources and the network has capacity for new inputs.','修改后检查终端仍能找到资源，并确认网络仍有接收新物品的容量。')])
add('requester', 'Requester: maintain crafted stock|请求器：维持合成库存', 'GuiRequester', 'requester', 'requester', 'crafting', 'crafting_cpu', [
    S('view.body','Requested resources|请求资源','Add the resource and amount that should be maintained. Distinguish the requested target from items already in storage.','添加希望维持库存的资源与数量，区分目标数量与已经存在的库存。',sample='Iron ingot x 64'),
    S('widget.scrollbar','Review all requests|检查全部请求','Scroll through the request list and check for duplicates or unnecessarily large targets.','滚动检查请求列表，避免重复请求或不必要的大额目标。'),
    S('view.body','Crafting prerequisites|合成前提','The requesting network still needs the recipe, ingredients and a free crafting CPU. A requester cannot supply a missing recipe.','发起请求的网络仍需有效配方、原料和空闲合成 CPU，请求器不能自动补齐缺失的配方。'),
    S('view.body','Test and observe|测试与观察','Start with a small target and inspect actual crafting status before enabling many standing requests.','先设置小目标，检查实际合成状态后，再启用大量持续请求。')])
add('requester_terminal', 'Requester Terminal|请求终端', 'GuiRequesterTerm', 'terminals/requester_terminal',
    'requester_terminal wireless_requester_terminal', 'crafting', 'crafting_cpu', [
    S('widget.search','Find a requester|查找请求器','Search for the requester you intend to manage; naming requesters helps keep production lines separate.','搜索要管理的请求器，命名有助于区分不同生产线。',sample='components'),
    S('view.body','Inspect requested amounts|核对请求数量','Review the resources and targets exposed by that requester before editing them.','修改前先核对该请求器公开的资源与目标数量。'),
    S('widget.scrollbar','Large request lists|长请求列表','Scroll to review all entries and check that requests belong to the intended network and machine.','滚动检查全部条目，确认请求属于预期的网络和机器。'),
    S('view.body','Follow a waiting job|跟踪等待任务','If a request waits, inspect its pattern, ingredients, CPU and exact returning product in the crafting status view.','请求等待时，在合成状态中检查样板、原料、CPU 与准确回网产物。')])
for id,title,style,host,comps in [
    ('portable_item_cell','Portable Item Cell|便携物品存储元件','terminals/portable_item_cell','item:portable_item_cell_','portable_item_cell_1k portable_item_cell_4k'),
    ('portable_fluid_cell','Portable Fluid Cell|便携流体存储元件','terminals/portable_fluid_cell','item:portable_fluid_cell_','portable_fluid_cell_1k'),
    ('wireless_terminal','Wireless Terminal|无线终端','terminals/wireless_terminal','WirelessTerminalGuiHost','wireless_terminal wireless_universal_terminal')]:
    wireless=id=='wireless_terminal'
    add(id,title,'GuiMEStorage',style,comps,'networks' if wireless else 'basics','wireless' if wireless else 'storage_cells',[
        S('widget.search','Search|搜索','Search the resources exposed by this device. W remains a normal character while the field has focus.','搜索此设备公开的资源，输入框获得焦点时，W 保持作为普通字符。',sample='iron'),
        S('repo.0','Stored resources|存储资源','A portable cell stores resources locally on that item; available capacity and supported resource types still apply.' if not wireless else 'The wireless device accesses its bound network. Check the actual access point, distance and dimension when disconnected.',
          '便携元件将资源保存在该物品内，仍受容量与资源类型限制。' if not wireless else '无线设备访问已绑定网络，断开时检查访问点、距离与维度。','minecraft:iron_ingot',16),
        S('slot.PLAYER_INVENTORY.0','Transfer and charge|转移与充能','Keep the device charged and test a small transfer. Portable fluid storage uses resource entries rather than treating every icon as a loose item.','保持设备电量并测试少量转移，便携流体存储使用资源条目，不应把所有图标理解为散装物品。'),
        S('widget.verticalToolbar','Device settings|设备设置','Review supported settings before enabling automatic pickup. On a Universal Terminal, use the native terminal-type selector to switch the installed view.','启用自动拾取前先检查设置。通用终端可通过原生终端类型选择器，切换已安装的终端视图。')],host=host)
add('portable_workbench','Portable Cell Workbench|便携存储元件工作台','GuiCellWorkbench','portable_cell_workbench',
    'portable_cell_workbench','basics','storage_cells',[
    S('slot.STORAGE_CELL.0','Cell to edit|待编辑元件','Insert the compatible cell to edit its partition away from a placed workstation.','放入兼容元件，可不依赖已放置的工作台编辑分区。','ae2:item_storage_cell_1k'),
    S('slot.CONFIG.0','Partition entries|分区标记','These entries restrict accepted resources. They do not create or deliver real stored items.','这些标记限制允许接收的资源，不会创建或提供真实库存。','minecraft:iron_ingot'),
    S('slot.STORAGE_CELL.0','Return the cell|归还元件','Take the cell back and verify its destination before closing the portable workbench.','关闭便携工作台前取回元件，并确认其存放位置。')],host='PortableCellWorkbenchGuiHost')

add('craft_amount','Request crafting: amount|发起合成：数量','GuiCraftAmount','craft_amount','crafting_terminal pattern_encoding_terminal','crafting','autocrafting',[
    S('widget.amountToCraft','Requested amount|请求数量','Enter the desired amount and check the displayed unit. This is a request, not a promise that the network has sufficient materials.','输入目标数量并核对显示单位，这只是请求，不代表网络已经备齐材料。',sample='16'),
    S('widget.next','Calculate the plan|计算计划','Continue to calculate the recipe plan. Read the material and CPU checks before starting a large task.','继续计算配方计划，大额任务开始前应阅读材料与 CPU 检查。'),
    S('widget.numberEntryButtonConfig','Quantity shortcuts|数量快捷键','Configure number-entry increments if needed. Modified-key shortcuts must not be confused with the actual requested amount.','按需设置数量增减快捷键，注意修饰键下的增量与最终请求数量不同。')])
add('craft_confirm','Request crafting: plan|发起合成：计划确认','GuiCraftConfirm','craft_confirm','crafting_terminal','crafting','autocrafting',[
    S('widget.search','Inspect materials|检查材料','Search the plan and inspect stored, craftable and missing resources. Missing items can prevent the task from starting.','搜索计划，核对已有、可合成与缺失资源，缺料可能导致任务无法启动。',sample='iron'),
    S('widget.selectCpuList','Choose a CPU|选择 CPU','Choose an available crafting CPU with enough storage for this plan. A busy or undersized CPU is not a valid destination.','为计划选择空闲且存储容量足够的 CPU，忙碌或容量不足的 CPU 不能作为有效目标。'),
    S('widget.craftTree','Dependency tree|依赖树','Open the tree to follow nested crafting dependencies and identify the branch that is missing resources.','打开合成树，跟踪嵌套依赖并定位缺料分支。'),
    S('widget.start','Start deliberately|确认后启动','Start only after reviewing the plan and target CPU. Live guidance observes this button; it does not start the job for you.','核对计划与目标 CPU 后再启动，实机引导只观察按钮，不会替你发起任务。')])
add('craft_cpu_list','Crafting CPU selection|合成 CPU 选择','GuiCraftConfirmCpuList','craft_confirm_cpu_list','crafting_terminal 1k_crafting_storage','crafting','crafting_cpu',[
    S('widget.search','Find a CPU|查找 CPU','Search named crafting CPUs to select the intended production line.','搜索已命名的合成 CPU，选择预期生产线。',sample='processors'),
    S('widget.sort','Compare CPUs|比较 CPU','Sort and inspect availability and storage. Free CPU capacity must satisfy the current crafting plan.','排序并检查空闲状态与存储容量，空闲 CPU 的容量必须满足当前计划。'),
    S('view.body','Select the destination|选择目标','Choose a suitable entry, then return and verify the CPU shown in the confirmation screen.','选择合适条目后返回，并核对确认页面显示的 CPU。')])
for id,title,cls,style in [('crafting_cpu','Crafting CPU: running job|合成 CPU：运行任务','GuiCraftingCPU','crafting_cpu'),('crafting_status','Crafting status: all CPUs|合成状态：全部 CPU','GuiCraftingStatus','crafting_status')]:
    add(id,title,cls,style,'1k_crafting_storage crafting_monitor crafting_terminal','crafting','crafting_cpu',[
        S('widget.search','Follow a product|跟踪产物','Search the active job to find the resource currently required or being crafted.','搜索运行任务，找到当前所需或正在制作的资源。',sample='processor'),
        S('view.body','Read task progress|阅读任务进度','Distinguish stored ingredients, active crafts and expected returned outputs. A processing job can wait for an exact product.','区分已存原料、正在加工的内容与预期回网产物；处理任务可能正在等待特定产物。'),
        S('widget.suspend','Pause a task|暂停任务','Inspect the suspend control and its current state before pausing production. Pausing does not undo items already delivered to machines.','暂停生产前核对暂停控件及其状态，暂停不会撤回已经投送给机器的物品。'),
        S('widget.cancel','Cancel a task|取消任务','Cancel only when intended. Inspect machines and intermediate items before submitting a replacement job.','仅在确认需要时取消，重新提交任务前先检查机器与中间产物。')])
add('crafting_tree','Crafting dependency tree|合成依赖树','GuiCraftingTree','', 'crafting_terminal','crafting','crafting_cpu',[
    S('widget.tree','Recipe branches|配方分支','Follow the tree from the requested product down to its ingredients and intermediate crafts.','从请求产物向下跟踪原料及中间合成分支。'),
    S('widget.missingOnly','Missing branches|缺失分支','Use the missing-only filter to focus on the resources or dependencies blocking the plan.','使用仅显示缺失分支的过滤，集中查看阻碍计划的资源与依赖。'),
    S('widget.screenshot','Export the view|导出视图','The native screenshot button exports the tree view. This guide never activates file export on your behalf.','原生截图按钮可导出合成树，引导不会替你执行文件导出。'),
    S('widget.back','Return to the plan|返回计划','Return to the parent branch or crafting plan after diagnosing the missing dependency.','定位缺失依赖后，返回父分支或合成计划。')])
add('craft_error','Crafting failure details|合成失败详情','GuiCraftError','craft_error','crafting_terminal','crafting','crafting_cpu',[
    S('text.errorText','Read the cause|阅读原因','Read the actual error rather than repeatedly submitting the same task. Look for missing ingredients, invalid recipes or capacity constraints.','阅读实际错误，不要反复提交同一任务；检查缺料、无效配方与容量限制。'),
    S('view.body','Repair the dependency|修复依赖','Correct the identified problem in the network or machine, then calculate a new plan.','在网络或机器中修复指出的问题，再重新计算计划。')])
add('task_priority','Crafting task priority|合成任务优先级','GuiCraftingTaskPriority','crafting_task_priority','crafting_terminal','crafting','crafting_cpu',[
    S('widget.priority','Task priority|任务优先级','Set the priority of this task relative to other tasks. It does not increase crafting CPU storage or invent missing ingredients.','设置此任务相对于其他任务的优先级，不会增加 CPU 容量或凭空补齐原料。',sample='10'),
    S('widget.back','Return and verify|返回核对','Return to the task screen and verify the selected priority before proceeding.','返回任务页面，继续前核对所选优先级。')])
add('stock_amount','Configure stock amount|设置备货数量','GuiSetStockAmount','set_stock_amount','interface stock_export_bus','automation','interfaces',[
    S('widget.amountToStock','Target amount|目标数量','Enter the desired local amount and check its unit and maximum. Zero can have a special clearing or disabling meaning on the parent device.','输入期望本地数量，核对单位与上限，零在上级设备中可能表示清空或停用。',sample='16'),
    S('widget.save','Save the target|保存目标','Save only after confirming the intended resource. The amount is a target, not a supplied inventory stack.','确认目标资源后再保存，数量是目标值，不是已提供的库存堆叠。'),
    S('widget.back','Return to the device|返回设备','Inspect the parent configuration and test actual replenishment after changing a target.','修改目标后检查上级配置，并测试真实补货。')])

# Network engineering, wireless pairing and diagnostics.
add('wireless_access_point','Wireless Access Point: pair a device|无线访问点：配对设备','GuiWirelessAccessPoint','wireless_access_point',
    'wireless_access_point wireless_terminal wireless_universal_terminal','networks','wireless',[
    S('slot.MACHINE_INPUT.0','Device to pair|待配对设备','Insert a supported wireless device into the pairing input. This associates the device with this network access point.','把支持的无线设备放入配对输入槽，使设备与此网络访问点关联。','ae2:wireless_terminal'),
    S('slot.MACHINE_OUTPUT.0','Paired device|已配对设备','Collect the paired device from the output. Keep it charged before trying remote access.','从输出处取回配对设备，远程访问前先确认设备电量。','ae2:wireless_terminal'),
    S('text.range','Wireless range|无线范围','Read the actual range and energy use. Supported booster slots can change the tradeoff between range and power cost.','阅读实际范围与能耗，支持的增程槽可改变范围与耗电之间的关系。'),
    S('slot.STORAGE.0','Boosters and testing|增程与测试','Use compatible boosters, then test access from the intended location and dimension. Do not assume every wireless feature bypasses range.','使用兼容增程材料后，在预期位置与维度测试；不要假定所有无线功能都忽略距离。')])
add('quantum_bridge','Quantum Bridge: pair the ends|量子桥：两端配对','GuiQNB','qnb', 'quantum_link quantum_ring quantum_entangled_singularity', 'networks','quantum_bridge',[
    S('slot.STORAGE.0','Entangled pair|缠绕奇点对','Place one member of the same entangled pair into each completed bridge. An ordinary Singularity is not an already paired entangled item.','在两端完整量子桥中分别放入同一对缠绕奇点；普通奇点不是已经配对的缠绕奇点。','ae2:quantum_entangled_singularity'),
    S('view.body','Power and formation|供电与结构','Check the full ring structure and power on both ends. Merely inserting the pair does not repair an incomplete structure.','检查两端完整环形结构与供电，仅放入奇点不能修复不完整的结构。'),
    S('slot.STORAGE.0','Verify the remote network|验证远端网络','Keep relevant chunks loaded and test the intended remote device. Removing the paired item disconnects the link.','保持相关区块加载并测试远端设备，取走配对物品会断开连接。')])
add('spatial_io','Spatial IO Port: transfer a region|空间 IO 端口：传送区域','GuiSpatialIOPort','spatial_io_port',
    'spatial_io_port spatial_storage_cell_2 spatial_storage_cell_16 spatial_storage_cell_128','networks','spatial_io',[
    S('slot.MACHINE_INPUT.0','Spatial cell|空间存储元件','Insert a Spatial Storage Cell large enough for the defined region. It stores a spatial region rather than ordinary item stacks.','放入足以容纳目标区域的空间存储元件，它保存空间区域而非普通物品堆叠。','ae2:spatial_storage_cell_2'),
    S('text.scs_size','Defined region|定义的区域','Verify the displayed spatial dimensions against the Spatial Pylon setup before operating the port.','操作前核对显示的空间尺寸与空间塔搭建的范围一致。'),
    S('text.required_power','Energy and efficiency|能量与效率','Read required energy, available energy and efficiency. The network must have enough stored energy for the transfer.','阅读所需能量、可用能量和效率，网络必须存有足够能量才能进行转移。'),
    S('slot.MACHINE_OUTPUT.0','Complete and recover|完成与取回','Trigger the port using the intended control and collect the resulting cell. Test with a small nonvaluable region first.','通过预期控制触发端口并取回处理后的元件，先用小型且不含贵重物品的区域测试。','ae2:spatial_storage_cell_2')])
add('spatial_anchor','Spatial Anchor: loaded chunks|空间锚：区块加载','GuiSpatialAnchor','spatial_anchor','spatial_anchor','networks','spatial_io',[
    S('text.loaded_chunks','Loaded chunks|已加载区块','Inspect the loaded chunk count and the network area affected by this anchor.','检查已加载区块数量与空间锚影响的网络区域。'),
    S('text.used_power','Power cost|耗电','Read the ongoing power cost. Keep the network powered if its operation depends on loaded chunks.','阅读持续耗电，需要依赖区块加载运行时应保持网络供电。'),
    S('widget.verticalToolbar','Overlay and verification|范围显示与核对','Use the supported overlay to inspect coverage, then verify the actual remote machines keep operating.','使用支持的范围显示检查覆盖，再验证远端机器确实持续运行。')])
add('network_status','Network status: power and channels|网络状态：电力与频道','GuiNetworkStatus','network_status','controller network_tool','networks','channels',[
    S('text.stored_power','Stored energy|已存能量','Compare current energy with capacity. A nonzero battery does not guarantee generation will keep up with demand.','比较当前能量与容量，有电不代表发电量能长期跟上需求。'),
    S('text.power_usage_rate','Energy demand|能量需求','Compare input, usage and channel-related energy demand to find a power deficit.','比较输入、消耗及频道相关耗电，判断是否存在供电缺口。'),
    S('widget.scrollbar','Connected devices|连接设备','Scroll the device overview and check that expected machines appear in the correct network.','滚动查看设备概况，确认目标机器出现在正确网络中。'),
    S('text.channel_power_rate','Channel checks|频道检查','When a machine is offline, also check cable capacity, controller topology and loaded chunks; energy alone is not enough.','机器离线时还应检查线缆容量、控制器拓扑与区块加载，仅有能量并不足够。')])
add('network_tool','Network Tool: upgrades and diagnostics|网络工具：升级与诊断','GuiNetworkTool','network_tool','network_tool','networks','monitors_tools',[
    S('slot.STORAGE.0','Upgrade storage|升级卡收纳','Keep compatible upgrade cards in the tool inventory for maintenance. These are real stored cards.','可在工具库存内收纳兼容升级卡，槽内存放的是真实物品。','ae2:capacity_card'),
    S('view.body','Inspect the target network|检查目标网络','Use the tool on the intended network device to inspect its actual status. Verify which network you are examining.','对预期网络设备使用工具检查实际状态，并确认当前检查的是哪个网络。'),
    S('slot.STORAGE.0','Recover and maintain|回收与维护','Keep room for removed cards and verify the machine settings after changing upgrades.','为取出的升级卡留出空间，改变升级后重新检查机器设置。')])
add('network_analyser','Network Analyzer|网络分析仪','GuiNetworkAnalyser','network_analyser','network_analyser','networks','monitors_tools',[
    S('text.mode_value','Analysis mode|分析模式','Choose the intended display mode and inspect which nodes or connections it classifies.','选择预期显示模式，检查它正在分类的节点或连接。'),
    S('text.normal_nodes','Node statistics|节点统计','Compare normal, dense and missing node statistics. The labels describe the current analysis, not automatic repairs.','比较普通、致密与缺失节点统计，这些标签描述当前分析结果，不会自动修复网络。'),
    S('widget.color_window','Overlay colors|显示颜色','Configure distinguishable colors, then inspect the world overlay to locate the corresponding cables and devices.','设置容易区分的颜色，再在世界中对照显示寻找相应线缆和设备。')])
add('tick_analyser','Tick Analyzer|运算分析仪','GuiTickAnalyser','tick_analyser','tick_analyser','networks','monitors_tools',[
    S('widget.duration_input','Sample duration|采样时长','Set a sampling duration long enough to observe a representative machine cycle.','设置足以覆盖典型机器循环的采样时长。',sample='100'),
    S('view.body','Read the distribution|阅读分布','Compare sampled work rather than drawing conclusions from one spike. Inspect the selected target and analysis range.','比较采样结果，不根据单次峰值下结论，并核对所选目标与分析范围。'),
    S('text.range_1','Compare under the same load|同负载比较','Repeat a sample under the same workload after a change so the result has a useful comparison.','修改后在相同工作负载下再次采样，使结果具有可比较性。')])
add('advanced_memory_card','Advanced Memory Card: P2P management|高级内存卡：P2P 管理','GuiAdvancedMemoryCard','advanced_memory_card',
    'advanced_memory_card me_p2p_tunnel','networks','p2p',[
    S('widget.search','Find a tunnel|查找隧道','Search tunnel entries by the available identifying information. Give endpoints names before managing a large installation.','按可用标识搜索隧道条目，大规模管理前先为端点命名。',sample='main'),
    S('view.body','Roles and frequency|角色与频率','Inspect each entry\'s type, input/output role, frequency and location before binding.','绑定前核对条目类型、输入输出角色、频率与位置。'),
    S('widget.scrollbar','Select the intended endpoint|选择正确端点','Scroll to the intended endpoint and use the native bind action deliberately. Pair compatible tunnel types and keep the carrier powered.','滚动到目标端点，再主动执行原生绑定操作；配对兼容类型并为承载网络供能。'),
    S('view.body','Verify the link|验证连接','Test the actual remote device after binding. A saved entry is not proof that its current world position is loaded and online.','绑定后测试真实远端设备，保存的条目不代表其当前位置已经加载且在线。')])

# Filters, protection and utility subdialogs.
add('cell_restriction','Storage cell restrictions|存储元件限制','GuiCellRestriction','cell_restriction','cell_workbench','basics','storage_cells',[
    S('widget.amountInput','Amount limit|数量限制','Set the amount limit supported by the selected cell. Check whether you intend a restrictive cap before applying it.','设置所选元件支持的数量限制，应用前确认确实需要限制上限。',sample='1024'),
    S('widget.typesInput','Type limit|类型限制','Set the allowed number of resource types without confusing types with stored item count.','设置允许的资源类型数，不要将类型数与物品总数量混淆。',sample='8'),
    S('widget.set','Apply restrictions|应用限制','Apply only to the intended cell, then inspect the cell tooltip and test one insertion.','只对目标元件应用限制，随后检查元件提示并测试一次存入。'),
    S('widget.release','Release restrictions|解除限制','Use release when you intend to remove the restriction. It does not delete or supply stored resources.','需要解除限制时使用此按钮，它不会删除或提供存储资源。')])
add('pickup_filter','Portable cell pickup filter|便携元件拾取过滤','GuiPortableCellPickupFilter','portable_cell_pickup_filter','portable_item_cell_1k','basics','storage_cells',[
    S('slot.PORTABLE_CELL_PICKUP_FILTER.0','Pickup filter|拾取过滤','Configure which drops the portable cell may collect automatically. Filter entries are ghost markers.','配置便携元件允许自动收集的掉落物，过滤项是幽灵标记。','minecraft:iron_ingot'),
    S('widget.verticalToolbar','Matching mode|匹配模式','Check the supported matching and inclusion mode. Start with a narrow filter to avoid collecting unwanted resources.','检查支持的匹配与包含模式，从小范围过滤开始，避免收集不需要的资源。'),
    S('widget.back','Test pickup|测试拾取','Return to the cell and test one dropped item with enough charge and capacity.','返回元件页面，在电量与容量充足时测试一个掉落物。')])
for id,title,cls,style,components in [
    ('void_cell','Void Cell: disposal mode|虚空存储元件：处理模式','GuiVoidCell','void_cell','void_storage_cell'),
    ('portable_void_cell','Portable Void Cell|便携虚空存储元件','GuiPortableVoidCell','portable_void_cell_condenser','portable_void_cell')]:
    add(id,title,cls,style,components,'automation','condenser',[
        S('widget.trash' if id=='void_cell' else 'widget.mode','Disposal mode|资源处理模式','Read the disposal or matter-conversion mode carefully. Resources accepted for disposal cannot be treated as recoverable normal storage.','仔细阅读销毁或物质转换模式，已接受销毁的资源不能当作可取回的普通库存。'),
        S('view.body','Narrow the input|限制输入范围','Restrict which resources can reach this device and test with expendable items before connecting a main storage network.','接入主存储前，限制能够到达此设备的资源，并用可消耗物品测试。'),
        S('widget.matterBalls' if id=='void_cell' else 'slot.MACHINE_OUTPUT.0','Products and capacity|产物与容量','If producing matter outputs, keep space for them and check the actual conversion requirements.','产出物质产物时，为其留出空间，并核对实际转换要求。')])
add('wireless_magnet','Wireless magnet settings|无线磁铁设置','GuiWirelessMagnet','wireless_magnet','wireless_terminal wireless_universal_terminal','networks','wireless',[
    S('slot.MAGNET_PICKUP_CONFIG.0','Pickup rules|拾取规则','Select which dropped resources may be picked up. Keep the pickup filter narrow while testing.','选择允许拾取的掉落资源，测试时保持拾取范围较小。','minecraft:iron_ingot'),
    S('slot.MAGNET_INSERT_CONFIG.0','Insertion rules|存入规则','Configure which collected resources may be inserted into ME storage. Pickup and insertion are separate decisions.','配置收集后允许存入 ME 的资源，拾取与存入是两个不同的判断。','minecraft:iron_ingot'),
    S('widget.pickup_mode','Matching modes|匹配模式','Check pickup mode, insertion mode and the master switch before enabling automatic collection.','启用自动收集前核对拾取模式、存入模式与总开关。'),
    S('widget.switch','Enable and test|启用并测试','Test with one drop and verify the destination, wireless connection, power and available network capacity.','用一个掉落物测试，确认去向、无线连接、电量与网络剩余容量。')])
add('priority','Storage priority|存储优先级','GuiPriority','priority','storage_bus drive interface pattern_provider','automation','storage_bus',[
    S('widget.priority','Priority value|优先级数值','Set the desired priority and read the insertion/extraction hints. Priorities do not create additional capacity.','设置优先级并阅读存入与取出提示，优先级不会增加容量。',sample='10'),
    S('text.priority_insertion_hint','Insertion order|存入顺序','Use the displayed insertion rule to decide which storage should receive new resources first.','按页面显示的存入规则，确定新资源应优先进入哪个存储。'),
    S('text.priority_extraction_hint','Extraction order|取出顺序','Check the extraction rule separately, then test one resource before reorganizing the whole network.','单独核对取出规则，重整整个网络前先测试一种资源。')])
add('priority_tuner','Priority Tuner|优先级调整器','GuiPriorityTuner','priority_tuner','priority_tuner','automation','storage_bus',[
    S('widget.priority','Stored priority|保存的优先级','Set the priority value the tool should apply. Verify the sign and magnitude before using it on a machine.','设置工具将应用的优先级，使用前核对正负号与数值大小。',sample='10'),
    S('view.body','Application mode|应用模式','Read the native tool mode and item tooltip before applying changes to one or several devices.','对单个或多个设备应用前，阅读原生工具模式与物品提示。'),
    S('widget.priority','Verify the destination|核对目标','Inspect a modified device afterward to confirm its priority and intended storage behavior.','修改后检查目标设备，确认优先级及存储行为符合预期。')])
add('config_modifier','Configuration Modifier: amount operations|配置修改器：数量运算','GuiConfigModifier','config_modifier','config_modifier','automation','interfaces',[
    S('widget.data_input','Numeric operand|运算数值','Enter the numeric operand used to adjust a compatible resource configuration. Inspect the original amounts before applying a bulk change.','输入调整兼容资源配置所用的数值，批量修改前先检查原有数量。',sample='2'),
    S('widget.mode','Arithmetic mode|运算模式','Select the intended add, subtract, multiply, divide, limit, set or remove operation. A multiplication is different from setting an absolute amount.','选择所需的加、减、乘、除、限制、设定或移除操作；乘法与设为固定数量不同。'),
    S('widget.data_input','Verify resulting amounts|核对结果数量','Test one supported target and reopen its configuration. Confirm the resulting amounts before applying the tool to more devices.','先对一个支持的目标测试并重新查看配置，确认数量结果后再用于更多设备。')])
add('quartz_knife','Quartz Cutting Knife: naming|石英切割刀：命名','GuiQuartzKnife','quartz_knife','certus_quartz_cutting_knife nether_quartz_cutting_knife','basics','monitors_tools',[
    S('widget.name','Name|名称','Enter the intended name using the native text field. Typing W here must remain ordinary text input.','在原生输入框中填写名称，这里输入 W 应保持为普通文字输入。',sample='Main storage'),
    S('slot.MACHINE_INPUT.0','Input|输入','Insert the material required by the installed naming recipe. Check the resulting item before confirming.','放入当前命名配方要求的材料，确认前核对产物。'),
    S('slot.MACHINE_OUTPUT.0','Result|结果','Take the intended named output and verify the displayed name.','取走目标命名产物并核对显示名称。')])
for id,title,cls in [('renamer','Rename a network device|重命名网络设备','GuiRenamer'),('pattern_renamer','Rename a pattern entry|重命名样板条目','GuiPatternItemRenamer')]:
    add(id,title,cls,'renamer','network_tool pattern_encoding_terminal','networks' if id=='renamer' else 'crafting','monitors_tools' if id=='renamer' else 'autocrafting',[
        S('widget.name','Descriptive name|清晰名称','Enter a name that distinguishes the device or pattern from similar entries.','填写能够与相似设备或样板区分的名称。',sample='Processor line'),
        S('view.body','Confirm in the parent screen|返回核对','Return using the native control, then check the name where the item or device is listed.','通过原生操作返回后，在物品或设备列表中核对名称。')])
add('output_sides','Machine output sides|机器输出面','GuiOutputSides','output_sides','inscriber crystal_assembler molecular_assembler','automation','processors',[
    S('widget.side_front','Machine-relative sides|机器相对面','The side controls are relative to the machine\'s orientation. Match the front with the actual placed block.','侧面控件按机器朝向定义，先将正面与世界中放置的机器对应。'),
    S('widget.side_top','Enable the intended output|启用目标输出面','Select only the sides connected to the intended receiving inventory. Test one product before using several outputs.','只启用连接目标接收容器的面，使用多个输出前先测试一个产物。'),
    S('widget.returnToParent','Return and test|返回并测试','Return to the machine and confirm that extraction reaches the intended inventory or requesting ME network.','返回机器，确认产物到达目标容器或发起任务的 ME 网络。')])
add('work_interval','Machine work interval|机器工作间隔','GuiWorkInterval','work_interval','advanced_io_bus import_export_bus stock_export_bus','automation','import_export',[
    S('widget.workInterval','Work interval|工作间隔','Set the interval using the displayed unit. A shorter interval increases checking frequency rather than creating ingredients or destination space.','按显示单位设置间隔，缩短间隔会增加检查频率，不会创造原料或目标空间。',sample='20'),
    S('view.body','Measure the result|观察结果','Test the actual throughput and server workload before applying a very short interval to many devices.','为大量设备应用很短间隔前，先测试实际吞吐与服务器负载。')])
add('terminal_settings','Terminal preferences|终端设置','GuiTerminalSettings','terminals/terminal_settings','terminal crafting_terminal wireless_terminal','basics','first_network',[
    S('view.body','Settings categories|设置分类','Use the native settings pages to choose search, display, convenience and crafting preferences.','通过原生设置页选择搜索、显示、便捷操作与合成偏好。'),
    S('view.body','Search focus and persistence|搜索焦点与记忆','Decide whether search is focused automatically and whether queries persist. Focused input keeps W available for typing.','设置搜索是否自动获得焦点、是否保留搜索词；输入框获得焦点时 W 保持用于输入。'),
    S('view.body','Automatic operations|自动操作','Review pickup, restock, crafting and grid-clear options before enabling them. These change real terminal behavior.','启用前核对拾取、补货、合成与网格清理选项，它们会改变真实终端行为。'),
    S('widget.back','Return and verify|返回核对','Return and test the chosen settings with one item before relying on them during production.','返回后先用一个物品测试所选设置，再用于生产。')])
add('key_types','Choose resource types|选择资源类型','GuiKeyTypeSelection','key_type_selection','terminal storage_bus','basics','fluid_storage',[
    S('widget.keytypes','Resource type selection|资源类型选择','Choose the supported resource types to display or handle, such as items or fluids. Available types depend on installed integrations.','选择要显示或处理的资源类型，例如物品或流体；可用类型取决于已安装联动。'),
    S('widget.back','Check the resulting view|核对视图','Return and verify that the filtered view still includes the resource you need. A hidden type is not deleted stock.','返回后确认过滤视图仍包含所需资源，隐藏类型不代表删除库存。')])
add('number_buttons','Number-entry shortcuts|数值输入快捷设置','GuiNumberEntryButtonSettings','number_entry_button_settings','crafting_terminal interface','basics','autocrafting',[
    S('view.body','Normal increments|普通增量','Configure the normal increment buttons using the native numeric fields.','使用原生数值输入框配置普通增减按钮。'),
    S('text.shift_label','Modified-key increments|修饰键增量','Review Shift, Ctrl and Alt increments separately so a modified click does not unexpectedly request a large amount.','分别检查 Shift、Ctrl 与 Alt 增量，避免修饰键点击意外请求大量物品。'),
    S('widget.back','Test the result|测试结果','Return to the quantity dialog and test a small value before submitting the actual operation.','返回数量窗口，用小数值验证后再提交实际操作。')])
add('pattern_modifier','Pattern Modifier: batch editing|样板修改器：批量编辑','GuiPatternModifier','pattern_modifier','pattern_modifier','crafting','autocrafting',[
    S('widget.mode','Editing mode|编辑模式','Choose the intended edit mode before selecting patterns. Batch edits can affect multiple installed recipes.','选择目标样板前先确定编辑模式，批量修改可能影响多个已安装配方。'),
    S('slot.ENCODED_PATTERN.0','Target patterns|目标样板','Select the patterns to edit and verify their inputs and outputs. Keep a backup before replacing an established production recipe.','选择待修改样板并核对输入与输出，替换已有生产配方前先备份。','ae2:processing_pattern'),
    S('widget.replace','Replacement and cloning|替换与复制','Use replacement, cloning, quantity or property controls only after checking the selected operation and blank-pattern requirements.','使用替换、复制、数量与属性操作前，核对当前操作与空白样板需求。'),
    S('widget.clear','Review changes|检查修改','Inspect the edited patterns and test one recipe. Clear the selection when finished to avoid editing unrelated patterns next time.','检查修改后的样板并测试一个配方，结束后清理选择，避免下次误改无关样板。')])
add('pattern_import_priority','Recipe import priority|配方导入优先级','GuiPatternImportPrioritySettings','terminals/pattern_import_priority_settings','pattern_encoding_terminal pattern_encoding_access_terminal','crafting','autocrafting',[
    S('view.body','Preferred recipe sources|优先配方来源','Arrange the preferred sources used when importing a recipe. This order concerns recipe selection, not storage priority.','排列导入配方时优先使用的来源，这一顺序针对配方选择，不是存储优先级。'),
    S('text.page_info','Review every page|检查全部页面','Inspect all available entries before accepting the order. Recipe-source options depend on installed recipe integrations.','确认顺序前检查全部条目，可选配方来源取决于已安装配方联动。'),
    S('widget.back','Verify an import|验证导入','Return to encoding and import one recipe to verify the resulting ingredients and output.','返回编码页面，导入一个配方并核对原料与产物。')])
add('processing_amount','Processing pattern amounts|处理样板数量','GuiSetProcessingPatternAmount','set_processing_pattern_amount','pattern_encoding_terminal processing_pattern','crafting','processing',[
    S('widget.amountToStock','Exact resource amount|准确资源数量','Set the amount for this processing entry and check the resource unit. Large fluid amounts are not equivalent to the same number of item stacks.','设置此处理条目的数量并核对资源单位，大数值流体量不等于相同数量的物品堆叠。',sample='1000'),
    S('widget.back','Check the full recipe|核对完整配方','Return and compare all input and output amounts before encoding. The requesting network waits for the exact declared product.','返回后比较全部输入与输出数量，再编码；发起任务的网络会等待准确声明的产物。')])
add('crafting_pattern_view','Inspect a crafting pattern|查看合成样板','GuiCraftingPattern','', 'crafting_pattern','crafting','autocrafting',[
    S('view.body','Recorded recipe|已记录配方','Inspect the crafting-grid layout and result recorded on the pattern. This view describes a recipe and does not craft items.','检查样板记录的合成网格与产物，此页面描述配方，不会制作物品。'),
    S('view.header','Substitution flags|替代设置','Read the item and fluid substitution flags before assuming similar ingredients are interchangeable.','先阅读物品与流体替代设置，不要直接假定相近原料能够互换。'),
    S('view.body','Verify before installing|安装前核对','Install the intended pattern in the proper provider or assembler, then test one request.','将目标样板安装到正确供应器或装配室，再测试一次请求。')])
add('processing_pattern_view','Inspect a processing pattern|查看处理样板','GuiProcessingPattern','', 'processing_pattern','crafting','processing',[
    S('view.body','Inputs and outputs|输入与输出','Inspect every declared input and output and its quantity. This display is read-only.','检查全部输入输出及数量，此视图为只读展示。'),
    S('view.body','Reusable tools|可重复使用的工具','A press or mold that stays installed in the machine must not be listed as consumed on every execution.','留在机器内的压印模板或模具，不应被列为每次执行都会消耗的原料。'),
    S('view.body','Match the real machine|匹配真实机器','Compare with the actual machine recipe and verify that the exact output returns to the same requesting network.','与真实机器配方比较，并确认准确产物回到发起请求的同一网络。')])

# Existing lessons remain authored in generate-guis.py; metadata makes their coverage explicit.
LEGACY = {
    'drive': ('GuiDrive','drive','basics','first_network'),
    'terminal': ('GuiMEStorage','terminals/terminal','basics','first_network'),
    'cell_workbench': ('GuiCellWorkbench','cell_workbench','basics','storage_cells'),
    'inscriber': ('GuiInscriber','inscriber','crafting','processors'),
    'pattern_crafting': ('GuiPatternEncodingTerm','terminals/pattern_encoding_terminal','crafting','autocrafting'),
    'pattern_processing': ('GuiPatternEncodingTerm','terminals/pattern_encoding_terminal','crafting','processing'),
    'pattern_provider': ('GuiPatternProvider','pattern_provider','crafting','autocrafting'),
    'interface': ('GuiInterface','interface','automation','interfaces')
}
