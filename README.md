# AZ Tutor

An agent-ready Python foundation for a tutoring system intended to run on Azure and
Azure AI Foundry. The repository deliberately starts with contracts and deployment
boundaries instead of guessing product behavior or cloud topology.

## Quick start

Prerequisites: [uv](https://docs.astral.sh/uv/) and Python 3.12.

```bash
uv sync --all-groups
uv run az-tutor
uv run pytest
```

Copy `.env.example` to `.env` for local cloud configuration. Do not commit secrets.

## Layout

- `src/az_tutor/agents/` — provider-independent agent contracts and registry.
- `src/az_tutor/integrations/` — future Azure and Azure AI Foundry adapters.
- `infra/azure/` — shared Azure Bicep entry point.
- `infra/foundry/` — Azure AI Foundry Bicep entry point.
- `tests/` — fast unit tests.
- `AGENTS.md` — working agreement for coding agents.

## Quality gate

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest
```

Cloud templates currently expose validated deployment inputs only. Concrete resources,
identity, networking, and model deployments should be added once those decisions are made.
