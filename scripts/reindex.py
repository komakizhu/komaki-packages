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

    index_paths: list[pathlib.Path] = []
    order = [
        ("package", "Package"), ("version", "Version"), ("architecture", "Architecture"),
        ("name", "Name"), ("description", "Description"), ("maintainer", "Maintainer"),
        ("author", "Author"), ("section", "Section"), ("depends", "Depends"),
        ("installed-size", "Installed-Size"), ("icon", "Icon"), ("filename", "Filename"),
        ("size", "Size"), ("md5sum", "MD5sum"), ("sha1", "SHA1"), ("sha256", "SHA256"),
    ]
    for arch, package_entries in sorted(packages_by_arch.items()):
        folder = root / "dists/stable/main" / f"binary-{arch}"
        folder.mkdir(parents=True, exist_ok=True)
        paragraphs: list[str] = []
        for _, fields in sorted(package_entries, key=lambda item: (item[0], item[1]["version"])):
            lines: list[str] = []
            for key, label in order:
                if fields.get(key):
                    lines.extend(field_lines(label, fields[key]))
            paragraphs.append("\n".join(lines))
        index_data = ("\n\n".join(paragraphs) + "\n").encode("utf-8")
        index = folder / "Packages"
        index.write_bytes(index_data)
        (folder / "Packages.gz").write_bytes(gzip.compress(index_data, mtime=0))
        index_paths.extend((index, folder / "Packages.gz"))

    release = [
        "Origin: Komaki", "Label: Komaki", "Suite: stable", "Codename: stable", "Version: 1.0",
        "Architectures: " + " ".join(sorted(packages_by_arch)), "Components: main",
        "Description: Komaki jailbreak package source",
        "Date: " + email.utils.format_datetime(dt.datetime.now(dt.timezone.utc), usegmt=True),
    ]
    release_root = root / "dists/stable"
    for label, algorithm in (("MD5Sum", "md5"), ("SHA1", "sha1"), ("SHA256", "sha256")):
        release.append(label + ":")
        for index in sorted(index_paths):
            relative = index.relative_to(release_root).as_posix()
            data = index.read_bytes()
            release.append(f" {checksum(data, algorithm)} {len(data):16d} {relative}")
    (release_root / "Release").write_text("\n".join(release) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
