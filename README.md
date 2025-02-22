# Azure ML Batch Endpoint Deployment Demo

This repository demonstrates how to set up a simple Azure Machine Learning (Azure ML) batch endpoint and deployment using GitHub Actions for CI/CD. The code and configuration here provide a basic skeleton you can customize for more complex use cases.

## Prerequisites

1. **Azure Service Principal (Service Account)**:  
   To automate resource creation and updates, you need a service principal with the appropriate permissions (e.g., `Contributor` role on the workspace scope).  
   This allows GitHub Actions to authenticate and interact with your Azure ML workspace without exposing user credentials.

2. **GitHub Secrets**:  
   Before running the GitHub Actions workflow, set the following repository secrets in GitHub:
   - **AZURE_CLIENT_ID**: The `appId` of your service principal.
   - **AZURE_CLIENT_SECRET**: The `password` of your service principal.
   - **AZURE_TENANT_ID**: The `tenant` where your Azure resources reside.
   - **AZURE_SUBSCRIPTION_ID**: The subscription ID where your Azure ML workspace is located.
   - **AZURE_RESOURCE_GROUP**: The resource group containing your Azure ML workspace.
   - **AZURE_WORKSPACE_NAME**: The name of your Azure ML workspace.

   These secrets allow the GitHub Actions workflow to log in, set the subscription, and apply changes in your Azure environment.

## Repository Structure

```
├── .github
│ └── workflows
│ └── azureml-deploy.yml
├── tests
│ ├── repo_tests
│ ├── endpoint
├── deployment
│ ├── batch_deployment.yaml
│ ├── environments
│ │ ├── env_validate.yaml
│ │ └── env_inference.yaml
│ ├── components
│ │ ├── config_validate.yaml
│ │ └── config_inference.yaml
│ │ └── pipeline.yaml
└── src
├── components
│ ├── cv_model_validate.py
│ └── cv_model_inference.py
```

### File Descriptions


### File Descriptions

**`.github/workflows/azureml-deploy.yml`**  
This GitHub Actions workflow is triggered when changes are pushed to the `qua` branch. It:  
- Installs the Azure CLI and Azure ML CLI extension.  
- Authenticates using the service principal credentials stored as GitHub Secrets.  
- Sets the default subscription, resource group, and workspace.  
- Creates or updates the Azure ML environments, components, pipeline, batch endpoint, and batch deployment.  
- Sets the default deployment for the endpoint.

**`deployment/endpoint.yaml`**  
Defines the Azure ML batch endpoint resource. It specifies the endpoint’s name and authentication mode. The endpoint is a logical concept that provides an entry point for submitting batch inference requests.

**`deployment/batch_deployment.yaml`**  
Defines the batch deployment associated with the endpoint. It includes details such as:  
- The compute target (where the batch job runs).  
- The environment (runtime environment with libraries and dependencies).  
- The component to be used for the deployment.

**`deployment/environments/env_validate.yaml`** and **`deployment/environments/env_inference.yaml`**  
Specify the environments for running the batch inference and validation. These include the Docker base image, Python version, and necessary packages (`azureml-defaults`, etc.). Once created, these environments are referenced in the components.

**`deployment/components/config_validate.yaml`** and **`deployment/components/config_inference.yaml`**  
Define the command components for model validation and inference. They specify the inputs, outputs, environment, and command to be executed.

**`deployment/pipeline.yaml`**  
Defines the pipeline that orchestrates the validation and inference steps. It specifies the inputs, outputs, and the sequence of jobs to be executed.

## GitHub Actions Workflow Overview

The `azureml-deploy.yml` workflow automates the entire deployment process:  
1. **Checkout and Setup**: Pulls the repository code and installs Azure CLI tools.  
2. **Authentication**: Uses the service principal credentials provided as GitHub Secrets to authenticate with Azure.  
3. **Configuration**: Sets the default subscription, resource group, and workspace context.  
4. **Environment & Endpoint Creation**:  
   - Creates/updates the environments defined by `env_validate.yaml` and `env_inference.yaml`.  
   - Creates/updates the components defined by `config_validate.yaml` and `config_inference.yaml`.  
   - Creates/updates the pipeline defined by `pipeline.yaml`.  
   - Creates/updates the batch endpoint and deployment defined by `endpoint.yaml` and `batch_deployment.yaml`.  
   - Sets the default deployment for the endpoint.

This workflow ensures that whenever code is merged into the `qua` branch, the latest configurations and code changes are automatically deployed to your Azure ML workspace.

## Next Steps

1. **Caching the CLI Tools (DONE ✅)**:   

   Consider caching the Azure CLI and Azure ML CLI extension installations to speed up the CI/CD process. This can be done using GitHub Actions cache keys and steps to reduce build time. 

3. **Labels and Tags**:   

   Explore using Git tags, labels, or branches to segment your CI/CD pipeline and manage different deployment environments or versions.
