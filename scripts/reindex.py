#!/usr/bin/env python3
"""Generate Sileo/APT indexes for .deb files under pool/."""
from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import gzip
import hashlib
import pathlib
import subprocess

DEFAULT_BASE_URL = "https://cdn.jsdelivr.net/gh/komakizhu/komaki-packages@main"
SOURCE_NAME = "Komaki Zhu"
SOURCE_DESCRIPTION = "Komaki Zhu 越狱插件源 / Komaki Zhu jailbreak package source"
PACKAGE_METADATA_OVERRIDES = {
    "app.local.nfcoma.applepay-alert-guard": {
        "name": "NFComa Apple Pay Alert Guard / NFComa Apple Pay 警告守护",
        "description": (
            "抑制 Apple Pay 不可用提醒并提供注入诊断 / "
            "Suppresses Apple Pay unavailable alerts and provides injection diagnostics.\n"
            " 中文：自动确认 SpringBoard 与 NFComa 中匹配的 Apple Pay 不可用提醒，并提供运行时注入诊断。"
            "此插件不会恢复 Apple Pay 或 NFC 服务。\n"
            " English: Automatically acknowledges matching Apple Pay unavailable alerts in SpringBoard and NFComa, "
            "with runtime injection diagnostics. It does not restore Apple Pay or NFC service."
        ),
    },
}


def parse_control(data: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for line in data.splitlines():
        if line[:1].isspace() and current:
            fields[current] += "\n" + line
        elif ":" in line:
            key, value = line.split(":", 1)
            current = key.strip().lower()
            fields[current] = value.strip()
    return fields


def checksum(data: bytes, algorithm: str) -> str:
    return hashlib.new(algorithm, data).hexdigest()


def field_lines(name: str, value: str) -> list[str]:
    lines = value.splitlines() or [""]
    return [f"{name}: {lines[0]}", *lines[1:]]


def render_packages(
    package_entries: list[tuple[str, dict[str, str]]],
    order: list[tuple[str, str]],
) -> bytes:
    paragraphs: list[str] = []
    for _, fields in sorted(package_entries, key=lambda item: (item[0], item[1]["version"])):
        lines: list[str] = []
        for key, label in order:
            if fields.get(key):
                lines.extend(field_lines(label, fields[key]))
        paragraphs.append("\n".join(lines))
    return ("\n\n".join(paragraphs) + "\n").encode("utf-8")


def write_release(
    path: pathlib.Path,
    index_paths: list[pathlib.Path],
    architectures: list[str],
    date: str,
) -> None:
    release = [
        f"Origin: {SOURCE_NAME}", f"Label: {SOURCE_NAME}", "Suite: stable", "Codename: stable", "Version: 1.0",
        "Architectures: " + " ".join(architectures), "Components: main",
        "Description: " + SOURCE_DESCRIPTION, "Date: " + date,
    ]
    for label, algorithm in (("MD5Sum", "md5"), ("SHA1", "sha1"), ("SHA256", "sha256")):
        release.append(label + ":")
        for index in sorted(index_paths):
            relative = index.relative_to(path.parent).as_posix()
            data = index.read_bytes()
            release.append(f" {checksum(data, algorithm)} {len(data):16d} {relative}")
    path.write_text("\n".join(release) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    args = parser.parse_args()
    root = args.root.resolve()
    base_url = args.base_url.rstrip("/")
    packages_by_arch: dict[str, list[tuple[str, dict[str, str]]]] = {}

    for deb in sorted((root / "pool").rglob("*.deb")):
        raw = subprocess.check_output(["dpkg-deb", "-f", str(deb)], text=True)
        fields = parse_control(raw)
        fields.update(PACKAGE_METADATA_OVERRIDES.get(fields.get("package", ""), {}))
        for required in ("package", "version", "architecture", "description"):
            if not fields.get(required):
                raise SystemExit(f"{deb}: missing {required} field")
        data = deb.read_bytes()
        fields["filename"] = deb.relative_to(root).as_posix()
        fields["size"] = str(len(data))
        fields["md5sum"] = checksum(data, "md5")
        fields["sha1"] = checksum(data, "sha1")
        fields["sha256"] = checksum(data, "sha256")
        icon = root / "icons" / f"{fields['package']}.png"
        if icon.is_file():
            fields["icon"] = f"{base_url}/icons/{icon.name}"
        elif not fields.get("icon", "").startswith(("http://", "https://")):
            fields.pop("icon", None)
        packages_by_arch.setdefault(fields["architecture"], []).append((fields["package"], fields))

    if not packages_by_arch:
        raise SystemExit("pool/ contains no .deb packages")

    order = [
        ("package", "Package"), ("version", "Version"), ("architecture", "Architecture"),
        ("name", "Name"), ("description", "Description"), ("maintainer", "Maintainer"),
        ("author", "Author"), ("section", "Section"), ("depends", "Depends"),
        ("installed-size", "Installed-Size"), ("icon", "Icon"), ("filename", "Filename"),
        ("size", "Size"), ("md5sum", "MD5sum"), ("sha1", "SHA1"), ("sha256", "SHA256"),
    ]
    architectures = sorted(packages_by_arch)
    hierarchical_index_paths: list[pathlib.Path] = []
    for arch, package_entries in sorted(packages_by_arch.items()):
        folder = root / "dists/stable/main" / f"binary-{arch}"
        folder.mkdir(parents=True, exist_ok=True)
        index_data = render_packages(package_entries, order)
        index = folder / "Packages"
        index.write_bytes(index_data)
        (folder / "Packages.gz").write_bytes(gzip.compress(index_data, mtime=0))
        hierarchical_index_paths.extend((index, folder / "Packages.gz"))

    release_date = email.utils.format_datetime(dt.datetime.now(dt.timezone.utc), usegmt=True)
    write_release(root / "dists/stable/Release", hierarchical_index_paths, architectures, release_date)

    # Sileo's simple “Add Source” flow treats the supplied URL as a flat APT root
    # and requests <URL>/Release and <URL>/Packages. Keep this alongside the
    # conventional dists/stable layout for clients that configure a suite.
    all_entries = [entry for entries in packages_by_arch.values() for entry in entries]
    flat_data = render_packages(all_entries, order)
    flat_index = root / "Packages"
    flat_gzip = root / "Packages.gz"
    flat_index.write_bytes(flat_data)
    flat_gzip.write_bytes(gzip.compress(flat_data, mtime=0))
    write_release(root / "Release", [flat_index, flat_gzip], architectures, release_date)


if __name__ == "__main__":
    main()
