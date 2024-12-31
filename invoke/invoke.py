import os
import uuid
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from azure.ai.ml import MLClient, Input, Output

load_dotenv()

endpoint_name = "cv-batch-endpoint"
input_data_uri = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"

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

    # Define the input data
    input_data = Input(
        type="uri_folder",  # Adjusted to uri_folder since component expects a folder
        path="https://mldummyquaoutputssta.blob.core.windows.net/cv-outputs",  # Directory containing your data
    )

    # Specify the output location
    output_data = Output(
        type="uri_folder",
        path="azureml://datastores/workspaceblobstore/paths/output_path/"
    )

    job = ml_client.batch_endpoints.invoke(
        endpoint_name=endpoint_name,
        inputs={'input_dir': input_data},
        outputs={'output_dir': output_data},  # Providing the output mapping
        job_name=job_name
    )

    print(f"Batch job '{job.name}' submitted successfully!")
    print("Monitor the job in the Azure ML Studio portal.")

if __name__ == "__main__":
    invoke_batch_endpoint()