# Komaki 越狱插件源

这是 Komaki 的通用 Sileo/APT 软件源，先收录 NFComa Apple Pay Alert Guard。Sileo 的“添加源”会直接请求源根目录下的 `Release`，所以索引脚本同时生成根目录平面索引和标准 `dists/stable/` 索引。后续插件放入 `pool/main/`，对应包图标放入 `icons/<Package>.png`，然后运行 `python3 scripts/reindex.py` 并推送 `main`。

## Sileo 源地址

- 国内友好 CDN：`https://cdn.jsdelivr.net/gh/komakizhu/komaki-packages@main/`
- GitHub Pages：`https://komakizhu.github.io/komaki-packages/`

两个地址都可直接添加到 Sileo；源根目录含有 `Release`、`Packages` 和 `Packages.gz`，同时保留标准 APT 索引路径 `dists/stable/`。

jsDelivr 官方 CDN 声明在中国周边设有节点；GitHub 分支路径可能缓存最多 12 小时，因此刚推送的新包在该地址出现可能有延迟。GitHub Pages 提供另一条可用入口。若要使用单一自有域名并接入中国内地 CDN，需要已备案域名和相应 CDN 服务。

## 更新索引

```sh
python3 scripts/reindex.py
```

脚本会读取 `pool/**/*.deb`，生成 Sileo 直接添加源所需的根目录 `Release`、`Packages`、`Packages.gz`，以及按架构分开的 `dists/stable/` 索引。包图标使用 `icons/<Package>.png`，生成的 Icon 字段指向 jsDelivr CDN。

本仓库只放越狱插件包、包图标和索引，不放 NFComa App、IPA 或 App 源码。
