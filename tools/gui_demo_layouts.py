"""Complete demo appearances, independent of the authored highlight/operation targets.

Geometry, backgrounds and text come from the pinned AE2S styles. Constructor registrations
are recorded in gui_native_widgets.json; these profiles select an illustrative, fixed state.
No artwork is embedded and no native container or network action is used by the renderer.
"""
import json
from pathlib import Path
from gui_layouts import point, target_geometry

CLASSES = json.loads(Path(__file__).with_name('gui_native_widgets.json').read_text())['classes']
COMMON_OPTIONAL = {'toolbox', 'wirelessUniversalTerminalSelector', 'keyTypeSelectionWindow', 'upgradeScrollbar'}
UPGRADES = dict(inscriber=3, cell_workbench=2, portable_workbench=2, pattern_provider=5,
                molecular_assembler=5, io_port=3, vibration_chamber=3, crystal_assembler=3,
                import_bus=4, export_bus=4, storage_bus=5, precise_export_bus=5,
                threshold_export_bus=5, stock_export_bus=5, import_export_bus=5,
                advanced_io_bus=5, precise_storage_bus=5, od_export_bus=5, od_storage_bus=5,
                mod_export_bus=5, mod_storage_bus=5, formation_plane=5, annihilation_plane=5,
                portable_item_cell=2, portable_fluid_cell=2, wireless_terminal=2)
NUMBERS = {'priority', 'level', 'upperLevel', 'lowerLevel', 'workInterval', 'amountToCraft', 'amountToStock'}
ICONS = dict(openPriority='PRIORITY', back='BACK', returnToParent='BACK', previousPage='ARROW_LEFT',
             nextPage='ARROW_RIGHT', craftingStatus='CRAFT_HAMMER', craftTree='CTL_CRAFT_TREE',
             encodePattern='WHITE_ARROW_DOWN', uploadPattern='ARROW_UP',
             clearCraftingGrid='S_ARROW_UP', clearToPlayerInv='S_ARROW_DOWN',
             rotateCraftingGrid='CRAFTING_GRID_ROTATE', balanceCraftingGrid='CRAFTING_GRID_BALANCE',
             craftingClearPattern='S_CLEAR', processingClearPattern='S_CLEAR',
             craftingSubstitutions='S_SUBSTITUTION_DISABLED', craftingFluidSubstitutions='S_SUBSTITUTION_DISABLED',
             processingCycleOutput='S_CYCLE', processingMergeHeiInputs='S_ARROW_UP',
             modeTabButton0='CRAFT_HAMMER', modeTabButton1='FURNACE',
             mode='CONDENSER_OUTPUT_TRASH', operationMode='ARROW_RIGHT',
             numberEntryButtonConfig='COG', taskPriority='PRIORITY', taskSubscription='COG',
             trash='CONDENSER_OUTPUT_TRASH', matterBalls='CONDENSER_OUTPUT_MATTER_BALL', singularity='CONDENSER_OUTPUT_SINGULARITY',
             clear='CLEAR', sort='SORT_BY_NAME', terminalStyle='TERMINAL_STYLE_SMALL')
LABELS = dict(start='Start', cancel='Cancel', save='Set', next='Next', selectCpu='CPUs',
              selectCpuList='SelectFromList', bookmarkMissing='BookmarkMissing', suspend='Suspend',
              replan='CraftErrorReplan', retry='CraftErrorRetry', set='Set',
              resetDefaults='NumberEntryButtonSettingsReset', magnetSettingsButton='WirelessMagnetConfigure', release='ResetRestriction')
LABELS.update(replace='PatternModifierReplaceButton',clear='PatternModifierClear')


def inherited(name):
    seen = set(); widgets = {}; toolbar = []; chain = []
    while name in CLASSES and name not in seen:
        seen.add(name); chain.insert(0, CLASSES[name]); name = CLASSES[name]['parent']
    for layer in chain:
        widgets.update(layer['widgets']); toolbar.extend(layer['toolbar'])
    return widgets, list(dict.fromkeys(toolbar))


