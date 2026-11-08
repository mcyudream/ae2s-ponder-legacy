# AE2S GUI 教程

本附属面向 AE2S / Supergiant 1.1.0，使用 Ponder Legacy 1.7.0。只在客户端检测到 Ponder 后注册兼容插件；GUI 适配器只读取状态。

## 一份定义，三种使用方式

资源 `assets/ae2s_ponder/ponder/gui/index.json` 列出 8 个教程，定义位于同目录。`@ae2s_ponder.gui.*` 键随简体中文／英文语言文件切换。

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

`tools/generate-guis.py` 是 GUI 定义与双语文字的可复现来源；修改后执行：

```bash
python3 tools/generate-guis.py
python3 tools/generate-guides.py
python3 tools/verify-assets.py
```

Java 动画中的 `gui(...)` 会被 Markdown 生成器计入快照时间，避免后续静态截图落到错误段。实际容器、双语演示、搜索框焦点、状态隔离及有／无 Ponder 的两端验收由开发 harness 执行，报告见 LEGACY-VERIFICATION.md。

本地可以用 `-PponderSourceDir=/absolute/path/to/ponder` 指定编译 SDK；默认使用兄弟目录，独立 CI 使用 build-dependencies.json 固定的 Ponder 源码版本。Mouse Tweaks 只提供 AE2S 公开类签名引用的编译 API，不是运行依赖。
