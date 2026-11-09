#!/usr/bin/env python3
"""Original AE2S 1.1.0 GUI lessons shared by scene clips, guide cards and live W guidance."""
import argparse
import json
from pathlib import Path
from gui_catalog import CATALOG, LEGACY
from gui_layouts import Layouts, BASE_CLASSES, target_geometry

ASSETS = Path(__file__).resolve().parents[1] / 'src/main/resources/assets/ae2s_ponder'
LANG_MARKER = '# Generated GUI lessons (tools/generate-guis.py)'
LESSONS = {}
TRANSLATIONS = {'en_us': {}, 'zh_cn': {}}


def text(lesson, suffix, en, zh):
    key = f'ae2s_ponder.gui.{lesson}.{suffix}'
    TRANSLATIONS['en_us'][key] = en
    TRANSLATIONS['zh_cn'][key] = zh
    return '@' + key


def lesson(id, en, zh, screen, texture, height, components, width=176):
    value = {'format': 1, 'id': 'ae2s_ponder:' + id, 'title': text(id, 'title', en, zh),
             'components': ['ae2:' + c for c in components], 'screen': screen, 'adapter': 'ae2s',
             'width': width, 'height': height, 'texture': 'ae2:textures/guis/' + texture + '.png',
             'targets': {}, 'steps': []}
    LESSONS[id] = value
    return value


def target(lesson, key, x, y, en, zh, type='slot', width=16, height=16, item='', count=0):
    id = lesson['id'].split(':')[1]
    lesson['targets'][key] = {'type': type, 'x': x, 'y': y, 'width': width, 'height': height,
                              'label': text(id, 'target.' + key, en, zh), 'item': item, 'count': count}
    return key


def step(lesson, key, en, zh, wait=None, demo=()):
    id = lesson['id'].split(':')[1]
    lesson['steps'].append({'title': lesson['targets'][key]['label'],
                           'text': text(id, 'step.' + str(len(lesson['steps'])), en, zh),
                           'target': key, 'duration': 75, 'wait': wait or {'type': 'next'}, 'demo': list(demo)})


def put(key, item='', count=1, at=20):
    return {'op': 'set_slot', 'target': key, 'item': item, 'count': count if item else 0, 'at': at}


def value(key, data, at=20):
    return {'op': 'set_value', 'field': key, 'value': data, 'at': at}


def has(item=''):
    return {'type': 'slot_has', 'item': item}


d = lesson('drive', 'ME Drive: insert storage', 'ME 驱动器：安装存储',
           'ae2.client.gui.implementations.GuiDrive', 'drive', 201, ['drive', 'item_storage_cell_1k', 'item_storage_cell_64k'])
cell = target(d, 'slot.STORAGE_CELL.0', 71, 14, 'Storage cell slot', '存储元件槽')
other = target(d, 'slot.STORAGE_CELL.1', 89, 14, 'Additional cell', '更多存储元件')
step(d, cell, 'Insert an ME storage cell. The drive needs network power and a channel before the terminal can use it.',
     '放入 ME 存储元件。驱动器还需要网络供电与频道，终端才能使用其中的存储。', has(), [put(cell, 'ae2:item_storage_cell_1k')])
step(d, other, 'The ten slots hold independent cells. Add a larger cell when bytes or available types run short.',
     '十个槽位分别容纳独立存储元件。字节或类型空间不足时，可增加容量或安装更多元件。', demo=[put(other, 'ae2:item_storage_cell_64k')])
step(d, cell, 'Cell contents stay on the cell when you remove it. Keep a backup before reorganizing your storage.',
     '移除存储元件时，数据仍保存在元件内。整理存储前先备份，不要把元件当作空壳丢弃。')
step(d, cell, 'Close this window and open the ME Terminal to test insertion and extraction. A drive is not a direct item input.',
     '关闭驱动器，打开 ME 终端测试存取。驱动器的槽位用于安装元件，不是直接投入普通物品的入口。')

d = lesson('terminal', 'ME Terminal: search and transfer', 'ME 终端：检索与存取',
           'ae2.client.gui.me.common.GuiMEStorage', 'terminal', 170, ['terminal', 'crafting_terminal'], 195)
