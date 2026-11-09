# AE2S Ponder Legacy 安装包验收

## 当前开发构建：0.4.0（完整 GUI 覆盖与布局适配）

- 日期：2026-11-08。Minecraft 1.12.2 / **Cleanroom 0.4.0 正式版（无 -alpha）** / Java 25.0.5。
- 生产包：`ae2s-ponder-legacy-0.4.0.jar`；SHA-256：`640e02545d29747567cc92db697bebc91f432260a9a385f9b115f45f268b8b81`。
- AE2S / Supergiant **1.1.0**；Ponder Legacy **1.7.1** 独立安装，SHA-256：`0b4039c5e8cf01e740612136ac188cc41406431d0553f462109bebaf3b2f0f3e`。
- 4 项单元测试通过；开发目录与独立发布目录的生产包逐字节一致。Ponder 的 CI 安装包与实测包也逐字节一致。

| 组合 | 结果 | 检查项 |
| --- | --- | --- |
| client-with-ponder | PASS | 11004 |
| client-without-ponder | PASS | 5 |
| server-with-ponder | PASS | 3 |
| server-without-ponder | PASS | 3 |


84 套教程覆盖 78 种 AE2S 原生界面类型，共 108 个动画与 109 篇双语页面。全量演示检查每个步骤的中英文帧缓冲、分数缩放、高亮边缘、回放与小窗口；本地保存 1122 张截图，提交代表图。原生运行保存 61 份实际控件几何，核对 W 引导、文本输入焦点、容器及背包隔离。

Ponder 的 `GuiDemoLayout` 统一负责分组偏移、祖先裁切、绘制层级和目标可见性。网络状态修正本地化参数；样板访问终端补齐标题、供应器分组和样板行；导入优先级显示真实注册项及编号；样板修改器按模式切换背景、控件和槽位。终端设置的互斥选项、发信器复合输入、颜色弹窗、元件终端标签页，以及 CPU／请求器列表也按各自原生布局处理。

真实客户端退出世界后，GUI 清理与附属场景重载在主线程执行，108 个 AE2S 动画继续可用。未安装 Ponder 的客户端进入世界和两种专服启动均通过。使用生产 SRG 包，没有 userdev 运行时重映射。

验收使用 Linux x64 / llvmpipe，禁用音频输出，未安装 CraftTweaker、HEI、GuideME、Mouse Tweaks、FTB Quests、Media API 或 Revo UI。静态演示的列表是独立示例数据，未据此声明所有生产任务均已逐项完成。原生 tick 分析仪 fixture 仍会记录 AE2S 的尾随 payload 警告；主动断开 fixture 可记录卸载世界后的原版过期实体／声音包。上述日志和检查范围保留于报告，没有将这些上游问题声明为已修复。

[报告与范围](docs/verification/development-0.4.0/summary.json) · [构建一致性](docs/verification/development-0.4.0/reproducibility.json)。本次为 main CI 开发构建，未创建发行标签。

---

## 历史开发构建：0.3.0（共享 GUI 教程）

- 日期：2026-11-08。Minecraft 1.12.2 / **Cleanroom 0.4.0 正式版（无 -alpha）** / Java 25.0.5。
- 安装包：`ae2s-ponder-legacy-0.3.0.jar`；SHA-256：`c134dd24dff406d417e9d631f17c9a03bf68e6e5a902d6ca379608949c7080a3`。
- AE2S / Supergiant **1.1.0**；独立安装 Ponder Legacy **1.7.0**，SHA-256：`86e072acb375b28dd68051c87ae2c752a6e9df81794e8da701fb641943f35041`。
- 4 项版本／可选依赖单元测试通过；开发目录与独立发布目录构建产物逐字节一致。Ponder 的 main CI 产物也与验收包一致。

| 组合 | 结果 | 检查项 |
| --- | --- | --- |
| client-with-ponder | PASS | 1872 |
| client-without-ponder | PASS | 5 |
| server-with-ponder | PASS | 3 |
| server-without-ponder | PASS | 3 |

8 套 GUI 均在 AE2S 原生界面上核对中英文、W 长按、语义槽位／动态控件、文本框焦点和演示状态隔离；样板终端按当前模式匹配引导。真实驱动器与元件工作台通过原生容器点击放入元件，验证同步后的步骤推进和配置槽启用。引导面板避让 AE2S 工具栏与扩展控件，缩放后高亮保持对齐。压印器同时用同步状态 fixture 核对加工进度与已完成产物条件，未声称完整运行自动生产线。

24 个机器动画与 25 篇双语图文回归通过；Java／Markdown 的 GUI 片段与实机引导解析同一数据，场景跳转和重播重建相同 GUI 帧。真实 P2P、内存卡、机器供电及投影材料继续通过。四种组合使用实际生产 SRG jar，未装 CraftTweaker、GuideME、Mouse Tweaks、FTB Quests、Media API 或 Revo UI。

[报告、运行指纹、截图与范围](docs/verification/development-0.3.0/summary.json) · [构建一致性](docs/verification/development-0.3.0/reproducibility.json)。Linux x64 / llvmpipe；不背书其他 AE2 实现或任意整合包。本次为 main CI 构建，正式发行状态见 PUBLICATION.md。

---

## 历史：0.2.0 正式基线验收

- 日期：2026-11-06。Minecraft 1.12.2 / **Cleanroom 0.4.0 正式版（不带 -alpha）** / Java 25.0.5。
- 安装包：`ae2s-ponder-legacy-0.2.0.jar`，SHA-256：`1f6c095c8859cf0053a431b5c0535a0a45a33d25ac10f3d96eef3c67997e0614`。
- AE2S / Supergiant 1.1.0；Ponder Legacy **1.5.0**，SHA-256：`bf668461d714313326ecf095614b58eee5b6fa5e5317c7ee5cb5de3bd92176d6`。Ponder 独立安装，不打入附属。

