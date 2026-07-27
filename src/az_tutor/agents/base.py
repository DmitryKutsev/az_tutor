"""Provider-independent agent contracts."""

from dataclasses import dataclass, field
from typing import Protocol


@dataclass(frozen=True, slots=True)
class AgentRequest:
    """Input passed to an agent."""

    message: str
    context: dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class AgentResponse:
    """Result returned by an agent."""

    message: str
    metadata: dict[str, object] = field(default_factory=dict)


class Agent(Protocol):
    """Contract implemented by every AZ Tutor agent."""

    @property
    def name(self) -> str:
        """Return a stable agent identifier."""
        ...

    async def run(self, request: AgentRequest) -> AgentResponse:
        """Handle one request."""
        ...
