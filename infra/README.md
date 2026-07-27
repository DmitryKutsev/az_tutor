# Infrastructure

Infrastructure is split by responsibility:

- `azure/`: shared Azure resource-group-level foundations.
- `foundry/`: Azure AI Foundry-specific resources and connections.

The templates intentionally declare only stable inputs today. Add resources after the
environment, security model, networking, naming, and deployment topology are agreed.

Validate locally with the Azure CLI when templates gain resources:

```bash
az bicep build --file infra/azure/main.bicep
az bicep build --file infra/foundry/main.bicep
```