def slot_count(id, semantic, source, width, height):
    if semantic == 'PLAYER_INVENTORY': return 27
    if semantic == 'PLAYER_HOTBAR': return 9
    if semantic in ('TOOLBOX', 'WIRELESS_SINGULARITY'): return 0
    counts = {
        'drive': {'STORAGE_CELL': 10}, 'sky_chest': {'STORAGE': 36},
        'cell_workbench': {'CONFIG': 63}, 'portable_workbench': {'CONFIG': 63},
        'pattern_provider': {'ENCODED_PATTERN': 36, 'STORAGE': 9},
        'molecular_assembler': {'ENCODED_PATTERN': 36},
        'interface': {'CONFIG': 18, 'STORAGE': 18},
        'io_port': {'MACHINE_INPUT': 6, 'MACHINE_OUTPUT': 6},
        'ingredient_buffer': {'STORAGE': 27}, 'wireless_access_point': {'STORAGE': 1},
        'network_tool': {'STORAGE': 9}, 'pickup_filter': {'PORTABLE_CELL_PICKUP_FILTER': 27},
        'wireless_magnet': {'MAGNET_PICKUP_CONFIG': 9, 'MAGNET_INSERT_CONFIG': 9},
        'crystal_assembler': {'STORAGE': 3},
    }
    if semantic in counts.get(id, {}): return counts[id][semantic]
    if semantic in ('CRAFTING_GRID', 'PROCESSING_INPUTS'): return 9
    if semantic == 'PROCESSING_OUTPUTS': return 3
    if semantic == 'CONFIG':
        return 9 if source.get('grid') == 'IO_BUS_CONFIG' else 63 if source.get('grid') == 'BREAK_AFTER_9COLS' else 1
    return 1


