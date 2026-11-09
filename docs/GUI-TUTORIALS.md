# AE2S GUI 教程

本附属面向 AE2S / Supergiant 1.1.0，使用 Ponder Legacy 1.7.1。只在客户端检测到 Ponder 后注册兼容插件；GUI 适配器只读取状态。

## 一份定义，三种使用方式

资源 `assets/ae2s_ponder/ponder/gui/index.json` 列出 84 个教程，定义位于同目录。`@ae2s_ponder.gui.*` 键随简体中文／英文语言文件切换。

Java 机器动画：

```java
scene.overlay().showGui(400, new ResourceLocation("ae2s_ponder:drive"))
    .onRight().pointAt(new Vec3d(5.5, 1.5, 3.5));
scene.idle(401);
```

Markdown 自动编排动画使用：

```md
<GuiTutorial id="ae2s_ponder:inscriber" duration={400} side="right" />
```

只有 `scene:` 链接既有 Java 动画的页面，卡片用于静态展示，时间轴片段由 Java 中的 `showGui` 安排。`structure:` 自动生成动画的 Markdown 会把带时长的 GUI 卡片编入同一时间轴。

同一 JSON 的 `screen` 与 `adapter: ae2s` 使真实机器页长按 W 可启动实机引导。独立演示读取 `demo` 动作，实机引导读取 `wait` 条件；两者状态独立。

## AE2S 语义目标

- `slot.STORAGE_CELL.0`：实际容器的第一格存储元件槽。
- `slot.CONFIG.0`：实际配置槽；禁用时不伪造可用高亮。
- `slot.INSCRIBER_PLATE_TOP.0`、`slot.MACHINE_INPUT.0`：不依赖可能被升级槽改变的数字序号。
- `widget.search`、`widget.encodePattern`：读取 AE2S WidgetContainer 控件位置及启用状态。
- `repo.0`：终端当前布局的第一格网络库存。
- `inscriber.progress`：AE2S 同步加工进度；`inscriber.work_observed`：加工中或已有产物，避免快速工序错过等待；`pattern.mode`：同步编码模式。

终端在每个实际文本框获得焦点时保留按键输入。实际槽位、窗口位置、按钮可见性来自 AE2S，不使用写死的屏幕坐标；JSON 坐标仅用于演示布局。演示引用 AE2S 已安装的原始界面纹理，没有复制上游纹理到附属包内。

## 修改与验证

`tools/generate-guis.py` 与 `tools/gui_catalog.py` 是 GUI 定义与双语文字的可复现来源；修改后执行：

```bash
python3 tools/generate-guis.py
python3 tools/generate-structures.py
python3 tools/generate-guides.py
python3 tools/verify-assets.py
```

Java 动画中的 `gui(...)` 会被 Markdown 生成器计入快照时间，避免后续静态截图落到错误段。实际容器、双语演示、搜索框焦点、状态隔离及有／无 Ponder 的两端验收由开发 harness 执行，报告见 LEGACY-VERIFICATION.md。

本地可以用 `-PponderSourceDir=/absolute/path/to/ponder` 指定编译 SDK；默认使用兄弟目录，独立 CI 使用 build-dependencies.json 固定的 Ponder 源码版本。Mouse Tweaks 只提供 AE2S 公开类签名引用的编译 API，不是运行依赖。

原生资源解析与完整范围见 [覆盖清单](GUI-COVERAGE.md)。独立 GUI 页面使用各自的上下文结构；物品入口、语言、操作步骤与动画引用由同一目录生成。


## 完整外观与指引框

`appearances.json` 与 `coverage.json`、操作步骤分别维护：前者保存完整界面的槽位、控件、工具栏和可见模式，
后两者定义教程范围与操作。`tools/gui_demo_layouts.py` 读取固定版本 AE2S 原生样式，
`tools/gui_native_widgets.json` 保存核对过的原生控件注册与继承关系，资源检查可重复生成结果。

客户端适配器向 Ponder 1.7.1 提供 `GuiDemoLayout`，使用原生被动按钮、数值输入、文本框和复选框绘制。
Ponder 统一处理分组偏移、弹窗层级、裁切和高亮坐标；适配器通过 API 中的只读 `GuiDemoState` 读取演示状态。
样板访问终端和 CPU 列表把每行注册到受裁切的分组，指引框绑定同一可见区域；元件终端的顶部标签页也计入整体边界。
终端设置按步骤切换搜索／通用／无线页面，并保留内部／外部搜索选项的互斥关系。
空白输入、隐藏弹窗和没有匹配宿主的升级区域不伪造交互。动态列表使用独立示例数据，不能据此读取真实网络库存。

开发验收保存原生控件的实际几何数据，并逐项检查 W 引导框与原生槽位、按钮、文本框、复合控件一致。
演示专项逐步检查高亮边缘、分数缩放、英文／简体中文、窗口缩放和回放状态，逐步骤保存帧缓冲截图。
