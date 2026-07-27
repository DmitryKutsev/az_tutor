"""Environment-backed application configuration."""

from dataclasses import dataclass
from os import environ


@dataclass(frozen=True, slots=True)
class AzureSettings:
    """Azure values that are safe to pass through application composition."""

    subscription_id: str | None
    tenant_id: str | None
    resource_group: str | None
    location: str
    foundry_project_endpoint: str | None

    @classmethod
    def from_env(cls) -> "AzureSettings":
        return cls(
            subscription_id=environ.get("AZURE_SUBSCRIPTION_ID"),
            tenant_id=environ.get("AZURE_TENANT_ID"),
            resource_group=environ.get("AZURE_RESOURCE_GROUP"),
            location=environ.get("AZURE_LOCATION", "westeurope"),
            foundry_project_endpoint=environ.get("AZURE_AI_FOUNDRY_PROJECT_ENDPOINT"),
        )
