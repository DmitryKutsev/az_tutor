from az_tutor.config import AzureSettings


def test_settings_have_safe_defaults(monkeypatch) -> None:
    for key in (
        "AZURE_SUBSCRIPTION_ID",
        "AZURE_TENANT_ID",
        "AZURE_RESOURCE_GROUP",
        "AZURE_LOCATION",
        "AZURE_AI_FOUNDRY_PROJECT_ENDPOINT",
    ):
        monkeypatch.delenv(key, raising=False)

    settings = AzureSettings.from_env()

    assert settings.location == "westeurope"
    assert settings.foundry_project_endpoint is None
