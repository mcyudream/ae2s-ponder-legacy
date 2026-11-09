#!/usr/bin/env python3
"""Generate reproducible bilingual shared Markdown resources from original lesson content."""
from pathlib import Path
import argparse, json, re
from guide_content import NEW, LEGACY, CATEGORIES
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'src/main/resources/assets/ae2s_ponder'
GUI_SEGMENTS={
    ('processors',0):'inscriber',('processors',2):'output_sides',('processors',3):'pattern_processing',
    ('interfaces',1):'interface',('interfaces',2):'stock_amount',
    ('level_stocking',0):'level_emitter',('level_stocking',1):'export_bus',
    ('subnetworks',3):'storage_bus',('cell_io',1):'io_port',
    ('wireless',1):'wireless_access_point',('wireless',2):'wireless_terminal',
    ('quantum_bridge',2):'quantum_bridge',('spatial_io',2):'spatial_io',
    ('planes',2):'formation_plane',('planes',3):'annihilation_plane',
    ('upgrades',1):'export_bus',('crafting_cpu',3):'crafting_status',
    ('monitors_tools',2):'network_status',('fluid_storage',1):'storage_bus',('condenser',1):'condenser'
}

def lang(code):
    return dict(line.split('=',1) for line in (ASSETS/f'lang/{code}.lang').read_text().splitlines() if line and not line.startswith('#') and '=' in line)
def metadata(id,title,components,category,language,linked=False):
    return '\n'.join(['---',f'id: ae2s_ponder:{id}','title: '+json.dumps(title,ensure_ascii=False),
        'item_ids: ['+', '.join('ae2:'+c for c in components)+']',('scene' if linked else 'structure')+f': ae2s_ponder:{id}',
        'tags: [ae2s_ponder:'+category+']','categories: ['+CATEGORIES[category][language]+']','presentation: both','step_ticks: 180','---',f'# {title}',''])
def actions(pos,item=None,index=0):
    ops=[{'op':'overlay.show_outline','color':'green','slot':'focus','selection':{'type':'position','pos':pos},'duration':175}]
    if item:
        x,y,z=pos
        ops += [{'op':'world.create_item','handle':f'item{index}','x':x-1,'y':y+1.4,'z':z+.5,'mx':0,'my':0,'mz':0,'item':'ae2:'+item,'count':1,'meta':0},
                {'op':'world.move_item','handle':f'item{index}','x':x+.5,'y':y+1.4,'z':z+.5,'duration':25},
                {'op':'scene.idle','ticks':30},{'op':'world.remove_item','handle':f'item{index}'}]
    return '\n```ponder\n'+json.dumps(ops,ensure_ascii=False,indent=2)+'\n```\n'
