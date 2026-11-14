# Komaki Zhu 越狱插件源 / Komaki Zhu Jailbreak Source

Komaki Zhu 的 Sileo/APT 越狱插件源，目前收录 NFComa 屏蔽钱包异常、小红书防自动刷新和 Bili-komaki。旧版 BiliShareBridge 的 TrollStore/TrollFools 独立注入文件仍保留。软件源名称和头像使用 Komaki Zhu 的 GitHub 资料。

Sileo 的“添加源”会直接请求源根目录下的 `Release`，所以索引脚本同时生成根目录平面索引和标准 `dists/stable/` 索引。

The Komaki Zhu Sileo/APT source currently hosts NFComa Wallet Alert Suppression, XHS No Startup Refresh, and Bili-komaki. Standalone TrollStore/TrollFools injection artifacts for the older BiliShareBridge remain available. The source name and icon use Komaki Zhu's GitHub profile.

Sileo's simple “Add Source” flow requests `Release` from the repository root. The index script therefore generates both flat root indexes and the standard `dists/stable/` layout.

## 当前插件 / Current Tweak

**NFComa 屏蔽钱包异常** 会自动关闭 iPhone 显示的“无法使用 Apple Pay”提示。它不会修复或启用 Apple Pay、NFC，也不能代替越狱注入器。

NFComa Wallet Alert Suppression automatically closes the “Apple Pay unavailable” alert on iPhone. It does not fix or enable Apple Pay or NFC, and it does not replace the jailbreak injector.

提供三种越狱安装包：Rootful（`iphoneos-arm`）、Rootless（`iphoneos-arm64`）和 RootHide（`iphoneos-arm64e`）。请安装与你的越狱环境相符的版本。

Three jailbreak packages are available: Rootful (`iphoneos-arm`), Rootless (`iphoneos-arm64`), and RootHide (`iphoneos-arm64e`). Install the package that matches your jailbreak.

这个插件目前有 Rootful、Rootless 和两个 RootHide 构建：

- [NFComa 屏蔽钱包异常 Rootful](pool/main/NFComa%20%E5%B1%8F%E8%94%BD%E9%92%B1%E5%8C%85%E5%BC%82%E5%B8%B8%20Rootful.deb)
- [NFComa 屏蔽钱包异常 Rootless](pool/main/NFComa%20%E5%B1%8F%E8%94%BD%E9%92%B1%E5%8C%85%E5%BC%82%E5%B8%B8%20Rootless.deb)
- [NFComa 屏蔽钱包异常 RootHide（旧构建）](pool/main/NFComa%20%E5%B1%8F%E8%94%BD%E9%92%B1%E5%8C%85%E5%BC%82%E5%B8%B8%20RootHide%20%E6%97%A7%E6%9E%84%E5%BB%BA.deb)
- [NFComa 屏蔽钱包异常 RootHide](pool/main/NFComa%20%E5%B1%8F%E8%94%BD%E9%92%B1%E5%8C%85%E5%BC%82%E5%B8%B8%20RootHide.deb)

## 统一命名规则 / Naming Convention

插件交付文件统一使用 `App名 功能简述 环境.扩展名`，文件名不包含版本号。例如：`VVebo 全功能解锁 RootHide.deb` 和 `VVebo 全功能解锁 TrollStore.dylib`。App 名、功能和环境之间用空格分隔；功能描述保持简洁。同一环境有多个构建时，加简短说明区分。APT 的 `Package` 标识符保持稳定，`.deb` 版本由包内信息及索引的 `Version` 字段记录。

Use `App name Short feature Environment.extension` for plugin delivery filenames, without a version number. For multiple builds of the same environment, add a short descriptive qualifier. Keep the stable Debian `Package` identifier unchanged; `.deb` package metadata and the APT `Version` field record its version.

### 小红书防自动刷新 / XHS No Startup Refresh

阻止小红书打开或回到前台时自动刷新首页，保留手动刷新和继续加载；用户触摸或滚动后会放行请求。
另外提供一个可供 TrollStore/TrollFools 注入的通用动态库：

