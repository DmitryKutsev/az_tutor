"""Explicit agent composition registry."""

from collections.abc import Iterator

from az_tutor.agents.base import Agent


class AgentRegistry:
    """Stores agents by stable name and rejects ambiguous registration."""

    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def register(self, agent: Agent) -> None:
        if agent.name in self._agents:
            raise ValueError(f"Agent already registered: {agent.name}")
        self._agents[agent.name] = agent

    def get(self, name: str) -> Agent:
        try:
            return self._agents[name]
        except KeyError as error:
            raise KeyError(f"Unknown agent: {name}") from error

    def __iter__(self) -> Iterator[Agent]:
        return iter(self._agents.values())

    def __len__(self) -> int:
        return len(self._agents)
