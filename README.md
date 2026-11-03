# AE2S Ponder Legacy

![AE2S Ponder Legacy](branding/cover.png)

<!-- legacy-overview:start -->
由 yudream 编写的 AE2S 基础教程附属。通过八个可回放场景讲清 ME 网络、存储、频道、总线、自动合成、处理样板和 P2P 的搭建顺序。

## 当前状态

> **公开仓库目前包含项目介绍、上游差异、图像与 CI 框架。Mod 源码尚未提交，等待对应迁移验收完成。CI 此时只报告 scaffold，没有执行 Mod 编译。**

当前为进行中的迁移或改名后验收阶段。构建通过、接口已导入和历史测试结果均不等于完整移植完成。当前源码提交与产物状态见 [PUBLICATION.md](PUBLICATION.md)；未通过验收的项目暂不提供成品发布。

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

源码提交后，使用 Java 25，在项目目录执行：

```bash
python3 tools/bootstrap_legacy.py
bash gradlew --no-daemon :build :reobfJar --console=plain
python3 tools/verify_legacy_package.py
```

CI 会准备固定版本的源码依赖，构建完整主源码与测试，并检查发行 jar 的身份、作者和图标。
仅有文档的仓库会明确报告 scaffold，不把跳过编译标为 Mod 构建成功。CI 构建不能替代客户端玩法和专服验收。

## 授权与图像

本附属的原创源码与结构按仓库 LICENSE 发布；AE2S、Ponder、CraftTweaker 为独立依赖，不随本附属重新分发。

此版本作者为 **yudream**，上游作者与版权保留如上。`branding/icon.png` 和 `branding/cover.png` 为本项目生成的展示图，
以代表物品或概念表现项目；不作为游戏实机截图，也不改变上游游戏资源的授权。生成记录见 `branding/provenance.json`。

<!-- legacy-overview:end -->