| 组合 | 结果 | 检查项 |
| --- | --- | --- |
| client-with-ponder | PASS | 1382 |
| client-without-ponder | PASS | 5 |
| server-with-ponder | PASS | 3 |
| server-without-ponder | PASS | 3 |

原八个 Java 动画保留，16 个 Markdown 生成动画和 1 篇静态排障页新增；共 24 个动画、25 篇双语页面。实际安装包播放与回退、原生结构和 multipart 重建、简体中文／英文、静态页与共享编排通过。额外核对首个网络及 P2P 的投影材料能解析 AE2S 终端、线缆和隧道物品。真实内置服务器中的 P2P 承载网、内存卡及基础机器供电测试继续通过。

[本版全部报告、环境与截图](docs/verification/release-0.2.0/summary.json)。四种组合均使用实际生产 SRG jar，**没有 CraftTweaker**；无 Ponder 时正常进入世界。专服到达启动完成事件且不加载客户端教程入口；编译 SDK 0.7.14-alpha 不作为基线证据。

Linux x64 / llvmpipe；未覆盖所有硬件、整合包或音频。虚拟世界展示操作顺序，不声称执行完整 ME 自动合成任务。现代官方 GuideME 只作为主题参考，行为按 AE2S 1.1.0 核对；不背书原版 AE2、AE2UEL。

---

## 历史：0.1.1 正式基线验收

- 日期：2026-11-05。
- Minecraft 1.12.2 / **Cleanroom 0.4.0 正式版（不带 -alpha）** / Java 25.0.5。
- 生产安装包：`ae2s-ponder-legacy-0.1.1.jar`。
- SHA-256：`26d132043b33f9c29e4c4af24db5f5e39cbea42a9453fe3339383a30694ef11f`。
- 实际安装的 Ponder：正式 **1.4.0**，官方 GitHub Release 下载包。
- Ponder SHA-256：`4c02d70c6f38ddf5305fa4be47a5e410e693c57f2cd8576ed5f78f8b7f32f14b`。

| 组合 | 结果 | 证据 |
| --- | --- | --- |
| 客户端，Ponder 1.4.0 | PASS，551 项 | [报告](docs/verification/release-0.1.1/client-with-ponder/report.json) · [环境](docs/verification/release-0.1.1/client-with-ponder/runtime.json) · [日志](docs/verification/release-0.1.1/client-with-ponder/startup.txt) |
| 客户端，无 Ponder | PASS，5 项 | [报告](docs/verification/release-0.1.1/client-without-ponder/report.json) · [环境](docs/verification/release-0.1.1/client-without-ponder/runtime.json) · [日志](docs/verification/release-0.1.1/client-without-ponder/startup.txt) |
| 专用服务器，Ponder 1.4.0 | PASS，3 项 | [报告](docs/verification/release-0.1.1/server-with-ponder/report.json) · [环境](docs/verification/release-0.1.1/server-with-ponder/runtime.json) · [日志](docs/verification/release-0.1.1/server-with-ponder/startup.txt) |
| 专用服务器，无 Ponder | PASS，3 项 | [报告](docs/verification/release-0.1.1/server-without-ponder/report.json) · [环境](docs/verification/release-0.1.1/server-without-ponder/runtime.json) · [日志](docs/verification/release-0.1.1/server-without-ponder/startup.txt) |

## 修复与回归

旧声明 `after:ponder-legacy@[1.4.0-cleanroom-alpha.1,)` 使用了自定义 `cleanroom` 版本限定符。FML 的版本排序将其排在正式 `1.4.0` 之后，因此 0.1.0 拒绝新 Ponder。使用加载器原有版本解析器的回归测试在修复前复现稳定版被拒绝，改为 `after:ponder-legacy@[1.4.0,)` 后四项通过：正式 1.4.0 可用、旧 cleanroom 预发行版仍在范围内、1.3.9 被排除、Ponder 保持可选。[JUnit 报告](docs/verification/release-0.1.1/dependency-regression.xml)。

实际客户端报告确认附属 **0.1.1** 与 Ponder **1.4.0**，完整执行八个场景的中英文时间线、回退重放、结构及 multipart 重建和 UI / OpenGL 检查，保留 16 张截图。真实内置服务器世界检查 P2P 内存卡绑定、承载网隔离及远端网络接入，以及合成、处理、频道三个结构的驱动器供电与频道。

两种专服组合均到达 `FMLServerStarted`。教程入口是 clientSideOnly，FML 在专服正确停用它；jar 内限定正式 0.4.0 的 Kirino 发现兼容修复仍在引导期执行。专服包的身份由 runtime.json 中实际安装包哈希确认，不将客户端入口已停用误判为模组缺失。

本次使用官方正式 0.4.0 安装器与生产 SRG 安装 jar，没有 userdev 运行时重映射。编译 SDK 仍为 0.7.14-alpha；它不替代正式 0.4.0 的验收。AE2S 1.1.0、CraftTweaker 4.1.20.698 和 Ponder 1.4.0 均校验发布文件摘要。CI 发布再次核对本附属哈希、实际报告版本和四组报告。

## 范围与历史

Linux x64、llvmpipe 图形后端，音频后端设为 null；不验收声音和任意整合包组合。自动合成与机器流程主要为 Ponder 脚本讲解，真实网络检查范围如上，不声称执行了完整 ME 自动合成任务。仅声明 AE2S / Supergiant 兼容。

[0.1.0 正式基线历史记录](docs/verification/release-0.1.0/ACCEPTANCE.md)和[更早的 0.4.0-alpha 档案](docs/VERIFICATION.md)保留原始版本及摘要。