search = target(d, 'widget.search', 80, 4, 'Search', '搜索框', 'region', 89, 12)
stock = target(d, 'repo.0', 8, 18, 'Network stock', '网络库存')
player = target(d, 'slot.PLAYER_INVENTORY.0', 8, 88, 'Player inventory', '玩家背包')
step(d, search, 'Click the search box and enter part of an item name. While typing, W stays available as a search character; click outside before holding W for guidance.',
     '点击搜索框输入物品名称。输入时 W 保持作为搜索字符；点击输入框外，再长按 W 可进入引导。',
     {'type': 'click'}, [value(search, 'iron'), put(stock, 'minecraft:iron_ingot', 64)])
step(d, stock, 'The item grid shows this network\'s stored and craftable entries. Click a stocked item to take it; craftable entries can start a request.',
     '物品区显示当前网络的库存与可合成条目。点击已有库存可取出物品，点击可合成条目可发起任务。', demo=[put(stock, 'minecraft:iron_ingot', 64)])
step(d, player, 'Transfer items between your inventory and network storage. The demonstration uses separate items and does not move your real inventory.',
     '在背包与网络之间存取物品。演示中的物品是独立数据，不会移动你真实背包中的物品。', demo=[put(stock, 'minecraft:iron_ingot', 32), put(player, 'minecraft:iron_ingot', 32)])
step(d, search, 'Clear the search to see everything again. If the terminal is offline, check power, cable connections, channels and loaded chunks.',
     '清空搜索可重新显示全部条目。终端离线时，检查电力、线缆、频道和区块加载。', demo=[value(search, '')])

d = lesson('cell_workbench', 'Cell Workbench: configure a partition', '存储元件工作台：配置分区',
           'ae2.client.gui.implementations.GuiCellWorkbench', 'cellworkbench', 253, ['cell_workbench'])
cell = target(d, 'slot.STORAGE_CELL.0', 152, 8, 'Cell to configure', '待配置存储元件')
config = target(d, 'slot.CONFIG.0', 8, 29, 'Partition filter', '分区过滤标记')
step(d, cell, 'Insert the storage cell you want to configure. Read its current contents before changing restrictions.',
     '放入需要配置的存储元件，修改限制前先核对原有内容。', has(), [put(cell, 'ae2:item_storage_cell_1k')])
step(d, config, 'Set the item filters in the configuration grid. These are ghost entries; they select allowed types and do not supply stored items.',
     '在配置网格设置允许存入的物品。这里是过滤标记，不会凭空提供库存，也不代表消耗这些物品。', demo=[put(config, 'minecraft:iron_ingot')])
step(d, config, 'Use supported cell upgrades only when needed. Page buttons appear for cells with more filter entries; live highlights follow the visible slots.',
     '按需使用元件支持的升级卡。过滤槽较多时会显示翻页按钮，实机高亮会跟随当前可见槽位。')
step(d, cell, 'Remove the configured cell and put it back into the drive. Confirm that allowed items enter it and other types use a different cell.',
     '取出配置好的元件，放回驱动器。检查目标物品能够存入，其他类型由另一块元件接收。',
     {'type': 'slot_empty'}, [put(cell)])

d = lesson('inscriber', 'Inscriber: print a silicon circuit', '压印器：压印硅板',
           'ae2.client.gui.implementations.GuiInscriber', 'inscriber', 178, ['inscriber', 'silicon_press'])
press = target(d, 'slot.INSCRIBER_PLATE_TOP.0', 39, 23, 'Upper press slot', '上部压印模板槽')
lower = target(d, 'slot.INSCRIBER_PLATE_BOTTOM.0', 39, 55, 'Lower press slot', '下部压印模板槽')
input = target(d, 'slot.MACHINE_INPUT.0', 63, 39, 'Input material', '输入原料')
progress = target(d, 'progress', 135, 39, 'Processing progress', '加工进度', 'region', 12, 18)
output = target(d, 'slot.MACHINE_OUTPUT.0', 113, 40, 'Printed result', '压印产物')
step(d, press, 'Put the Silicon Press in the upper press slot. Leave the lower slot empty for this printing recipe; the press is reusable.',
     '在上部模板槽放入硅压印模板。本次压印配方下部槽留空，模板可以重复使用。', has('ae2:silicon_press'), [put(press, 'ae2:silicon_press')])