- [Rootful `.deb`](pool/main/%E5%B0%8F%E7%BA%A2%E4%B9%A6%20%E9%98%B2%E8%87%AA%E5%8A%A8%E5%88%B7%E6%96%B0%20Rootful.deb)
- [Rootless `.deb`](pool/main/%E5%B0%8F%E7%BA%A2%E4%B9%A6%20%E9%98%B2%E8%87%AA%E5%8A%A8%E5%88%B7%E6%96%B0%20Rootless.deb)
- [RootHide `.deb`](pool/main/%E5%B0%8F%E7%BA%A2%E4%B9%A6%20%E9%98%B2%E8%87%AA%E5%8A%A8%E5%88%B7%E6%96%B0%20RootHide.deb)
- [TrollStore/TrollFools `.dylib`](artifacts/%E5%B0%8F%E7%BA%A2%E4%B9%A6%20%E9%98%B2%E8%87%AA%E5%8A%A8%E5%88%B7%E6%96%B0%20TrollStore.dylib)

Keeps the Xiaohongshu home feed stable when the app opens or returns to the foreground. Manual refresh and pagination remain available, and requests are released after user interaction. The TrollStore/TrollFools file is a universal arm64/arm64e dylib for injection; it is not a pre-injected IPA.

### 哔哩哔哩 Bili-komaki

把 B 站竖屏视频交给普通视频播放器打开，并提供首页防自动重载的总开关和分开关。支持粉色与蓝色 B 站客户端。当前 Sileo 包版本为 **2.0.0**。条目沿用原来的 B 站 App 图标，软件源头像不变；Debian 包标识保持稳定，旧条目可直接升级。

Routes Bilibili portrait videos to the standard video player and provides master and separate switches for home refresh suppression. It targets both pink and blue Bilibili clients. The current Sileo package version is **2.0.0**. The package keeps the existing Bilibili app icon and stable Debian package identifier, so the old entry upgrades in place; the source avatar is unchanged.

- [Rootful `.deb`](pool/main/%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9%20Bili-komaki%20Rootful.deb)
- [Rootless `.deb`](pool/main/%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9%20Bili-komaki%20Rootless.deb)
- [RootHide `.deb`](pool/main/%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9%20Bili-komaki%20RootHide.deb)

旧版 BiliShareBridge 的独立注入文件保留在源中，不包含在上述 Bili-komaki `.deb` 内：

- [旧版 TrollFools `.zip`](artifacts/%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9%20%E5%88%86%E4%BA%AB%E6%A1%A5%E6%8E%A5%20TrollFools.zip)
- [旧版 TrollStore `.dylib`](artifacts/%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9%20%E5%88%86%E4%BA%AB%E6%A1%A5%E6%8E%A5%20TrollStore.dylib)

### Quantumult X 设置 VPN 冷启动修复 / Quantumult X Settings VPN Cold Start Fix

面向 iOS 17.3.1、RootHide 和 arm64e 上的 Quantumult X 1.8.1（build 951）。系统从“设置 → VPN”启动且 QX 主程序未运行时，如果 Tunnel 收到 nil 启动参数，此插件会向 QX 原生 provider 转发空字典；非空参数原样传递，QX 自己的校验和错误处理保持有效。真机日志确认 QX 主程序未运行时 provider 启动回调成功；实际隧道流量和 BetterCCVPN 尚未单独验证。

Targets Quantumult X 1.8.1 (build 951) on iOS 17.3.1 with RootHide on arm64e. When iOS Settings starts the VPN while the QX app is not running, the tweak forwards an empty dictionary if the Tunnel receives nil options. Non-nil options and QX's native validation and error handling are preserved. Device logs confirm a successful provider callback with the QX app absent; actual tunnel traffic and BetterCCVPN have not been separately verified.

- [Quantumult X 设置 VPN 冷启动修复 RootHide `.deb`](pool/main/Quantumult%20X%20%E8%AE%BE%E7%BD%AE%20VPN%20%E5%86%B7%E5%90%AF%E5%8A%A8%E4%BF%AE%E5%A4%8D%20RootHide.deb)（版本 / Version `0.1.0`）

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
