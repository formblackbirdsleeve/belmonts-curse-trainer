"""Snapshot of trainer state, mutated by plugins and consumed by the overlay."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PlayerStats:
    hp: int = 100
    max_hp: int = 100
    mp: int = 50
    max_mp: int = 50
    hearts: int = 0
    gold: int = 0


@dataclass
class TrainerState:
    profile: str = "default"
    player: PlayerStats = field(default_factory=PlayerStats)
    godmode: bool = False
    infinite_mp: bool = False
    damage_multiplier: float = 1.0
    current_room: str = ""
    attached: bool = True
    notes: dict[str, str] = field(default_factory=dict)
</｜｜DSML｜｜ parameter>
</｜｜DSML｜｜ invoke>
</｜｜DSML｜｜ calls>