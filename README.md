# AE2S Ponder Legacy

[![Build and release](https://github.com/mcyudream/ae2s-ponder-legacy/actions/workflows/ci.yml/badge.svg)](https://github.com/mcyudream/ae2s-ponder-legacy/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/mcyudream/ae2s-ponder-legacy)](https://github.com/mcyudream/ae2s-ponder-legacy/releases)

![AE2S Ponder Legacy 展示插画](branding/cover.png)

为 **Applied Energistics 2 Supergiant（应用能源 2 超巨星，AE2S）** 制作的独立思索附属模组，由 **yudream** 编写。通过八个可回放的中英文教程，演示 ME 网络、存储、频道、总线、自动合成、处理样板和 P2P 的搭建与操作。

**当前版本：0.1.1。运行基线：Minecraft 1.12.2 / Cleanroom 0.4.0 正式版（不带 `-alpha`）/ Java 25。**

## 下载与安装

1. 准备 **Minecraft 1.12.2、Cleanroom 0.4.0 正式版、Java 25**。
2. 安装 [AE2S / Supergiant 1.1.0](https://github.com/FormlessDragon/Applied-Energistics-2-Supergiant/releases/tag/v1.1.0)。请下载普通安装 jar。
3. 观看教程另需 [Ponder Legacy 1.4.0](https://github.com/mcyudream/ponder-legacy/releases/tag/v1.4.0) 和 **CraftTweaker 4.1.20.698**。
4. 从 [GitHub Releases](https://github.com/mcyudream/ae2s-ponder-legacy/releases) 下载 `ae2s-ponder-legacy-0.1.1.jar`，放入客户端的 `mods/`，替换本项目旧 jar。

`-sources.jar` 供开发使用；`-mcp.jar` 和验证模组不作为安装文件发布。Ponder 与 AE2S 独立安装，均未打入本附属。

本附属只需装在客户端。**Ponder 为可选依赖**：未安装时正常启动并进入世界，教程入口停用。本版已实测 **Ponder Legacy 1.4.0 正式版**。加载器验收基线为正式 **Cleanroom 0.4.0**，与 `0.4.0-alpha` 分别记录。

## 从 0.1.0 升级

`0.1.0` 的 Ponder 最低版本写成 `1.4.0-cleanroom-alpha.1`，加载器将这个自定义后缀排在正式 `1.4.0` 之后，导致正确安装的 1.4.0 被拒绝。`0.1.1` 改为 `after:ponder-legacy@[1.4.0,)`，保持 Ponder 可选；移除旧附属 jar 并安装 0.1.1，保留 Ponder 1.4.0 即可。

## 如何观看

- 悬停驱动器、样板供应器、ME P2P 隧道等关联物品，按住 **W**。
- `/ponder index` 打开包含四个分类的教程索引。
- `/ponder ae2:drive`、`/ponder ae2:pattern_provider`、`/ponder ae2:me_p2p_tunnel` 可直接进入相应教程。
- 支持关键帧、框选、物品移动和时间轴回放；简体中文和英文跟随游戏语言切换。

## 八个教程

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

## 验收与兼容范围

实际生产安装包在**正式 Cleanroom 0.4.0**上完成以下验收，文件 SHA-256 和原始报告见 [正式基线验收](LEGACY-VERIFICATION.md)：

| 运行组合 | 结果 |
| --- | --- |
| 客户端，安装 Ponder | 551 项检查通过，八个教程中英文播放与回退重放 |
| 客户端，未安装 Ponder | 5 项检查通过，正常进入世界 |
| 专用服务器，安装 Ponder | 3 项检查通过，到达服务器启动完成事件 |
| 专用服务器，未安装 Ponder | 3 项检查通过，到达服务器启动完成事件 |

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

`build-dependencies.json` 固定 Ponder 编译源码提交，`dependency-lock.json` 固定 AE2S 官方 dev/runtime 文件摘要。也可使用同级 `../ponder` 开发工程；源码依赖仅用于编译，Ponder 保持可选。

编译 SDK 使用 Cleanroom `0.7.14-alpha` userdev；实际最低加载器声明与生产验收基线为 **0.4.0 正式版**。SDK 上的运行结果不替代基线验收。

GitHub Actions 在 push / PR 时构建、检查八个结构及语言资源、验证发布包身份并生成归档。推送与包内版本一致的 `v0.1.1` 标签后，CI 还会核对正式基线报告及安装包 SHA-256，再创建 GitHub Release，上传安装 jar、源码 jar 和 `SHA256SUMS`。发布页使用 [0.1.1 更新说明](docs/releases/0.1.1.md)。

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
