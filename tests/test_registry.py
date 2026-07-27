from dataclasses import dataclass

import pytest

from az_tutor.agents import AgentRequest, AgentResponse, AgentRegistry


@dataclass
class StubAgent:
    name: str = "stub"

    async def run(self, request: AgentRequest) -> AgentResponse:
        return AgentResponse(message=request.message)


def test_registry_registers_and_resolves_agent() -> None:
    registry = AgentRegistry()
    agent = StubAgent()

    registry.register(agent)

    assert registry.get("stub") is agent
    assert list(registry) == [agent]


def test_registry_rejects_duplicate_names() -> None:
    registry = AgentRegistry()
    registry.register(StubAgent())

    with pytest.raises(ValueError, match="already registered"):
        registry.register(StubAgent())
