"""Minimal local entry point."""

from az_tutor.agents.registry import AgentRegistry


def main() -> None:
    """Report the current skeleton state."""
    registry = AgentRegistry()
    print(f"AZ Tutor is ready; registered agents: {len(registry)}")


if __name__ == "__main__":
    main()
