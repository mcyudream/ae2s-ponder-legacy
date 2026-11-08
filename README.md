# AE2S Ponder Legacy

[![Build and release](https://github.com/mcyudream/ae2s-ponder-legacy/actions/workflows/ci.yml/badge.svg)](https://github.com/mcyudream/ae2s-ponder-legacy/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/mcyudream/ae2s-ponder-legacy)](https://github.com/mcyudream/ae2s-ponder-legacy/releases)

![AE2S Ponder Legacy 展示插画](branding/cover.png)

为 **Applied Energistics 2 Supergiant（应用能源 2 超巨星，AE2S）** 制作的独立思索附属模组，由 **yudream** 编写。通过 25 篇中英文教程（24 个动画与静态双展示教程、1 篇排障索引），覆盖 ME 网络、存储、自动化、材料制备及进阶网络。

**当前开发版本：0.3.0（main CI）。运行基线：Minecraft 1.12.2 / Cleanroom 0.4.0 正式版（不带 `-alpha`）/ Java 25。**

## 下载与安装

1. 准备 **Minecraft 1.12.2、Cleanroom 0.4.0 正式版、Java 25**。
2. 安装 [AE2S / Supergiant 1.1.0](https://github.com/FormlessDragon/Applied-Energistics-2-Supergiant/releases/tag/v1.1.0)。请下载普通安装 jar。
3. 观看本版教程另需 **Ponder Legacy 1.7.0 或更新版本**，当前从 [Ponder main CI](https://github.com/mcyudream/ponder-legacy/actions/workflows/ci.yml) 下载 `release-assets`。CraftTweaker、GuideME 和 Mouse Tweaks 均无需安装。
4. 从 [本项目 main CI](https://github.com/mcyudream/ae2s-ponder-legacy/actions/workflows/ci.yml) 的 `release-assets` 下载 `ae2s-ponder-legacy-0.3.0.jar`，放入客户端的 `mods/`，替换本项目旧 jar。正式发行仍以 [GitHub Releases](https://github.com/mcyudream/ae2s-ponder-legacy/releases) 为准。

`-sources.jar` 供开发使用；`-mcp.jar` 和验证模组不作为安装文件发布。Ponder 与 AE2S 独立安装，均未打入本附属。

本附属只需装在客户端。**Ponder 为可选依赖**：未安装时正常启动并进入世界，教程入口停用。本版使用独立构建的 **Ponder Legacy 1.7.0** 安装包验收，具体哈希见 [验收记录](LEGACY-VERIFICATION.md)。加载器验收基线为正式 **Cleanroom 0.4.0**，与 `0.4.0-alpha` 分别记录。

## 升级

0.3.0 新增 8 套共享 GUI 教程，使用 Ponder 1.7.0 的时间轴 GUI API；已安装 Ponder 时需同步升级至 1.7.0 或更新版本。未安装 Ponder 仍可正常进入游戏。

历史 0.2.0 同装新版 FTB Quests 时，请使用 **Ponder Legacy 1.5.1 或更新版本**。1.5.0 与声明 `after:ponder-legacy` 的 FTBQ 会形成双向加载顺序循环；该问题由 Ponder 1.5.1 修复，**历史附属 0.2.0 无需更新**。联合安装的正式 Cleanroom 0.4.0 报告见 [Ponder 补丁验收](https://github.com/mcyudream/ponder-legacy/blob/v1.5.1/docs/verification/release-1.5.1-cleanroom-0.4.0/summary.json)。

0.2.0 的双展示和 Markdown 教程需要 Ponder Legacy 1.5.0 或更新版本；Ponder 保持可选。请同时替换旧教程附属与旧 Ponder jar。

### 历史 0.1.0 → 0.1.1 修复

`0.1.0` 的 Ponder 最低版本写成 `1.4.0-cleanroom-alpha.1`，加载器将这个自定义后缀排在正式 `1.4.0` 之后，导致正确安装的 1.4.0 被拒绝。`0.1.1` 改为 `after:ponder-legacy@[1.4.0,)`，保持 Ponder 可选；移除旧附属 jar 并安装 0.1.1，保留 Ponder 1.4.0 即可。

## 如何观看

- 悬停驱动器、样板供应器、ME P2P 隧道等关联物品，按住 **W**。
- `/ponder index` 打开包含四个分类的教程索引。
- `/ponder ae2:drive`、`/ponder ae2:pattern_provider`、`/ponder ae2:me_p2p_tunnel` 可直接进入相应教程。
- W 为唯一入口，界面内切换动画／静态图文，并可保存默认展示。简体中文和英文跟随游戏语言切换。
- 支持关键帧与回放；静态页可搜索、滚动和旋转 3D 场景，F7 编辑 Markdown。
- 教程结构可投影到世界；材料按钮检查背包，清单可钉在 HUD／背包并拖拽保存位置。

## 0.3.0：机器动画中的 GUI 讲解

- 播放机器教程时，在同一个思索页面的侧边留白弹出 GUI 片段，介绍控件、物品流转与操作顺序；片段结束后继续 3D 演示。
- GUI 与机器动画共用时间轴、暂停、跳转和重播。第一网络、元件分区、自动合成、处理样板、处理器生产与接口备货已接入。
- 打开真实机器页后，点击输入框外并长按 **W** 进入实机引导。槽位高亮读取 AE2S 实际位置，支持窗口调整和动态终端布局；搜索框输入时不会抢占 W。
- 静态页的 GUI 卡片可打开独立演示。动画、独立演示、实机引导共用 `ponder/gui/*.json`，F7 Markdown 编辑器可插入同一教程引用。
- 演示不操作真实机器，不改变背包，不发送代操作数据包。实机引导观察真实槽位、按钮与同步值，操作仍由玩家完成。

| GUI 教程 | 内容 |
| --- | --- |
| ME 驱动器 | 安装元件、扩容和保管数据 |
| ME 终端／合成终端 | 搜索、库存与背包存取 |
| 存储元件工作台 | 元件插入、分区标记与取回 |
| 压印器 | 硅模板、输入、加工与硅板输出 |
| 合成样板编码 | 选择模式、空白样板、9 铁锭到铁块 |
| 处理样板编码 | 选择模式、铁矿石到铁锭、准确回网 |
| 样板供应器 | 安装样板、回网缓冲和优先级 |
| ME 接口 | 配置槽、实物备货、消耗与补货 |

配置槽使用幽灵标记的教程明确区分标记与实物。样板终端会按当前合成／处理模式匹配 W 引导；未插元件的工作台配置槽暂不可高亮，插入后按实际可用状态显示。

编写与扩展示例见 [GUI 教程接入说明](docs/GUI-TUTORIALS.md)。外置视频／任务等功能继续按 Ponder 的可选依赖启用。

## 原有八个教程（均补充静态展示）

| 场景 | 演示内容 | 部分入口物品 |
| --- | --- | --- |
| 第一个 ME 网络 | 振动仓供电、能量接收器、储能、驱动器与终端 | 振动仓、驱动器、终端 |
| 存储元件与分区 | 元件装入、容量限制、工作台分区、取出保管 | 存储元件、元件工作台 |
| 频道与线缆容量 | 无控制器网络、8/32 频道、线缆颜色、石英纤维 | 控制器、各色线缆、石英纤维 |
| 接入外部容器 | 存储总线方向、箱子访问、优先级与过滤 | 存储总线、ME 接口 |
| 物品输入与输出 | 输入总线、输出过滤、目标空间和传输控制 | 输入/输出总线、存储水平发信器 |
| 自动合成 | 编码 9 铁锭 → 1 铁块、样板供应器、装配室与 CPU | 样板供应器、装配室、合成存储器 |
| 处理样板 | 编码铁矿石 → 铁锭、熔炉各面、燃料和成品回收 | 处理样板、样板供应器、输入总线 |
| ME P2P 隧道 | 独立承载网、石英纤维供电、内存卡保存与绑定 | ME P2P 隧道、内存卡 |

结构使用 AE2S 1.1.0 的真实方块与 multipart 部件，在 Ponder 虚拟世界中编排流程和动画。讲解包含供电、存储、频道及操作顺序；虚拟世界中的动画不代表执行了完整的 ME 自动合成任务。

## 新增 17 篇 Markdown 教程

| 分类 | 内容 |
| --- | --- |
| 基础材料 | 充能器、石英生长与福鲁伊克斯材料 |
| 存储 | 流体存储、物质聚合器 |
| 自动化 | 接口备货、存储水平控制、IO 端口、成型与湮灭面板、升级卡 |
| 合成 | 压印器与处理器、合成 CPU |
| 网络 | 子网络、无线终端、量子桥、空间 IO、监视器与网络工具 |
| 排障 | 供电、频道、过滤、容量、处理样板与回收检查索引（静态页） |

按官方 AE2 GuideME 的主题补全，使用原创中英文讲解，并按 **AE2S 1.1.0** 的真实注册、配方与操作重写。例如无线终端在访问点界面配对，量子桥两端没有直连线缆绕过桥。现代版的配方和专有 API 不直接照搬。

源码位于 `assets/ae2s_ponder/ponder/guides/`；一份 Markdown 编排讲解、步骤动作和静态快照。`<GuideOnly>` 支持参数与排障补充，`<AnimationOnly>` 支持动画特化。生成工具 `tools/generate-guides.py`、`tools/generate-structures.py` 可重复检查资源。

## 验收与兼容范围

实际生产安装包在**正式 Cleanroom 0.4.0**上完成以下验收，文件 SHA-256 和原始报告见 [正式基线验收](LEGACY-VERIFICATION.md)：

| 运行组合 | 结果 |
| --- | --- |
| 客户端，安装 Ponder 1.7.0 | 24 个动画、25 篇图文与 8 套 GUI，中英文播放、回退、静态演示和真实容器 W 引导 |
| 客户端，未安装 Ponder | 正常进入世界，教程入口停用 |
| 专用服务器，安装／未安装 Ponder | 到达服务器启动完成事件，客户端代码隔离 |

教程入口和渲染保持客户端隔离。包内包含仅用于正式 0.4.0 物理专服的 Kirino 模组发现兼容修复；服务端仍无需安装本附属。

- 支持目标为 **AE2S / Supergiant 1.1.0**，实际 loader ID 为 `ae2`；不声明原版 AE2 1.12.2、AE2UEL 或现代官方 Ponder 的二进制兼容。
- 频道数值按默认配置讲解；整合包更改配置后可能不同。
- 高级内存卡专属界面、多输入 P2P、请求器等尚无专门教程。
- 验收范围及图形环境见记录；没有覆盖任意整合包、硬件或音频输出。
- [早期 0.4.0-alpha 验证档案](docs/VERIFICATION.md) 保留当时的安装包与失败记录，不能替代正式版验收。

本次对其他已发布 1.12.2 模组的依赖范围检查见 [巡检记录](docs/DEPENDENCY-AUDIT-2026-11-05.md)。

## 构建与 CI 发布

使用 Java 25，在克隆的独立仓库中执行：

```bash
python3 tools/bootstrap_legacy.py
bash gradlew --no-daemon :build :reobfJar --console=plain
python3 tools/verify_legacy_package.py --require-verified-hash
python3 tools/prepare_release.py
```

`build-dependencies.json` 固定 Ponder 编译源码提交，`dependency-lock.json` 固定 AE2S 官方 dev/runtime 文件摘要。也可使用同级 `../ponder` 开发工程，或用 `-PponderSourceDir=/absolute/path/to/ponder` 显式选择 1.7.0 SDK；源码依赖仅用于编译，Ponder 保持可选。

编译 SDK 使用 Cleanroom `0.7.14-alpha` userdev；实际最低加载器声明与生产验收基线为 **0.4.0 正式版**。SDK 上的运行结果不替代基线验收。

GitHub Actions 在 push / PR 时构建、检查 24 个结构、25 篇双语教程、8 套 GUI 及语言资源，核对安装包 SHA-256 与四种正式基线报告，再生成归档。后续明确发布与包内版本一致的标签时，CI 才创建 GitHub Release，上传安装 jar、源码 jar 和 `SHA256SUMS`。本次仅提交 main；[0.3.0 更新说明](docs/releases/0.3.0.md)。

### 开发验证

```bash
bash gradlew :runClient -PwithPonder
bash gradlew :runClient
python3 tools/generate-structures.py --check

# 官方正式 0.4.0 环境，使用实际安装 jar 与独立 SRG 验证模组
bash gradlew :build :reobfDevHarnessJar :ponder:reobfJar
python3 tools/verify-cleanroom.py client --with-ponder
python3 tools/verify-cleanroom.py client
python3 tools/verify-cleanroom.py server --with-ponder
python3 tools/verify-cleanroom.py server
```

生产验证启动器目前面向 Linux x64；本地测试服需所有者接受 Minecraft EULA。`LEGACY_PONDER_JAR` 可指定待验收的 Ponder 安装包。运行验证模组位于 `src/dev/`，不进入发布包。

## 身份、作者与授权

| 项目 | 内容 |
| --- | --- |
| 名称 / 作者 | AE2S Ponder Legacy / **yudream** |
| 加载器 Mod ID | `ae2s-ponder-legacy` |
| 资源与场景命名空间 | `ae2s_ponder` |
| 原创项目仓库 | [mcyudream/ae2s-ponder-legacy](https://github.com/mcyudream/ae2s-ponder-legacy) |
| AE2S 身份与来源 | [MC 百科](https://www.mcmod.cn/class/28382.html) · [AE2S 上游](https://github.com/FormlessDragon/Applied-Energistics-2-Supergiant) |
| Ponder 来源 | [Ponder Legacy](https://github.com/mcyudream/ponder-legacy)，原框架作者及授权由该项目保留 |

本附属的 Java 场景、原创结构和中英文讲解由 yudream 编写，按 [MIT](LICENSE) 发布。依赖的原作者、版权和许可分别保留，见 [NOTICE](NOTICE.md) 与 [功能及上游差异](docs/UPSTREAM-DIFFERENCES.md)。本附属不修改 AE2S 配方、容量、频道或核心实现。

`branding/icon.png` 和 `branding/cover.png` 为项目展示插画，生成记录见 [provenance.json](branding/provenance.json)，不作为游戏截图。CurseForge / Modrinth 的状态见 [PUBLICATION.md](PUBLICATION.md)，平台发布配置见 [发布说明](docs/PUBLISHING.md)。
