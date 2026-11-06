# 来源与运行依赖

本附属的 Java 场景、结构编排与中英文讲解为本项目新增内容，使用 MIT 许可证。
工程包含 Gradle Wrapper（Gradle 项目，Apache-2.0）。

运行依赖不嵌入、不重新分发：

- Applied Energistics 2 Supergiant（AE2S）：[源码与许可证](https://github.com/FormlessDragon/Applied-Energistics-2-Supergiant)，基于 Applied Energistics 2；具体代码、API 与资源许可见其 LICENSE。通过注册 ID 与 AE2S 1.1.0 的结构 NBT 使用已安装模组的方块、物品和模型。
- Ponder Cleanroom：本仓库 `../ponder`，其来源与 MIT 许可见该项目的 NOTICE.md / LICENSE。
- Cleanroom、CraftTweaker 与 Minecraft：各自的许可与分发条款适用。

没有从 AE2S 复制纹理、模型或实现类；教程中的这些资源由用户安装的 AE2S 提供。
`dependency-lock.json` 记录实际使用的官方 AE2S 1.1.0 文件和 SHA-256。

## 教程主题参考

新增教程按官方 AE2 GuideME 的主题组织，参考 [AppliedEnergistics/Applied-Energistics-2](https://github.com/AppliedEnergistics/Applied-Energistics-2) 1.21.1 分支，固定参考提交 `7a11e9af14dd3283bc7122f3879e7793a6e1b7c7`。
讲解与结构由本项目重新编写，并核对 AE2S 1.1.0 的注册、接口与使用方式。未复制官方教程纹理、模型或现代渲染器；未将现代版行为直接声明为 AE2S 行为。生成器保留对应主题的来源路径。
