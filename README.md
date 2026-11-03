# AE2S Ponder Legacy

![AE2S Ponder Legacy](branding/cover.png)

<!-- legacy-overview:start -->
由 yudream 编写的 AE2S 基础教程附属。通过八个可回放场景讲清 ME 网络、存储、频道、总线、自动合成、处理样板和 P2P 的搭建顺序。

## 当前状态

本版本已完成当前声明范围的正式 Cleanroom 0.4.0 安装包验收。实际运行包的 SHA-256、检查项和限制见 [验收记录](LEGACY-VERIFICATION.md)。这不表示上游所有扩展或任意整合包组合均已验证。

<!-- legacy-authorship:start -->
## 作者与来源 / Authors and upstream

- 此 Legacy 版本作者与维护者 / Legacy author and maintainer：**yudream**。
- 原作者 / Original author(s)：**yudream (original addon)**。
- 原仓库 / Original repository：[mcyudream/ae2s-ponder-legacy](https://github.com/mcyudream/ae2s-ponder-legacy)。
- 本附属由 yudream 原创；AE2S、Ponder 等依赖的原作者与授权分别保留。
<!-- legacy-authorship:end -->

## 运行环境与身份

| 项目 | 要求 / 标识 |
| --- | --- |
| Minecraft | 1.12.2 |
| 运行基线 | Cleanroom **0.4.0 正式版（不带 `-alpha`）** |
| Java | 25 |
| 加载器 Mod ID | `ae2s-ponder-legacy` |
| 资源与原注册命名空间 | `ae2s_ponder`（保留） |
| AE2 实现 | Applied Energistics 2 Supergiant（AE2S），实际 Mod ID `ae2` |

Mod 的 alpha 版本号与加载器版本无关。开发 SDK 可以较新，兼容结论必须来自上述正式运行基线。
加载器身份改名后，安装时应替换本项目旧 jar；原资源命名空间的保留不构成跨实现的存档转换承诺。

## 功能与迁移范围

- 八套原创结构与分步讲解，简体中文和英文。
- 使用 AE2S 1.1.0 的真实方块与 multipart 部件，按物品关联到 Ponder 入口。
- 四个教程分类，支持关键帧、框选、物品移动和时间轴回放。

## 与上游的具体差异

| 项目 | 上游基线 | 本 Legacy 版本 |
| --- | --- | --- |
| 项目来源 | AE2S 提供网络与机器；Ponder 提供演示框架 | 这是原创教程附属，没有另一个被重新署名的上游教程 Mod。AE2S 与 Ponder 作者分别保留归属。 |
| 功能边界 | AE2S 核心存储与自动合成逻辑 | 新增教程内容，不替换 AE2S 核心实现，不调整配方、容量或频道平衡。 |
| 演示方式 | 实际游戏中的 ME 网络运行 | 在 Ponder 虚拟世界中编排操作流程；不把演示动画当作真实合成网络执行结果。 |
| 依赖方式 | AE2S / Ponder 独立项目 | 只对 AE2S 1.1.0 系列编译和验证；Ponder 可选，未安装时不注册教程，不内嵌两者代码。 |
| 运行端 | 核心 AE2S 需要相应运行环境 | 教程入口仅客户端启用，服务端无需安装；意外装入正式 0.4.0 专服时含限定版本的发现兼容修复。 |

## 尚未实现与兼容边界

- 覆盖入门与基础自动化流程；高级内存卡专属界面、多输入 P2P、请求器等尚无专门场景。
- 频道数值按默认设置讲解，整合包更改频道配置后需相应调整理解。
- 不声明原版 AE2 1.12.2、AE2UEL 或现代官方 Ponder 的二进制兼容。

## 依赖

- 必需：AE2S 1.1.0（实际加载器 ID ae2），锁定官方 dev/runtime 文件的 SHA-256。
- 教程启用条件：Ponder Legacy 1.4.0-cleanroom-alpha.1 与 CraftTweaker 4.1.20.698。

## 使用方式

1. 安装 AE2S 与本附属；若要观看教程，另装 Ponder Legacy 和 CraftTweaker。
2. 悬停驱动器、样板供应器或 ME P2P 隧道并按住 W。
3. `/ponder index` 浏览分类，或使用 `/ponder ae2:drive` 等命令进入。

## 构建与 CI

在完整源码项目目录使用 Java 25 执行：

```bash
python3 tools/bootstrap_legacy.py
bash gradlew --no-daemon :build :reobfJar --console=plain
python3 tools/verify_legacy_package.py
```

CI 会准备固定版本的源码依赖，构建完整主源码与测试，并检查发行 jar 的身份、作者和图标。
仅有文档的仓库会明确报告 scaffold，不把跳过编译标为 Mod 构建成功。CI 构建不能替代客户端玩法和专服验收。

## 发布平台

CurseForge / Modrinth 的项目资料、文件、依赖和 CI 凭据配置见 [发布说明](docs/PUBLISHING.md)。平台尚未发布的状态见 PUBLICATION.md。

## 授权与图像

本附属的原创源码与结构按仓库 LICENSE 发布；AE2S、Ponder、CraftTweaker 为独立依赖，不随本附属重新分发。

此版本作者为 **yudream**，上游作者与版权保留如上。`branding/icon.png` 和 `branding/cover.png` 为本项目生成的展示图，
以代表物品或概念表现项目；不作为游戏实机截图，也不改变上游游戏资源的授权。生成记录见 `branding/provenance.json`。

<!-- legacy-overview:end -->

## 详细使用与开发说明

为 **Applied Energistics 2 Supergiant（应用能源 2 超巨星，AE2S）** 制作的独立思索附属模组。
版本 `0.1.0`，客户端兼容目标为 **AE2S 1.1.0 / Cleanroom 0.4.0 / Java 25**。
AE2S 身份见 [MC 百科](https://www.mcmod.cn/class/28382.html)，运行依赖见 [AE2S 1.1.0 发布页](https://github.com/FormlessDragon/Applied-Energistics-2-Supergiant/releases/tag/v1.1.0)。

## 安装与使用

1. 在 **Cleanroom 0.4.0 / Minecraft 1.12.2 / Java 25** 客户端安装 **AE2S 1.1.0**。
2. 安装本仓库的 **Ponder Cleanroom 1.4.0-cleanroom-alpha.1** 及其运行依赖 **CraftTweaker 4.1.20.698**。
3. 将 `build/libs/ae2s-ponder-legacy-0.1.0.jar` 放入 `mods/`。
4. 悬停相应物品，按住 **W**；或运行 `/ponder ae2:drive`、`/ponder ae2:pattern_provider`、`/ponder ae2:me_p2p_tunnel`。
   `/ponder index` 打开索引，包含本附属的四个分类。界面语言跟随游戏，支持简体中文和英文。

`-mcp.jar` 和 `-sources.jar` 是开发文件，不要作为第二份模组安装。
本模组为客户端教程附属，服务端无需安装。Ponder 为可选依赖：不安装时，附属不会注册教程，AE2S 核心玩法正常运行。
Ponder 自身在远程服务器上的版本和联网要求以 [Ponder 文档](https://github.com/mcyudream/ponder-legacy) 为准。
请使用本工作区重新构建的 Ponder 安装 jar；本次同时修复了多物品关联的重复场景误报和发布包缺少 Mixin refmap 的问题。

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

结构使用真实 AE2S 方块与 multipart 部件。说明、框选与物品移动在 Ponder 虚拟世界中编排，
不是在虚拟世界里运行完整的 ME 自动合成系统；实际操作步骤与所需供电、存储、频道均在讲解中说明。
频道数值以正常频道设置为准；整合包修改配置后可能不同。

## 构建与开发

本工程使用同级 `../ponder` 或 bootstrap 获取的 `.legacy-deps/ponder`，通过编译期依赖使用其公共插件 API，不把 Ponder 或 AE2S 打入发布 jar。
编译工具链使用 Cleanroom `0.7.14-alpha` 的 userdev；官方 `0.4.0` 未提供当前 CleanroomGradle 所需的 userdev 工件。
最低加载器声明保持 `0.4.0`，基线验证使用官方 0.4.0 安装环境与真实安装 jar。

```bash
export JAVA_HOME=/path/to/jdk-25
./gradlew :build
./gradlew :runClient -PwithPonder
./gradlew :runClient                  # 不安装 Ponder 的运行环境

# 自动真实客户端验证，完成后退出
./gradlew :runClient -PwithPonder -Psmoke
./gradlew :runClient -PwithPonder -Psmoke -PpackagedSmoke
./gradlew :runClient -Psmoke -PpackagedSmoke

# 结构为本项目原创，可确定性再生成和校验
python3 tools/generate-structures.py
python3 tools/generate-structures.py --check

# 官方 CR 0.4.0 环境，无 userdev 重映射（Linux x64）
./gradlew :build :reobfDevHarnessJar :ponder:reobfJar
python3 tools/verify-cleanroom.py client --with-ponder
python3 tools/verify-cleanroom.py client
python3 tools/verify-cleanroom.py server --with-ponder
python3 tools/verify-cleanroom.py server
```

本工作区可使用 `./tools/dev.sh :build`，自动选择 `../../.dev/` 的 Java 25；
其他位置可设置 `AE2S_PONDER_JAVA_HOME`。
第一次开发运行会从官方发布下载 AE2S `-dev.jar`，并按 `dependency-lock.json` 校验 SHA-256。
可通过 `AE2S_CACHE` 指定保存了相同官方文件的缓存目录。所有运行依赖均独立安装，不在本模组中重新分发。

开发客户端和独立服务器分别位于 `run/client/` 和 `run/server/`。
专用服务器可执行 `./gradlew :runServer -Psmoke` 或加上 `-PwithPonder`；
完整开服前需由服务器所有者自行阅读并接受 Minecraft EULA。验证程序不会代为接受；
官方运行验证会复用 `run/server/eula.txt` 中已有的本地测试服确认。
本附属无需在服务端安装；若装入正式 0.4.0 专服，包含限定于该版本的 Kirino 发现兼容修复。当前两种组合的检查见 PUBLICATION.md。

## 维护入口

- `src/main/java/dev/yudream/ae2sponder/AE2SPonder.java`：无 Ponder 类型引用的客户端条件入口。
- `compat/Lesson.java`：场景、物品关联与分类；所有场景 ID 使用 `ae2s_ponder` 命名空间。
- `compat/AE2SScenes.java`：逐步流程、关键帧、输入提示、框选与物品动画。
- `assets/ae2s_ponder/lang/`：中英文标题与讲解；英文文件同时提供 Ponder 的后备语言。
- `tools/generate-structures.py`：结构源数据及 AE2S 1.1.0 部件 NBT，生成到 `assets/ae2s_ponder/ponder/`。
- `src/dev/`：独立验证模组，只在 `-Psmoke` 时安装，不进入发布 jar。
- [验证记录](docs/VERIFICATION.md)：本次实际执行的检查与范围。

支持 AE2S / Supergiant，不声明兼容原版 AE2 1.12.2、AE2UEL 或现代官方 Ponder。
当前附属覆盖上述基础流程；AE2S 的高级内存卡专属界面、多输入 P2P、请求器等功能可在此基础上继续补充。
