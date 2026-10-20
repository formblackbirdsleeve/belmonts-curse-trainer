"""Protocol + base class every plugin must implement."""
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from core.host import TrainerHost
    from models.state import TrainerState


@runtime_checkable
class TrainerPlugin(Protocol):
    name: str
    version: str

    def on_load(self, host: "TrainerHost") -> None: ...
    def on_tick(self, state: "TrainerState") -> None: ...
    def on_unload(self) -> None: ...


class BasePlugin:
    name = "unnamed"
    version = "0.0.0"

    def on_load(self, host: "TrainerHost") -> None:
        self.host = host

    def on_tick(self, state: "TrainerState") -> None:
        pass

    def on_unload(self) -> None:
        pass