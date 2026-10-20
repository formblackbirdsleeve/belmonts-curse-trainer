# Contributing to belmonts-curse-trainer

Thanks for wanting to help. This is a community trainer for *Castlevania: Belmont's Curse* (2025 release, Steam / GOG).

## Ground rules

- **Single-player only.** The trainer is for the offline campaign and Bloodmoon Trials. Do not open PRs that target the online leaderboard or co-op sessions.
- **No kernel drivers.** Userspace only. Anything that requires a signed driver will be rejected.
- **Signature rescan every patch.** When Konami ships a patch, addresses move. Bump `models/offsets.py` and update `CHANGELOG` in the release notes.

## Workflow

1. Fork, branch from `main` (`feat/<plugin>-<short-desc>`).
2. Plugins live under `plugins/` and register via `loader/plugin_loader.py`.
3. Run `pytest tests/` before opening the PR.
4. Keep plugin modules under ~200 lines; if it grows, split a service out into `services/`.

## Code style

- `ruff` + `black` defaults.
- Type hints on public plugin entrypoints (`def __init__(self, ctx: PluginContext)`).
- No prints in plugin code — use `ctx.log`.

## Reporting broken offsets

Open an issue titled `[OFFSETS] <game version> <plugin>` with the log snippet from `logs/trainer.log`. Do not paste memory dumps.