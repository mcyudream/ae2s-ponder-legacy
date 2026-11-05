# AE2S Ponder Legacy 0.1.1 正式基线验收

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
