# Agent working agreement

## Mission

Keep AZ Tutor easy for humans and coding agents to understand, change, and verify.

## Source of truth

- Python package: `src/az_tutor/`
- Tests: `tests/`
- Azure infrastructure: `infra/azure/`
- Azure AI Foundry infrastructure: `infra/foundry/`
- Tooling and dependencies: `pyproject.toml`, managed only with `uv`

## Working loop

1. Read this file and the nearest README before editing.
2. Keep changes small and avoid guessing cloud resources or credentials.
3. Add or update tests with behavior changes.
4. Run `uv run ruff check .`, `uv run ruff format --check .`,
   `uv run mypy`, and `uv run pytest`.
5. Update documentation when contracts or setup change.

## Architecture boundaries

- Domain and agent contracts must not import Azure SDKs.
- Provider-specific adapters belong under `src/az_tutor/integrations/`.
- Infrastructure code must remain separate from application code.
- Secrets are environment variables or managed identities; never commit them.
- Add SDKs only when a concrete adapter needs them.

## Definition of done

The change is typed, tested, formatted, documented, and contains no credentials or
environment-specific assumptions.
