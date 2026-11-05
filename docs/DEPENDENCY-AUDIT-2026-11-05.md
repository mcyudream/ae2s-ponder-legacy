# 已发布模组依赖范围检查（2026-11-05）

## 结论

检查 mcyudream 已公开发布的六个 Minecraft 1.12.2 Mod 项目，包含最新版和仍公开的历史安装文件，共 **14 个发行安装包记录**，读取真实 jar 的 `@Mod` 注解及 `mcmod.info`，使用 **Cleanroom 0.4.0 自带 FML 的 VersionParser / DefaultArtifactVersion** 判断版本范围。

唯一复现“旧预发行最低版本拒绝新正式版”的发行安装包为 **AE2S Ponder Legacy 0.1.0**。0.1.1 已改为 `after:ponder-legacy@[1.4.0,)`，并重新执行正式 0.4.0 的四组运行验收。

| 项目 | 检查版本 | 本次结果 |
| --- | --- | --- |
| [AE2S Ponder Legacy](https://github.com/mcyudream/ae2s-ponder-legacy/releases) | 0.1.0 | 旧范围拒绝 Ponder 1.4.0；修复为 0.1.1 |
| [Hostile Neural Networks Legacy](https://github.com/mcyudream/hostile-neural-networks-legacy/releases) | 6.5.1-cleanroom.1 / .2 / .3 | `after:ponder-legacy` 不限定 Ponder 版本，未发现同类拒绝 |
| [Powah Legacy](https://github.com/mcyudream/powah-legacy/releases) | 5.1.0-cleanroom-alpha.2 | `after:ponder-legacy` 不限定 Ponder 版本，未发现同类拒绝 |
| [Ponder Legacy](https://github.com/mcyudream/ponder-legacy/releases) | 1.4.0、1.4.0-cleanroom-alpha.1 | 对正式 CR 0.4.0 的下限通过；未发现同类问题 |
| [Industrial Platform](https://github.com/mcyudream/IndustrialPlatform/releases) | 2.4.4、2.4.2，nightly 内 2.1.0 / 2.4.2 / 2.4.4 | 可选 KubeJS / Create 未限定版本，未发现同类范围 |
| [Smart Workbench](https://github.com/mcyudream/Smart-workbench/releases) | 1.0.1、1.0.0 | 无依赖版本范围；1.0.0 曾有注解/元数据版本不一致，最新版 1.0.1 已统一 |

另发现 Ponder 仓库的 **Java 附属示例**仍使用 `1.4.0-cleanroom-alpha.1` 作为下限，且其 `mcmod.info` 仍引用旧 ID `ponder_legacy`。示例已统一为 `ponder-legacy@[1.4.0,)` 和版本 1.4.0，并增加使用 FML 解析器的示例回归测试。该示例不在 Ponder 生产 jar 中，已安装的 Ponder 1.4.0 无需替换。

## 范围与证据

- 发行包 SHA-256、实际注解、元数据及逐条结果见 [原始报告](verification/dependency-audit-2026-11-05/report.json)。下载时对 GitHub 提供的 SHA-256 逐项校验；未提供摘要的历史文件在报告中明确标记。
- 42 条依赖声明，以当前公开版本及 Cleanroom 0.4.0、AE2S 1.1.0、CraftTweaker 4.1.20.698 为比较对象。没有比较对象的第三方扩展标为 `EXTERNAL_NOT_IN_AUDIT`，不当作通过。
- 本检查用于发现依赖声明和版本排序错误，不替代各模组的客户端功能或专服验收。其他 Minecraft 版本、Bukkit / Velocity 插件、未发布源码工程未纳入这份 1.12.2 检查。
- 历史安装包及标签保持原样；修复通过新版本提供。
