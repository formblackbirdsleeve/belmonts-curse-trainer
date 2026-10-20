"""In-memory plugin registry with enable/disable support."""
from __future__ import annotations

from typing import Iterable

from shared.contracts import TrainerPlugin


class PluginRegistry:
    def __init__(self) -> None:
        self._plugins: dict[str, TrainerPlugin] = {}
        self._disabled: set[str] = set()

    def register(self, plugin: TrainerPlugin) -> None:
        if plugin.name in self._plugins:
            raise ValueError(f"plugin already registered: {plugin.name}")
        self._plugins[plugin.name] = plugin

    def disable(self, name: str) -> None:
        self._disabled.add(name)

    def enable(self, name: str) -> None:
        self._disabled.discard(name)

    def active(self) -> Iterable[TrainerPlugin]:
        return (p for n, p in self._plugins.items() if n not in self._disabled)

    def all(self) -> list[TrainerPlugin]:
        return list(self._plugins.values())