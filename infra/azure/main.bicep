targetScope = 'resourceGroup'

@description('Deployment region for Azure resources.')
param location string = resourceGroup().location

@description('Stable workload name used by future resources.')
@minLength(2)
param workloadName string = 'az-tutor'

@description('Tags applied to future Azure resources.')
param tags object = {}

output deploymentContext object = {
  location: location
  workloadName: workloadName
  tags: tags
}
