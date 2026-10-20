"""TrainerHost: owns process handle, plugin registry, and tick loop."""
from __future__ import annotations

import time
from typing import Any

import pymem

from core.attach import GameProcess
from core.registry import PluginRegistry
from loader.plugin_loader import PluginLoader
from models.state import TrainerState
from utils.logging_setup import get_logger

log = get_logger(__name__)


class TrainerHost:
    def __init__(self, proc: GameProcess, profile: str = "default") -> None:
        self.proc = proc
        self.profile = profile
        self.state = TrainerState(profile=profile)
        self.registry = PluginRegistry()
        self._loader = PluginLoader(self)

    def load_plugins(self, folder: str) -> None:
        loaded = self._loader.discover_and_load(folder)
        log.info("loaded %d plugins from %s", len(loaded), folder)

    def tick(self) -> None:
        for plugin in self.registry.active():
            try:
                plugin.on_tick(self.state)
            except Exception as exc:  # keep the loop alive
                log.exception("plugin %s crashed on tick: %s", plugin.name, exc)
                self.registry.disable(plugin.name)

    def run_headless(self) -> None:
        log.info("headless mode, profile=%s", self.profile)
        while self.proc.is_alive():
            self.tick()
            time.sleep(0.05)

    def run_gui(self) -> None:
        from ui.overlay import OverlayWindow
        overlay = OverlayWindow(self)
        overlay.exec_loop()

    @property
    def handle(self) -> pymem.Pymem:
        return self.proc.handle