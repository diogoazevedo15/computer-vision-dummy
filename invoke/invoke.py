import os
import uuid
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from azure.ai.ml import MLClient, Input

load_dotenv()

endpoint_name = "cv-batch-endpoint"
input_data_url = "azureml://subscriptions/2a4f4e29-3789-4e47-867d-62a6eb17950b/resourcegroups/ml-dummy-qua-rg/workspaces/ml-dummy-qua-mlws/datastores/workspaceblobstore/paths/LocalUpload/"
datastore_path = "azureml://subscriptions/2a4f4e29-3789-4e47-867d-62a6eb17950b/resourcegroups/ml-dummy-qua-rg/workspaces/ml-dummy-qua-mlws/datastores/workspaceblobstore/paths/LocalUpload/"

credential = ClientSecretCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    client_id=os.getenv("AZURE_CLIENT_ID"),
    client_secret=os.getenv("AZURE_CLIENT_SECRET")
)

ml_client = MLClient(
    credential=credential,
    subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
    resource_group_name=os.getenv("AZURE_RESOURCE_GROUP"),
    workspace_name=os.getenv("AZURE_WORKSPACE_NAME"),
)

def invoke_batch_endpoint():
    job_name = f"batch-job-{uuid.uuid4()}"
    print(f"Submitting batch job '{job_name}' to endpoint '{endpoint_name}'...")

    # Define inputs
    inputs = {
        'input_url': Input(type="uri_folder", path=datastore_path),  # String input
        'output_url': Input(type="uri_folder", path=datastore_path)  # Datastore input
    }

    job = ml_client.batch_endpoints.invoke(
        endpoint_name=endpoint_name,
        inputs=inputs,  # Pass the inputs dictionary
        job_name=job_name
    )

    print(f"Batch job '{job.name}' submitted successfully!")
    print("Monitor the job in the Azure ML Studio portal.")

if __name__ == "__main__":
    invoke_batch_endpoint()