def appearance(layouts, row, lesson):
    id = row['id']; cls = row['screen'].rsplit('.', 1)[-1]; style = layouts.style(row['style'])
    (width, height), texture = layouts.dimensions(style, cls)
    # Fixed three-row terminal and request examples. These sizes include their native footer.
    if cls in ('GuiRequester', 'GuiRequesterTerm'): width, height = 195, 215
    if cls == 'GuiCellTerminal': width, height = 208, 225
    if cls == 'GuiPatternAccessTerm': width, height = 213, 201
    if cls == 'GuiPEATerm': width, height = 213, 282
    if cls == 'GuiAdvancedMemoryCard': width, height = 256, 196
    if cls == 'GuiCraftingTree': width, height = 256, 220
    widgets, toolbar = inherited(cls)
    if cls == 'GuiTerminalSettings': toolbar = ['COG', 'TERMINAL_SEARCH_SETTINGS', 'WIRELESS_SETTINGS_PAGE']
    if cls in ('GuiPatternAccessTerm','GuiPEATerm'): toolbar = ['TERMINAL_STYLE_SMALL','COG','PATTERN_TERMINAL_VISIBLE']
    if cls == 'GuiCraftingStatus': toolbar = []  # This screen uses its CPU selection panel instead.
    for key in ('openPriority','back','returnToParent','generationRateBar'):
        if key in style.get('widgets', {}): widgets.setdefault(key, {'kind':'add'})
    for key in style.get('widgets', {}):
        if key.startswith('side_'): widgets[key] = {'kind':'add','icon':'OUTPUT_SIDE_CONFIG'}
    if cls in ('GuiPatternEncodingTerm', 'GuiPEATerm'):
        panel = 'ProcessingEncodingPanel' if id == 'pattern_processing' else 'CraftingEncodingPanel'
        widgets.update(CLASSES[panel]['widgets'])
        widgets.update({k: {'kind': 'add'} for k in ('modeTabButton0', 'modeTabButton1', 'modePanel0', 'modePanel1')})
    if cls == 'GuiAdvancedMemoryCard': widgets.update({k: {'kind': 'addTextField' if k == 'search' else 'add'} for k in ('search','scrollbar','entryList')})
    active = {}
    for key, source in style.get('widgets', {}).items():
        if key in COMMON_OPTIONAL or key.startswith(('patternModifierPanel', 'providerSelection')): continue
        if key in ('verticalToolbar', 'upgrades'): continue
        if key not in widgets and key not in NUMBERS and not any(key == n+'Input' or key == n+'Preview' for n in NUMBERS): continue
        if key.startswith('processing') and id != 'pattern_processing': continue
        if key.startswith('crafting') and key != 'craftingStatus' and cls in ('GuiPatternEncodingTerm', 'GuiPEATerm') and id == 'pattern_processing': continue
        if key in ('modePanel0', 'modePanel1') and key != ('modePanel1' if id == 'pattern_processing' else 'modePanel0'): continue
        if key in ('lockReason', 'emptyMessage'): continue
        x, y = point(source, width, height); spec = widgets.get(key, {})
        w, h = source.get('width', 0), source.get('height', 0)
        kind = spec.get('kind', 'add')
        if key in NUMBERS: kind = 'number'
        elif key.endswith('Preview'): continue  # Native number widget owns its preview and visibility.
        elif key.endswith('Input') or kind == 'addTextField': kind = 'field'
        elif kind == 'addCheckbox': kind = 'checkbox'
        elif 'scrollbar' in key.lower(): kind = 'scrollbar'; w, h = 12, h or max(16, height-y-(100 if 'PLAYER_INVENTORY' in style.get('slots', {}) else 30))
        elif key in ('progressBar','generationRateBar'): kind = 'progress'; w, h = 6, 18
        elif key.startswith('modePanel'): kind = 'encoding'; w, h = 124, 66
        elif key == 'entryList': kind = 'memory'; w, h = 229, 132
        elif key == 'keytypes': kind = 'keytypes'; w, h = 150, 64
        elif key == 'viewCells': kind = 'viewcells'; w, h = 24, 102
        elif key == 'linkPanel':
            kind = 'panel'; w, h = style['images'][key]['srcRect'][2:4]
        elif key == 'selectCpuList' and cls == 'GuiCraftingStatus': kind = 'cpulist'; w, h = 103, height
        elif key == 'color_window': kind = 'colorwindow'
        elif key.startswith('color_') and key[-1:].isdigit(): kind = 'color'
        else: kind = 'button'
        if kind == 'field' and any(key == n+'Input' for n in NUMBERS): continue
        if key in ('craftingClearPattern','craftingSubstitutions','craftingFluidSubstitutions','processingCycleOutput','processingClearPattern','processingMergeHeiInputs','clearCraftingGrid','clearToPlayerInv'): w,h=8,8
        if key=='scrollbar':
            if style.get('terminalStyle'): h=52
            elif cls=='GuiCellTerminal': h=108
            elif cls in ('GuiRequester','GuiRequesterTerm'): h=96
        active[key] = dict(kind=kind, x=x, y=y, width=w or 16, height=h or 16,
                           icon=ICONS.get(key, spec.get('icon', '')), label=LABELS.get(key, spec.get('label','')), text=spec.get('text',''))
    if cls == 'GuiCellTerminal':
        for index in range(8):
            active['cellTab'+str(index)] = dict(kind='celltab',x=4+index*24,y=-19,width=22,height=22,icon='',label='',text='')
    if cls == 'GuiCraftingTree':
        for key, icon in [('tree',''),('back','BACK'),('missingOnly','CRAFTING_TREE_BRANCHES_FAILED'),('screenshot','CRAFTING_TREE_SCREENSHOT')]:
            _, (x,y,w,h) = target_geometry(style,'widget.'+key,width,height)
            active[key] = dict(kind='canvas' if key=='tree' else 'button',x=x,y=y,width=w,height=h,icon=icon,label='',text='')
    # Hidden side panels stay closed. Core toolbar and upgrade slots remain part of the viewport.
    upgrades = UPGRADES.get(id, 0)
    if toolbar:
        toolbar = [v for v in toolbar if v not in ('PATTERN_MODIFIER','TYPE_FILTER_ALL')] + (['TYPE_FILTER_ALL'] if 'TYPE_FILTER_ALL' in toolbar else [])
    slots = {}
    for semantic, source in style.get('slots', {}).items():
        if source.get('hidden'): continue
        if semantic.startswith('PROCESSING') and id != 'pattern_processing': continue
        if semantic.startswith('CRAFTING_') and id == 'pattern_processing': continue
        for index in range(slot_count(id, semantic, source, width, height)):
            key = f'slot.{semantic}.{index}'
            _, bounds = target_geometry(style, key, width, height)
            x, y, w, h = bounds
            if 0 <= x < width-8 and 0 <= y < height-8: slots[key] = [x,y,w,h]
    if style.get('terminalStyle'):
        for index in range(27): slots['repo.'+str(index)] = [8+index%9*18,18+index//9*18,16,16]
    # A complete appearance is also authoritative for highlight geometry.
    for key, target in lesson['targets'].items():
        if key in slots: bounds = slots[key]
        elif key.startswith('widget.') and key[7:] in active:
            widget = active[key[7:]]; bounds = [widget[k] for k in ('x','y','width','height')]
        elif key == 'widget.verticalToolbar': bounds = [-17,1,20,max(20,len(toolbar)*22+2)]
        elif key == 'widget.upgrades': bounds = [width+1,0,29,max(30,upgrades*18+12)]
        else:
            try: _, bounds = target_geometry(style,key,width,height)
            except ValueError: bounds = [target[k] for k in ('x','y','width','height')]
        target.update(zip(('x','y','width','height'), bounds))
    left = min([0, -19 if toolbar else 0] + [v['x'] for v in active.values()] + [v['x'] for v in lesson['targets'].values()]) - 4
    top = min([0] + [v['y'] for v in active.values()] + [v['y'] for v in lesson['targets'].values()]) - 4
    right = max([width + (32 if upgrades else 0)] + [v['x']+v['width'] for v in active.values()] + [v['x']+v['width'] for v in lesson['targets'].values()]) + 4
    bottom = max([height,len(toolbar)*22+6] + [v['y']+v['height'] for v in active.values()] + [v['y']+v['height'] for v in lesson['targets'].values()]) + 4
    for target in lesson['targets'].values(): target['x'] -= left; target['y'] -= top
    lesson.update(width=right-left, height=bottom-top, texture=texture)
    return dict(width=width,height=height,x=-left,y=-top,style=row['style'],screen=cls,
                widgets=active,toolbar=toolbar,upgrades=upgrades,slots=slots,texture=texture)