step(d, input, 'Insert silicon into the middle input. Check the installed recipe viewer if your pack changes the material.',
     '向中间输入槽放入硅；整合包修改原料时，以实际配方查看器为准。', has('ae2:silicon'), [put(input, 'ae2:silicon')])
step(d, progress, 'Supply power and wait for real machine progress. The live guide observes synchronized progress or a completed output, including fast upgraded machines.',
     '为压印器供能并等待加工。实机引导观察同步进度或已完成的产物，也可识别升级后快速完成的工序。',
     {'type': 'value_at_least', 'field': 'inscriber.work_observed', 'value': '1'}, [value('inscriber.progress', '50'), value('inscriber.work_observed', '1'), value(progress, '50%')])
step(d, output, 'The Printed Silicon appears in the output. Combine it with a printed circuit and redstone in a separate assembly operation.',
     '硅板会出现在输出槽，下一道工序再与电路、红石组合为处理器。', has('ae2:printed_silicon'), [put(input), put(output, 'ae2:printed_silicon'), value(progress, '100%')])
step(d, output, 'Collect the result while leaving the press installed. For automation, verify each accessible machine face with one test item.',
     '取走产物，保留机器中的模板。自动化前，用一个测试物品逐面核对输入输出。', {'type': 'slot_empty'}, [put(output)])

