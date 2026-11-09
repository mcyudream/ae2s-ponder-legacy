"""Read UI geometry and class inheritance from the exact pinned AE2S runtime artifact."""
from pathlib import Path
from zipfile import ZipFile
import copy
import hashlib
import json
import posixpath
import re
import struct

ROOT = Path(__file__).resolve().parents[1]
BASE_CLASSES = {'ae2.client.gui.implementations.' + name: 'Shared implementation; concrete variants have their own lessons.'
                for name in ('GuiUpgradeable', 'GuiSpecialStorageBus', 'GuiSpecialExportBus')}
PARTS=set('terminal cell_terminal crafting_terminal pattern_encoding_terminal pattern_access_terminal pattern_encoding_access_terminal requester_terminal storage_bus import_bus export_bus od_storage_bus od_export_bus mod_storage_bus mod_export_bus precise_storage_bus precise_export_bus threshold_export_bus stock_export_bus import_export_bus advanced_io_bus formation_plane annihilation_plane level_emitter energy_level_emitter threshold_level_emitter'.split())


def class_info(data):
    cursor = 8
    size = struct.unpack_from('>H', data, cursor)[0]
    cursor += 2
    pool = [None] * size
    i = 1
    while i < size:
        tag = data[cursor]
        cursor += 1
        if tag == 1:
            length = struct.unpack_from('>H', data, cursor)[0]
            cursor += 2
            pool[i] = data[cursor:cursor + length].decode('utf-8', 'replace')
            cursor += length
        elif tag in (7, 8, 16, 19, 20):
            pool[i] = struct.unpack_from('>H', data, cursor)[0]
            cursor += 2
        elif tag in (3, 4, 9, 10, 11, 12, 17, 18):
            cursor += 4
        elif tag in (5, 6):
            cursor += 8
            i += 1
        elif tag == 15:
            cursor += 3
        else:
            raise ValueError('Unknown class constant tag: ' + str(tag))
        i += 1
    flags, this, parent = struct.unpack_from('>HHH', data, cursor)
    return dict(name=pool[pool[this]].replace('/', '.'),
                parent=pool[pool[parent]].replace('/', '.') if parent else '', abstract=bool(flags & 0x400))


class Layouts:
    def __init__(self):
        lock = json.loads((ROOT / 'dependency-lock.json').read_text())['ae2s']['runtime']
        jar = ROOT / 'libs' / lock['file']
        if hashlib.sha256(jar.read_bytes()).hexdigest() != lock['sha256']:
            raise ValueError('GUI catalog requires the pinned AE2S runtime jar')
        self.sha256 = lock['sha256']
        self.jar = ZipFile(jar)
        self.classes = {v['name']: v for name in self.jar.namelist()
                        if name.startswith('ae2/client/') and name.endswith('.class')
                        for v in [class_info(self.jar.read(name))]}
        self.styles = {}

    def concrete_screens(self):
        def native(name):
            visited = set()
            while name in self.classes and name not in visited:
                if name == 'ae2.client.gui.AEBaseGui':
                    return True
                visited.add(name)
                name = self.classes[name]['parent']
            return False
        return sorted(name for name, info in self.classes.items()
                      if '$' not in name and not info['abstract'] and name not in BASE_CLASSES and native(name))

    def screen(self, simple):
        found = [name for name in self.classes if name.rsplit('.', 1)[-1] == simple]
        if len(found) != 1:
            raise ValueError('Missing or ambiguous native screen: ' + simple)
        return found[0]

    def subject(self,component):
        kind='block' if 'assets/ae2/blockstates/'+component+'.json' in self.jar.namelist() else 'part' if component in PARTS else 'item'
        return dict(kind=kind,id=component)

    def style(self, path):
        if not path:
            return {}
        if not path.startswith('/'):
            path = '/screens/' + path + '.json'
        path = posixpath.normpath(path)
        if path in self.styles:
            return self.styles[path]
        source = json.loads(self.jar.read('assets/ae2' + path))
        layers = [self.style(posixpath.normpath(posixpath.dirname(path) + '/' + inc))
                  for inc in source.get('includes', [])] + [source]
        # Match GuiStyleManager: merge named entries, replace the full value of an overridden entry.
        result = {}
        maps = {'slots', 'text', 'palette', 'images', 'terminalStyle', 'widgets', 'tooltips'}
        for layer in layers:
            for key, value in layer.items():
                if key in maps:
                    result.setdefault(key, {}).update(copy.deepcopy(value))
                else:
                    result[key] = copy.deepcopy(value)
        self.styles[path] = result
        return result

    def dimensions(self, style, cls):
        background = style.get('background', {})
        if 'srcRect' in background:
            texture='ae2:textures/'+background['texture']
            data=self.jar.read('assets/ae2/textures/'+background['texture'])
            return background['srcRect'][2:4], texture
        generated = style.get('generatedBackground')
        if generated:
            return [generated.get('width', 200), generated.get('height', 160)], ''
        terminal = style.get('terminalStyle', {})
        if all(key in terminal for key in ('header', 'firstRow', 'row', 'lastRow', 'bottom')):
            return [terminal['header']['srcRect'][2], sum(terminal[k]['srcRect'][3]
                    for k in ('header', 'firstRow', 'row', 'lastRow', 'bottom'))], 'ae2:textures/' + terminal['header']['texture']
        special = {
            'GuiCraftingPattern': ([176,109], 'crafting_pattern_recipe'),
            'GuiProcessingPattern': ([176,251], 'processing_pattern_recipe'),
            'GuiCraftingTree': ([256,256], 'crafting_tree'),
            'GuiAdvancedMemoryCard': ([256,196], 'advanced_memory_card'),
            'GuiRequester': ([195,210], 'requester'),
            'GuiRequesterTerm': ([195,210], 'requester_terminal'),
            'GuiCellTerminal': ([211,220], 'cell_terminal')
        }
        size, texture = special.get(cls, ([200,160], ''))
        return size, 'ae2:textures/guis/' + texture + '.png' if texture else ''