def files():
    result={};source=(ROOT/'src/main/java/dev/yudream/ae2sponder/compat/AE2SScenes.java').read_text()
    gui_rows=json.loads((ASSETS/'ponder/gui/coverage.json').read_text())['lessons']
    for code,l in [('en_us',0),('zh_cn',1)]:
        text=lang(code)
        for id,(category,components,prefix) in LEGACY.items():
            title=text[f'ae2s_ponder.ponder.{id}.header'];page=metadata(id,title,components,category,l,True)
            # Derive exact annotation cursor times, including reversible item-flow delays.
            method=re.search(r'public static void \w+\(SceneBuilder scene, SceneBuildingUtil util\) \{\s*begin\(scene, "'+id+r'".*?(?=\n    public static void|\n\})',source,re.S).group()
            cursor=15;step=0
            for call in re.finditer(r'flow\(scene,.*?;|explain\(scene, util, "([^"]+)"[^;]*;|gui\(scene, "([^"]+)"[^;]*;',method):
                if call.group(2):
                    page+=f'\n<GuiTutorial id="ae2s_ponder:{call.group(2)}" />\n'
                    cursor+=401;continue
                if call.group(1) is None:cursor+=32;continue
                step+=1;key=call.group(1);narration=text[f'ae2s_ponder.ponder.shared.{key}'];tick=cursor+30;cursor+=170
                page+=f'\n## {step}\n\n{narration}\n\n<GameScene scene="ae2s_ponder:{id}" tick={{{tick}}} />\n'
            page+='\n<GuideOnly>\n\n'+('[排查与索引](troubleshooting.md)' if l else '[Troubleshooting and topic index](troubleshooting.md)')+'\n\n</GuideOnly>\n'
            result[f'ponder/guides/{code}/{id}.md']=page
        for row in gui_rows:
            gui=json.loads((ASSETS/f'ponder/gui/{row["id"]}.json').read_text())
            title=text[gui['title'][1:]];id='gui/'+row['id']
            page=metadata(id,title,row['components'],row['category'],l)
            if l==0:
                page+='\n## Find the device\n\nOpen the named AE2S device or the related subdialog. The structure shows the surrounding network context; use the GUI demonstration to inspect its controls.\n'
                page+='\n## GUI operation\n\nFollow the cursor, highlighted controls and resource entries in the demonstration. Playback uses separate data.\n'
            else:
                page+='\n## 找到设备\n\n打开对应 AE2S 设备或相关子页面。结构展示其网络上下文，使用 GUI 演示查看控件与操作。\n'
                page+='\n## 界面操作\n\n跟随演示中的光标、高亮控件与资源条目。回放使用独立数据。\n'
            duration=max(320,len(gui['steps'])*76+20)
            page+=f'\n<GuiTutorial id="ae2s_ponder:{row["id"]}" duration={{{duration}}} side="right" />\n'
            if l==0:
                page+='\n## Follow along in game\n\nOn the actual device, leave the text field and hold W to start guidance. Perform native operations yourself; the guide observes controls and does not send machine actions.\n'
                page+='\n## Verify the result\n\nCheck the real inventory, selected settings and destination. Start with one transfer or one batch before scaling up.\n'
            else:
                page+='\n## 实机跟随\n\n在真实设备中，离开输入框后长按 W 进入引导。原生操作仍由你执行，引导观察控件，不会代发机器操作。\n'
                page+='\n## 核对结果\n\n检查真实库存、所选设置与目标去向。扩大规模前，先测试一次传输或一批加工。\n'
            page+='\n<GuideOnly>\n'
            for step in gui['steps']:
                heading=text.get(step['title'][1:],step['title']) if step['title'].startswith('@') else step['title']
                body=text.get(step['text'][1:],step['text']) if step['text'].startswith('@') else step['text']
                page+=f'\n### {heading}\n\n{body}\n'
            page+='\n</GuideOnly>\n'
            result[f'ponder/guides/{code}/{id}.md']=page
        for id,category,components,titles,reference,steps in NEW:
            page=metadata(id,titles[l],components,category,l)
            for i,(en_h,zh_h,en,zh,pos) in enumerate(steps):
                page+=f'\n## {en_h if l==0 else zh_h}\n\n{en if l==0 else zh}\n'+actions(pos,
                    'certus_quartz_crystal' if id=='charger' and i==1 else 'logic_processor' if id=='processors' and i==4 else None,i)
                gui = GUI_SEGMENTS.get((id,i))
                if gui:page+=f'\n<GuiTutorial id="ae2s_ponder:{gui}" duration={{400}} side="right" />\n'
            page+='\n<GuideOnly>\n\n'+('[排查与索引](troubleshooting.md)' if l else '[Troubleshooting and topic index](troubleshooting.md)')+'\n\n</GuideOnly>\n'
            result[f'ponder/guides/{code}/{id}.md']=page
        title='Tutorial Index and Troubleshooting' if l==0 else '教程索引与故障排查'
        page=f'---\nid: ae2s_ponder:troubleshooting\ntitle: {title}\nitem_ids: [ae2:network_tool]\npresentation: guide\n---\n# {title}\n\n'
        page+=('These tutorials target AE2S / Supergiant 1.1.0 on Minecraft 1.12.2 / Cleanroom. Resource recipes and channel settings may be changed by the modpack.\n' if l==0 else '本教程面向 Minecraft 1.12.2 / Cleanroom 的 AE2S / Supergiant 1.1.0，资源配方与频道设置可被整合包改动。\n')
        for category,names in CATEGORIES.items():
            page+='\n## '+names[l]+'\n\n'
            for id,(cat,components,prefix) in LEGACY.items():
                if cat==category:page+='- ['+text[f'ae2s_ponder.ponder.{id}.header']+f']({id}.md)\n'
            for id,cat,components,titles,reference,steps in NEW:
                if cat==category:page+=f'- [{titles[l]}]({id}.md)\n'
        if l==0:page+='\n## Check in order\n\n| Symptom | Check |\n| - | - |\n| Terminal offline | Power, connections, channels, loaded chunks |\n| Import stops | Source side, filter, free bytes and types, storage access |\n| Crafting waits | Exact pending product, machine power, output side, same-network return |\n| Wireless fails | Pairing slot, battery, bound access point, range and dimension |\n| IO port stalls | Transfer direction, partitions, full destination, completion mode |\n'
        else:page+='\n## 按顺序排查\n\n| 症状 | 检查项目 |\n| - | - |\n| 终端离线 | 电力、连接、频道、区块加载 |\n| 输入停止 | 源容器侧面、过滤、字节与类型空间、访问权限 |\n| 合成等待 | 准确的待回网产物、机器供电、输出面、是否回到同一网络 |\n| 无线失效 | 配对槽、电量、绑定访问点、距离与维度 |\n| IO 端口停滞 | 转移方向、分区、目标已满、完成模式 |\n'
        result[f'ponder/guides/{code}/troubleshooting.md']=page
    result['ponder/guides/index.json']=json.dumps({'pages':list(LEGACY)+[r[0] for r in NEW]+['troubleshooting']+['gui/'+r['id'] for r in gui_rows]},indent=2)+'\n'
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    for name,text in files().items():
        path=ASSETS/name
        if args.check:
            if not path.exists() or path.read_text()!=text:raise SystemExit('Guide differs: '+str(path))
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
    count=len(json.loads((ASSETS/'ponder/guides/index.json').read_text())['pages'])
    print(f'{count} bilingual tutorials verified' if args.check else 'Generated bilingual tutorials')
if __name__=='__main__':main()