for processing in (False, True):
    id = 'pattern_processing' if processing else 'pattern_crafting'
    d = lesson(id, 'Pattern Terminal: ' + ('processing' if processing else 'crafting'),
               '样板终端：' + ('处理样板' if processing else '合成样板'),
               'ae2.client.gui.me.patternencode.GuiPatternEncodingTerm', 'pattern', 251,
               ['pattern_encoding_terminal', 'processing_pattern' if processing else 'crafting_pattern', 'blank_pattern'], 195)
    mode = target(d, 'widget.modeTabButton' + ('1' if processing else '0'), 173, 98 if processing else 77,
                  'Processing mode' if processing else 'Crafting mode', '处理模式' if processing else '合成模式', 'button', 22, 22)
    blank = target(d, 'slot.BLANK_PATTERN.0', 147, 86, 'Blank pattern', '空白样板')
    inputs = []
    if processing:
        inputs.append(target(d, 'slot.PROCESSING_INPUTS.0', 24, 93, 'Consumed material', '消耗的原料'))
        result = target(d, 'slot.PROCESSING_OUTPUTS.0', 109, 93, 'Expected product', '预期产物')
        for_recipe = [put(inputs[0], 'minecraft:iron_ore'), put(result, 'minecraft:iron_ingot')]
    else:
        for i in range(9):
            inputs.append(target(d, f'slot.CRAFTING_GRID.{i}', 15 + (i % 3) * 18, 93 + (i // 3) * 18,
                                 'Crafting ingredient', '合成原料'))
        result = target(d, 'slot.CRAFTING_RESULT.0', 106, 111, 'Recipe result', '配方产物')
        for_recipe = [put(key, 'minecraft:iron_ingot') for key in inputs] + [put(result, 'minecraft:iron_block')]
    encode = target(d, 'widget.encodePattern', 147, 106, 'Encode', '编码', 'button', 16, 16)
    encoded = target(d, 'slot.ENCODED_PATTERN.0', 147, 133, 'Encoded pattern', '已编码样板')
    step(d, mode, 'Choose Processing for an external machine recipe.' if processing else 'Choose Crafting for a crafting-grid recipe.',
         '选择处理模式，用于外部机器的加工配方。' if processing else '选择合成模式，用于合成网格配方。',
         {'type': 'value_equals', 'field': 'pattern.mode', 'value': 'PROCESSING' if processing else 'CRAFTING'},
         [value('pattern.mode', 'PROCESSING' if processing else 'CRAFTING'), {'op': 'click', 'target': mode, 'at': 20}])
    step(d, blank, 'Insert a blank pattern. The guide observes this real slot and never places an item for you.',
         '放入空白样板。实机引导只观察真实槽位，不会替你放入物品。', has('ae2:blank_pattern'), [put(blank, 'ae2:blank_pattern')])
    step(d, inputs[0], 'Specify exactly the consumed inputs and expected outputs. Keep reusable presses installed in the machine; do not list them as consumed ingredients.' if processing else 'Fill the recipe grid and verify the resulting item. These are recipe entries; ingredients are supplied when a crafting request executes.',
         '填写准确的输入、输出和数量。留在机器内重复使用的模板，不应列为每次消耗的原料。' if processing else '填写合成网格并核对产物。这里记录配方，实际原料在发起合成任务后才会供应。', demo=for_recipe)
    step(d, encode, 'Click Encode after checking mode, ingredients and output. Encoding still requires a valid recipe and a blank pattern.',
         '核对模式、原料与产物后点击编码。编码仍需有效配方与空白样板。', {'type': 'slot_has', 'target': encoded},
         [{'op': 'click', 'target': encode, 'at': 20}, put(blank), put(encoded, 'ae2:processing_pattern' if processing else 'ae2:crafting_pattern')])
    step(d, encoded, 'Take the encoded pattern and install it in a Pattern Provider. Processing outputs must return to the same requesting network.' if processing else 'Take the encoded pattern and install it in a Pattern Provider beside a Molecular Assembler; the network also needs a Crafting CPU.',
         '取出已编码样板，装入样板供应器。处理产物必须回到发起任务的同一网络。' if processing else '取出已编码样板，装入紧邻分子装配室的样板供应器；网络还需要合成 CPU。',
         {'type': 'slot_empty'}, [put(encoded)])

d = lesson('pattern_provider', 'Pattern Provider: install and return', '样板供应器：安装与回网',
           'ae2.client.gui.implementations.GuiPatternProvider', 'pattern_provider', 245, ['pattern_provider', 'cable_pattern_provider'])
pattern = target(d, 'slot.ENCODED_PATTERN.0', 8, 42, 'Encoded patterns', '已编码样板槽')
buffer = target(d, 'slot.STORAGE.0', 8, 127, 'Return buffer', '回网缓冲槽')
priority = target(d, 'widget.openPriority', 152, -5, 'Priority', '优先级', 'button', 20, 20)
step(d, pattern, 'Insert a matching encoded pattern. A crafting pattern uses a Molecular Assembler; a processing pattern delivers ingredients to the adjacent machine.',
     '装入已编码样板。合成样板使用分子装配室，处理样板则向相邻机器发送原料。', has(), [put(pattern, 'ae2:processing_pattern')])
step(d, buffer, 'The return buffer receives products for the network. A separate Import Bus can also return products to the same network.',
     '回网缓冲用于接收产物并送入网络，也可用独立输入总线将产物导回同一网络。', demo=[put(buffer, 'minecraft:iron_ingot')])
step(d, priority, 'Set priority only when several providers offer the recipe. Check target orientation and blocking mode before increasing parallel work.',
     '多个供应器提供同一配方时可调整优先级。增加并行前，先检查朝向、目标输入面与阻挡模式。')
step(d, buffer, 'Request one batch and confirm the exact product returns. The task waits until the requesting network receives it.',
     '先请求一批，确认准确产物完成回网。发起任务的网络收到预期产物后，任务才会继续。', demo=[put(buffer)])

d = lesson('interface', 'ME Interface: stock and insert', 'ME 接口：备货与存入',
           'ae2.client.gui.implementations.GuiInterface', 'interface', 253, ['interface', 'cable_interface'])
config = target(d, 'slot.CONFIG.0', 8, 53, 'Requested stock', '期望库存配置')
stock = target(d, 'slot.STORAGE.0', 8, 71, 'Local inventory', '本地实物库存')
step(d, config, 'Configure the desired item and amount in a ghost slot. This entry requests stock; it is not an already supplied item.',
     '在配置槽设置物品与期望数量。这是请求库存的标记，不是已经提供的真实物品。', demo=[put(config, 'minecraft:iron_ingot', 16)])
step(d, stock, 'With network power, a channel and enough stored items, the interface replenishes its real local inventory.',
     '网络具备电力、频道和足够库存时，接口会补充本地实物库存。', has('minecraft:iron_ingot'), [put(stock, 'minecraft:iron_ingot', 16)])
step(d, stock, 'Let the adjacent machine consume from the real inventory. Avoid routing those same items straight back into the interface.',
     '让相邻机器从实物库存取用，避免管道将同批物品立即送回接口，形成循环。', demo=[put(stock, 'minecraft:iron_ingot', 8)])
step(d, stock, 'An interface can accept machine output into network storage. Use a Pattern Provider for processing-pattern ingredient delivery.',
     '接口也可接收机器产物并存入网络。按处理样板投送原料，应使用样板供应器。', demo=[put(stock, 'minecraft:iron_ingot', 16)])


def expanded():
    layouts = Layouts()
    rows = []
    for id, (cls, style, category, scene) in LEGACY.items():
        rows.append(dict(id=id, screen=layouts.screen(cls), style='/screens/'+style+'.json', category=category,
                         scene=scene, components=[c.split(':',1)[1] for c in LESSONS[id]['components']],
                         widgets=list(layouts.style(style).get('widgets',{})), host=''))
    for source in CATALOG:
        id = source['id']; cls = source['cls']; style = layouts.style(source['style'])
        (width,height), texture = layouts.dimensions(style,cls)
        d = dict(format=1, id='ae2s_ponder:'+id, title=text(id,'title',*source['title']),
                 components=['ae2:'+c for c in source['components']], screen=layouts.screen(cls),
                 adapter='ae2s',width=width,height=height,texture=texture,targets={},steps=[])
        for index, operation in enumerate(source['steps']):
            key = operation['target']
            if key not in d['targets']:
                kind, (x,y,w,h) = target_geometry(style,key,width,height)
                d['targets'][key]=dict(type=kind,x=x,y=y,width=w,height=h,
                    label=text(id,'target.'+key,*operation['label']),item='',count=0)
            demo=[]
            if operation['item']:
                if d['targets'][key]['type']!='slot':raise ValueError('Demo item requires a slot: '+id+' '+key)
                demo.append(put(key,operation['item'],operation['count']))
            if operation['sample']:demo.append(value(key,operation['sample']))
            step(d,key,*operation['text'],wait=operation['wait'],demo=demo)
        LESSONS[id]=d
        rows.append(dict(id=id,screen=d['screen'],style='/screens/'+source['style']+'.json' if source['style'] else '',
                         category=source['category'],scene=source['scene'],components=source['components'],
                         widgets=list(style.get('widgets',{})),host=source.get('host','')))
    covered={r['screen'] for r in rows}
    missing=set(layouts.concrete_screens())-covered
    if missing:raise ValueError('Native GUI without an authored lesson: '+repr(sorted(missing)))
    for row in rows:row['subject']=layouts.subject(row['components'][0])
    return dict(ae2s='1.1.0',runtime_sha256=layouts.sha256,native_screens=layouts.concrete_screens(),
                implementation_bases=BASE_CLASSES,lessons=rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    coverage=expanded()
    from gui_demo_layouts import appearance
    layouts = Layouts()
    appearances = {row['id']: appearance(layouts,row,LESSONS[row['id']]) for row in coverage['lessons']}
    files = {f'ponder/gui/{id}.json': json.dumps(data, ensure_ascii=False, indent=2) + '\n' for id, data in LESSONS.items()}
    files['ponder/gui/appearances.json'] = json.dumps(appearances, ensure_ascii=False, indent=2) + '\n'
    files['ponder/gui/index.json'] = json.dumps({'tutorials': ['ae2s_ponder:' + id for id in LESSONS]}, indent=2) + '\n'
    files['ponder/gui/coverage.json']=json.dumps(coverage,ensure_ascii=False,indent=2)+'\n'
    for code, entries in TRANSLATIONS.items():
        relative = f'lang/{code}.lang'
        original = (ASSETS / relative).read_text().split(LANG_MARKER)[0].rstrip()
        files[relative] = original + '\n\n' + LANG_MARKER + '\n' + ''.join(f'{k}={v}\n' for k, v in entries.items())
    for relative, content in files.items():
        path = ASSETS / relative
        if args.check:
            if not path.is_file() or path.read_text() != content:
                raise SystemExit('GUI resource differs: ' + str(path))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    print(f'{len(LESSONS)} shared bilingual GUI lessons verified' if args.check else 'Generated shared GUI lessons')


if __name__ == '__main__':
    main()
