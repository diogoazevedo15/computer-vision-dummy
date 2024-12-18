import os
import uuid
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.ai.ml import MLClient

# Load environment variables from .env
load_dotenv()

# Configuration
endpoint_name = "hello-batch-endpoint"  # Replace with your endpoint name
input_data_uri = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"  # Sample input data

# Authenticate with Azure ML using ClientSecretCredential for explicit credentials
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

    # Invoke the batch endpoint with the correct input format
    job = ml_client.batch_endpoints.invoke(
        endpoint_name=endpoint_name,
        inputs={"input_data": input_data_uri},  # Pass inputs as a dictionary
        job_name=job_name
    )

    print(f"Batch job '{job.name}' submitted successfully!")
    print("Monitor the job in the Azure ML Studio portal.")

if __name__ == "__main__":
    invoke_batch_endpoint()
