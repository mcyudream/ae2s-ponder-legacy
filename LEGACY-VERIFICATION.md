# AE2S Ponder Legacy 正式基线验收

- 日期：2026-11-03。
- 环境：Minecraft 1.12.2 / **Cleanroom 0.4.0 正式版（无 -alpha）** / Java 25。
- 生产安装包：`ae2s-ponder-legacy-0.1.0.jar`。
- SHA-256：`2ab4282a0ec10c40c5eabd0e89494994e98c0a8fe5807269f6f2a0aa7a27ef6b`。
- 作者、loader ID、展示名与打包图标另由 `tools/verify_legacy_package.py` 检查。

| 组合 | 结果 | 断言数 | 证据 |
| --- | --- | --- | --- |
| client-without-ponder | PASS | 5 | [报告](docs/verification/legacy-identity/cleanroom-0.4.0-final/client-without-ponder/report.json) |
| client-with-ponder | PASS | 551 | [报告](docs/verification/legacy-identity/cleanroom-0.4.0-final/client-with-ponder/report.json) |
| server-without-ponder | PASS | 3 | [报告](docs/verification/legacy-identity/cleanroom-0.4.0-final/server-without-ponder/report.json) |
| server-with-ponder | PASS | 3 | [报告](docs/verification/legacy-identity/cleanroom-0.4.0-final/server-with-ponder/report.json) |

## 覆盖范围

AE2S 1.1.0 安装包发现、无 Ponder 时安全停用教程、有 Ponder 时八个场景的结构与完整时间轴、英文/中文讲解及画面，以及两种专服启动。客户端有 Ponder 报告含 551 个断言。

每份 runtime.json 记录该组合实际安装的 jar 和哈希，包括可选 Ponder、CraftTweaker 或 JEI。验收使用官方安装器的生产运行库与 SRG 安装包，不将 userdev / 其他 Cleanroom 版本作为本基线的运行证据。

正式 0.4.0 专服的 Kirino 发现兼容修复仅在该版本的物理专服生效，不改动官方加载器 jar。客户端图像检查使用 Linux llvmpipe 和空音频后端；未覆盖全部硬件及任意整合包组合。功能差异与未实现项目仍以 README 为准。

## 0.1.0 发行依赖组合复查

2026-11-03 使用已公开发行的 Ponder Legacy `v1.4.0-cleanroom-alpha.1` 安装包，重新检查同一附属安装包在正式 CR 0.4.0 上的运行结果。

- Ponder SHA-256：`9be55d18dff404d74b886521395c47cc6d2c5ec1ff3d22d73fecb1553f9ee4ab`。
- 客户端：**PASS，551 项**，八个教程中英文完整播放、回退重放及真实网络检查；[报告](docs/verification/release-0.1.0/client-with-ponder/report.json)、[环境](docs/verification/release-0.1.0/client-with-ponder/runtime.json)。
- 专用服务器：**PASS，3 项**，到达 `FMLServerStarted`；[报告](docs/verification/release-0.1.0/server-with-ponder/report.json)、[环境](docs/verification/release-0.1.0/server-with-ponder/runtime.json)。
- 未安装 Ponder 的两组结果使用上表中同一附属 SHA-256 的正式基线记录。早期记录保持原始依赖摘要。

CI 发布同时核对安装包哈希、四组正式基线报告及上述公开 Ponder 发行包的两组复查报告。
