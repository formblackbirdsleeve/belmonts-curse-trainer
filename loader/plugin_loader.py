"""Discover plugin modules under a folder and register them with the host."""
from __future__ import annotations

import importlib.util
import inspect
from pathlib import Path
from typing import TYPE_CHECKING

from shared.contracts import BasePlugin, TrainerPlugin
from utils.logging_setup import get_logger

if TYPE_CHECKING:
    from core.host import TrainerHost

log = get_logger(__name__)


class PluginLoader:
    def __init__(self, host: "TrainerHost") -> None:
        self.host = host

    def discover_and_load(self, folder: str) -> list[str]:
        root = Path(folder)
        loaded: list[str] = []
        if not root.exists():
            log.warning("plugin folder missing: %s", root)
            return loaded

        for path in sorted(root.glob("*.py")):
            if path.name.startswith("_"):
                continue
            plugin = self._load_one(path)
            if plugin is None:
                continue
            plugin.on_load(self.host)
            self.host.registry.register(plugin)
            loaded.append(plugin.name)
        return loaded

    def _load_one(self, path: Path) -> TrainerPlugin | None:
        spec = importlib.util.spec_from_file_location(f"bc_plugins.{path.stem}", path)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:
            log.exception("failed to import %s: %s", path, exc)
            return None

        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj is BasePlugin or not issubclass(obj, BasePlugin):
                continue
            if obj.__module__ != module.__name__:
                continue
            return obj()
        return None