# 越狱源工作约束

## 插件与文件命名

- 新增或重新打包的插件交付文件名，统一使用：`App名 功能简述 环境.扩展名`，文件名中不写版本号。
- 示例：`VVebo 全功能解锁 RootHide.deb`；TrollStore 动态库示例：`VVebo 全功能解锁 TrollStore.dylib`。
- App 名、简短功能、安装环境之间以空格分隔；功能描述保持简洁。环境使用 `Rootful`、`Rootless`、`RootHide`、`TrollStore` 或 `TrollFools` 等明确名称。
- 同一 App、功能和环境需要保留多个构建时，在环境后加简短的用途或状态说明来区分，不使用版本号。
- 该规则适用于 `.deb`、`.dylib`、`.zip` 等交付文件名。现有 Debian `Package` 标识符保持稳定，避免影响已安装用户的升级关系。
- `.deb` 的版本号由包内控制信息和 APT `Packages` 索引的 `Version` 字段记录；整理文件名时不改包版本。
- 已发布文件名默认保留；用户明确要求统一整理时，按本规则迁移，并同步更新 README 链接和软件源索引。发布到远端仍须有明确授权。

## 软件源索引

- 新增或改名 `.deb` 后，将文件放入 `pool/main/`，并运行 `python3 scripts/reindex.py` 更新索引。
- 更新后核对生成的 `Filename` 与实际文件路径一致，并检查 README 中的文件链接。
