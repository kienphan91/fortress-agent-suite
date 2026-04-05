# Fortress Agent Suite

**Fortress** là bộ công cụ tối ưu cho các OpenClaw agent trong môi trường production, cung cấp khả năng tự phục hồi (self-healing), giám sát hệ thống và bảo mật chủ động.

## ⚠️ Security & Privilege Warning
**IMPORTANT**: This suite operates with high privileges. It requires access to:
- `/root/.openclaw/` (configuration, workspace, secrets).
- Ability to modify `crontab` and execute system commands (`openclaw gateway restart`, `git`, `pip`).
- Network access to ClawHub and GitHub APIs to self-update or install new skills.
**Use only in trusted environments.**

## Features
- 🛡️ **Self-Healing**: Automatic gateway recovery.
- 🩺 **Health Monitoring**: Disk/RAM watchdog.
- ⚙️ **Automated Maintenance**: Auto-cron enforcement and workspace Git-sync.
- 🤖 **Model Manager**: Automated LLM provider configuration.

---

# Fortress Agent Suite (English)

**Fortress** is a production-grade suite for OpenClaw agents, providing self-healing, system monitoring, and proactive security hardening.

## ⚠️ Security & Privilege Warning
**IMPORTANT**: This suite requires elevated system privileges:
- Direct access to `/root/.openclaw/` (config, workspace, and secrets).
- Permission to modify `crontab`, restart system services, and execute shell commands (`git`, `pip`).
- Network access for autonomous skill installation and API interaction.
**Please deploy in trusted environments only.**

## Key Features
- 🛡️ **Self-Healing**: Detects gateway downtime, restores from latest backup, and restarts.
- 🩺 **Health Monitoring**: Automated disk/RAM watchdogs and log rotation.
- ⚙️ **Automated Maintenance**: Ensures critical cron jobs remain active and performs automated Git-sync for workspace integrity.
- 🤖 **Model Manager**: Autonomous management of LLM providers and model configuration for 9Router.

## Installation
1. Clone the repository into your OpenClaw `skills/` directory.
2. Install dependencies: `pip install psutil`.
3. Apply the `crontab_template.txt` to your system crontab.
4. Set up your API tokens in `/root/.openclaw/secrets/`.

## License
MIT
