# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an educational repository for the **Claude Code Crash Course** — a hands-on learning platform structured around Git branches. Each `project/*` branch teaches a specific Claude Code feature through chronologically ordered commits.

## Branch Structure

Each topic lives in its own `project/*` branch. To explore a topic:

```bash
git checkout project/<topic-name>
git log --oneline --reverse  # See the step-by-step commits
```

Available branches:
- `project/custom-commands` — Custom slash commands (`.claude/commands/`)
- `project/mcp` — MCP Integration with Context7
- `project/context-engineering-mcp` — Task-specific MCP configs using `--mcp-config` flag
- `project/subagents` — Specialized subagents
- `project/hooks-notifications` — Hook system with sound notifications (Python + pygame)
- `project/hookhub` — Next.js web app for hook discovery

## GitHub Actions Workflows

Both workflows require the `CLAUDE_CODE_OAUTH_TOKEN` secret:

- **`claude.yml`** — PR Assistant: triggers when `@claude` is mentioned in issues, PR comments, or reviews
- **`claude-code-review.yml`** — Auto-reviews all new/updated PRs using the `code-review` plugin from the Anthropic plugin marketplace

## Claude Code Local Configuration

`.claude/settings.local.json` grants these permissions by default:
- `Bash(git:*)`, `Bash(ls:*)`, `Bash(git ls-tree:*)`
- MCP servers: `context7` (documentation lookup via https://mcp.context7.com/mcp)

## Project-Specific Notes (per branch)

When working on project branches, each has its own stack:

- **hooks-notifications**: Python 3.11+, uses `uv` — run with `uv run play_sound.py`
- **context-engineering-mcp**: FastMCP server — run with `uv run verbose_mcp_server.py`; use `claude --mcp-config .mcp.json.tavily` to load task-specific MCP configs
- **hookhub**: Next.js 15, React 19, TypeScript, Tailwind CSS — standard `npm run dev`

## Contributing

New topics: create a `project/<feature-name>` branch with commits representing step-by-step learning units.
