"""Entry point for belmonts-curse-trainer."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from core.host import TrainerHost
from core.attach import attach_to_game
from utils.logging_setup import setup_logging


def main() -> int:
    parser = argparse.ArgumentParser(prog="belmonts-curse-trainer")
    parser.add_argument("--headless", action="store_true", help="Run without overlay GUI")
    parser.add_argument("--profile", default="default", help="Profile name under profiles/")
    parser.add_argument("--version", action="version", version="0.9.3")
    args = parser.parse_args()

    setup_logging(Path("logs") / "trainer.log")

    proc = attach_to_game()
    if proc is None:
        print("[!] BelmontsCurse.exe not found. Start the game first.", file=sys.stderr)
        return 2

    host = TrainerHost(proc, profile=args.profile)
    host.load_plugins("plugins")
    if args.headless:
        host.run_headless()
    else:
        host.run_gui()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())