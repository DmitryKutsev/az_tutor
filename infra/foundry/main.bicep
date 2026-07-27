targetScope = 'resourceGroup'

@description('Deployment region for Azure AI Foundry resources.')
param location string = resourceGroup().location

@description('Stable Azure AI Foundry project name.')
@minLength(2)
param projectName string = 'az-tutor'

@description('Tags applied to future Azure AI Foundry resources.')
param tags object = {}

output deploymentContext object = {
  location: location
  projectName: projectName
  tags: tags
}
