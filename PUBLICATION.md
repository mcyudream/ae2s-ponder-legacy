# AE2S Ponder Legacy 发布状态

- 原创附属作者与维护者：**yudream**。源码、结构与讲解按 MIT 发布；依赖来源与授权见 [README](README.md) / [NOTICE](NOTICE.md)。
- Minecraft 1.12.2 / **Cleanroom 0.4.0 正式版** / Java 25 验收：**PASS**，见 [正式记录](LEGACY-VERIFICATION.md)。
- GitHub：[源码](https://github.com/mcyudream/ae2s-ponder-legacy)、[构建与发布 CI](https://github.com/mcyudream/ae2s-ponder-legacy/actions/workflows/ci.yml)、[0.1.1 发行页](https://github.com/mcyudream/ae2s-ponder-legacy/releases/tag/v0.1.1)。
- `v0.1.1` 标签触发 CI 构建，核对实际运行验收哈希后发布安装包、源码包与 `SHA256SUMS`。更新说明见 [0.1.1](docs/releases/0.1.1.md)。
- CurseForge / Modrinth：尚未创建项目或上传版本。
- Loader Mod ID：`ae2s-ponder-legacy`；资源与场景空间：`ae2s_ponder`。

安装时替换本项目旧 jar，并独立安装 README 中的依赖。早期 `0.4.0-alpha` 记录与正式 `0.4.0` 验收分别保留。

0.1.1 修复 Ponder 正式 1.4.0 的版本范围误判；实际客户端和专服组合均重新验收。
