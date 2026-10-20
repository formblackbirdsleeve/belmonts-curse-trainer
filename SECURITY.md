# Security Policy

## Scope

`belmonts-curse-trainer` is an offline single-player trainer for *Castlevania: Belmont's Curse*. It reads and writes process memory of a locally running `BelmontsCurse.exe` (or `BelmontsCurse-Win64-Shipping.exe` on GOG).

## What we do NOT do

- No network exfiltration of save data.
- No persistence outside `%APPDATA%/BelmontsCurseTrainer/`.
- No kernel-mode components, no boot-time drivers.
- No anti-cheat tampering. If you launch the game through a protected client, the trainer will refuse to attach.

## Reporting a vulnerability

DM a maintainer on the community Discord or open a private security advisory on GitHub. Please include:

- Trainer version (`--version`)
- Game build / Steam appid
- Reproduction steps

We aim to respond within 5 business days.

## Supported versions

| Trainer | Game build | Status |
|---------|-----------|--------|
| 0.9.x   | 1.04.xxxx | Supported |
| 0.8.x   | 1.03.xxxx | Security fixes only |