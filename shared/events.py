"""Tiny pub/sub used by plugins to signal state changes to the overlay."""
from __future__ import annotations

from collections import defaultdict
from typing import Callable

Handler = Callable[..., None]


class EventBus:
    def __init__(self) -> None:
        self._subs: dict[str, list[Handler]] = defaultdict(list)

    def on(self, topic: str, fn: Handler) -> None:
        self._subs[topic].append(fn)

    def emit(self, topic: str, **payload) -> None:
        for fn in self._subs.get(topic, []):
            fn(**payload)


bus = EventBus()