def point(position, width, height):
    return position.get('left', width - position.get('right', width)), position.get('top', height - position.get('bottom', height))


def target_geometry(style, key, width, height):
    if key.startswith('repo.'):
        index=int(key[5:]);return 'slot',[8+(index%9)*18,18+(index//9)*18,16,16]
    if key.startswith('slot.'):
        _, semantic, index = key.split('.')
        source = style.get('slots', {}).get(semantic)
        if source is None:
            raise ValueError('No native semantic layout for ' + key)
        x, y = point(source, width, height)
        index = int(index)
        grid = source.get('grid', 'HORIZONTAL')
        cols = re.search(r'BREAK_AFTER_(\d+)COLS', grid)
        if cols:
            count = int(cols.group(1)); x += index % count * 18; y += index // count * 18
        elif grid == 'VERTICAL':
            y += index * 18
        elif grid == 'IO_BUS_CONFIG':
            offsets = [(0,0),(-18,0),(18,0),(0,-18),(0,18),(-18,-18),(18,-18),(-18,18),(18,18)]
            dx, dy = offsets[index % 9]; x += dx; y += dy
        else:
            x += index * 18
        return 'slot', [x,y,16,16]
    if key.startswith('widget.'):
        id = key[7:]
        source = style.get('widgets', {}).get(id)
        if source is None:
            if id == 'tree': return 'region',[8,28,width-16,height-36]
            if id in ('screenshot','missingOnly','back'):
                return 'button',[8 + ('back','missingOnly','screenshot').index(id)*24,4,20,20]
            raise ValueError('No native widget layout for ' + key)
        x, y = point(source,width,height)
        w, h = source.get('width',20), source.get('height',20)
        w=max(8,w or 20);h=max(10,h or 20)
        type = 'region' if h<=14 or id in ('scrollbar','tree','upgrades','verticalToolbar','level','upperLevel','lowerLevel','priority','amountToCraft','amountToStock','workInterval','keytypes','color_window','progressBar','generationRateBar') else 'button'
        return type,[x,y,w,h]
    if key.startswith('text.'):
        source=style.get('text',{}).get(key[5:])
        if source is None:
            raise ValueError('No native text layout for ' + key)
        x,y=point(source.get('position',{}),width,height)
        return 'region',[x,y,min(max(32,width-x-8),190),12]
    if key=='view.header':return 'region',[8,3,width-16,22]
    if key=='view.body':return 'region',[8,28,width-30,max(20,height-120 if 'PLAYER_INVENTORY' in style.get('slots',{}) else height-54)]
    raise ValueError('Unknown GUI target ' + key)
