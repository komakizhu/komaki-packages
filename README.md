# Komaki Zhu 越狱插件源 / Komaki Zhu Jailbreak Source

Komaki Zhu 的 Sileo/APT 越狱插件源，目前收录 NFComa Apple Pay Alert Guard、小红书防自动刷新和 BiliShareBridge。软件源名称和头像使用 Komaki Zhu 的 GitHub 资料。

Sileo 的“添加源”会直接请求源根目录下的 `Release`，所以索引脚本同时生成根目录平面索引和标准 `dists/stable/` 索引。

The Komaki Zhu Sileo/APT source currently hosts NFComa Apple Pay Alert Guard, XHS No Startup Refresh, and BiliShareBridge. The source name and icon use Komaki Zhu's GitHub profile.

Sileo's simple “Add Source” flow requests `Release` from the repository root. The index script therefore generates both flat root indexes and the standard `dists/stable/` layout.

## 当前插件 / Current Tweak

**NFComa Apple Pay Alert Guard** 会自动关闭 iPhone 显示的“无法使用 Apple Pay”提示。它不会修复或启用 Apple Pay、NFC，也不能代替越狱注入器。

This tweak automatically closes the “Apple Pay unavailable” alert on iPhone. It does not fix or enable Apple Pay or NFC, and it does not replace the jailbreak injector.

提供三种越狱安装包：Rootful（`iphoneos-arm`）、Rootless（`iphoneos-arm64`）和 RootHide（`iphoneos-arm64e`）。请安装与你的越狱环境相符的版本。

Three jailbreak packages are available: Rootful (`iphoneos-arm`), Rootless (`iphoneos-arm64`), and RootHide (`iphoneos-arm64e`). Install the package that matches your jailbreak.

### 小红书防自动刷新 / XHS No Startup Refresh

阻止小红书打开或回到前台时自动刷新首页，保留手动刷新和继续加载；用户触摸或滚动后会放行请求。
三个 `.deb` 的文件名使用“中文名-版本-环境”规则；另外提供一个可供 TrollStore/TrollFools 注入的通用动态库：

- [Rootful `.deb`](pool/main/小红书防自动刷新-0.1.0-rootful.deb)
- [Rootless `.deb`](pool/main/小红书防自动刷新-0.1.0-rootless.deb)
- [RootHide `.deb`](pool/main/小红书防自动刷新-0.1.0-roothide.deb)
- [TrollStore/TrollFools `.dylib`](artifacts/小红书防自动刷新-0.1.0-1-trollstore.dylib)

Keeps the Xiaohongshu home feed stable when the app opens or returns to the foreground. Manual refresh and pagination remain available, and requests are released after user interaction. The TrollStore/TrollFools file is a universal arm64/arm64e dylib for injection; it is not a pre-injected IPA.

### 哔哩哔哩分享桥接 / BiliShareBridge

将支持的视频、番剧、直播间和空间内容交给 iOS 系统分享面板，并为蓝色分身转换 `bilibili` / `bilitwin` 链接。Sileo 条目使用 B 站 8.76.0 App 图标；源头像保持不变。

Routes supported video, series, live room, and space shares to the iOS system share sheet, and translates `bilibili` / `bilitwin` URLs for the blue app variant. The Sileo package icon uses the Bilibili 8.76.0 app icon; the source avatar is unchanged.

三个 `.deb` 仅含自研桥接库，不含 `BiliBiliTweak` 或 8.89 专用 `BiliNetworkCompat`：

- [有根 Rootful `.deb`](pool/main/哔哩哔哩分享桥接-1.1.1-rootful.deb)
- [无根 Rootless `.deb`](pool/main/哔哩哔哩分享桥接-1.1.1-rootless.deb)
- [RootHide `.deb`](pool/main/哔哩哔哩分享桥接-1.1.1-roothide.deb)
- [TrollFools `.zip`](artifacts/哔哩哔哩分享桥接-1.1.1-1-trollfools.zip)
- [通用 `.dylib`](artifacts/哔哩哔哩分享桥接-1.1.1-1-trollstore.dylib)

All three `.deb` files contain only the original bridge, not `BiliBiliTweak` or the 8.89-only `BiliNetworkCompat`.

## Sileo 源地址 / Sileo Source URLs

- 当前推荐 / Recommended now：`https://komakizhu.github.io/komaki-packages/`
- 国内友好 CDN / China-friendly CDN：`https://cdn.jsdelivr.net/gh/komakizhu/komaki-packages@main/`

GitHub Pages 已同步当前索引和安装包，可直接添加到 Sileo。jsDelivr 的 `@main` 缓存可能暂时保留旧索引；如果刷新时报 404 或校验错误，请改用 GitHub Pages 地址。

GitHub Pages currently serves the latest indexes and packages and can be added directly to Sileo. The jsDelivr `@main` cache may temporarily serve old indexes. If a refresh reports a 404 or checksum error, use the GitHub Pages URL.

## 更新索引 / Updating the Index

```sh
python3 scripts/reindex.py
```

后续插件放入 `pool/main/`，对应包图标放入 `icons/<Package>.png`，运行脚本生成源索引。/ Put future packages in `pool/main/`, add icons under `icons/<Package>.png`, and run the script to regenerate the indexes.

脚本会读取 `pool/**/*.deb`，生成根目录 `Release`、`Packages`、`Packages.gz`，以及按架构分开的标准 APT 索引。/ The script reads `pool/**/*.deb` and generates root `Release`, `Packages`, and `Packages.gz` files plus architecture-specific standard APT indexes.

本仓库只放越狱插件包、TrollStore 动态库、软件源头像、包图标和索引，不放 NFComa App、IPA 或 App 源码。/ This repository contains jailbreak packages, the TrollStore dylib, the source avatar, package icons, and indexes. It does not contain the NFComa app or IPA source.
