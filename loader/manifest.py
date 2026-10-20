"""Optional manifest reader — plugins may ship manifest.toml alongside their .py."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PluginManifest:
    name: str
    version: str
    author: str
    compatible_game: str


def read_manifest(folder: Path) -> PluginManifest | None:
    mf = folder / "manifest.toml"
    if not mf.exists():
        return None
    data = tomllib.loads(mf.read_text(encoding="utf-8"))
    return PluginManifest(
        name=data["name"],
        version=data["version"],
        author=data.get("author", "unknown"),
        compatible_game=data.get("game", "1.04.x"),
    )