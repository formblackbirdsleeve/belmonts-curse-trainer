"""Locate and attach to the BelmontsCurse process."""
from __future__ import annotations

from dataclasses import dataclass

import pymem
import pymem.exception
import psutil

PROCESS_NAMES = ("BelmontsCurse.exe", "BelmontsCurse-Win64-Shipping.exe")


@dataclass
class GameProcess:
    handle: pymem.Pymem
    pid: int
    name: str

    def is_alive(self) -> bool:
        try:
            psutil.Process(self.pid)
            return True
        except psutil.NoSuchProcess:
            return False


def attach_to_game() -> GameProcess | None:
    for name in PROCESS_NAMES:
        try:
            pm = pymem.Pymem(name)
            return GameProcess(handle=pm, pid=pm.process_id, name=name)
        except pymem.exception.ProcessNotFound:
            continue
    return None