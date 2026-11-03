# Komaki Zhu 越狱插件源 / Komaki Zhu Jailbreak Source

Komaki Zhu 的 Sileo/APT 越狱插件源，目前收录 NFComa Apple Pay Alert Guard。软件源名称和头像使用 Komaki Zhu 的 GitHub 资料。

Sileo 的“添加源”会直接请求源根目录下的 `Release`，所以索引脚本同时生成根目录平面索引和标准 `dists/stable/` 索引。

The Komaki Zhu Sileo/APT source currently hosts NFComa Apple Pay Alert Guard. The source name and icon use Komaki Zhu's GitHub profile.

Sileo's simple “Add Source” flow requests `Release` from the repository root. The index script therefore generates both flat root indexes and the standard `dists/stable/` layout.

## 当前插件 / Current Tweak

**NFComa Apple Pay Alert Guard** 会自动关闭 iPhone 显示的“无法使用 Apple Pay”提示。它不会修复或启用 Apple Pay、NFC，也不能代替越狱注入器。

This tweak automatically closes the “Apple Pay unavailable” alert on iPhone. It does not fix or enable Apple Pay or NFC, and it does not replace the jailbreak injector.

提供三种越狱安装包：Rootful（`iphoneos-arm`）、Rootless（`iphoneos-arm64`）和 RootHide（`iphoneos-arm64e`）。请安装与你的越狱环境相符的版本；没有 TrollStore 安装包。

Three jailbreak packages are available: Rootful (`iphoneos-arm`), Rootless (`iphoneos-arm64`), and RootHide (`iphoneos-arm64e`). Install the package that matches your jailbreak. There is no TrollStore package.

## Sileo 源地址 / Sileo Source URLs

- 国内友好 CDN / China-friendly CDN：`https://cdn.jsdelivr.net/gh/komakizhu/komaki-packages@main/`
- GitHub Pages：`https://komakizhu.github.io/komaki-packages/`

两个地址都可直接添加到 Sileo。/ Both URLs can be added directly in Sileo.

## 更新索引 / Updating the Index

```sh
python3 scripts/reindex.py
```

后续插件放入 `pool/main/`，对应包图标放入 `icons/<Package>.png`，运行脚本生成源索引。/ Put future packages in `pool/main/`, add icons under `icons/<Package>.png`, and run the script to regenerate the indexes.

脚本会读取 `pool/**/*.deb`，生成根目录 `Release`、`Packages`、`Packages.gz`，以及按架构分开的标准 APT 索引。/ The script reads `pool/**/*.deb` and generates root `Release`, `Packages`, and `Packages.gz` files plus architecture-specific standard APT indexes.

本仓库只放越狱插件包、软件源头像、包图标和索引，不放 NFComa App、IPA 或 App 源码。/ This repository contains jailbreak packages, the source avatar, package icons, and indexes. It does not contain the NFComa app or IPA.
