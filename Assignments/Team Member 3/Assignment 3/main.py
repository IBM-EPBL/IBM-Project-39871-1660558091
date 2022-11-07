import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = "<endpoint>" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "<api-key>" # eg "JjXw2wMctrVMD1f3-H4ECpnv0zgEb2JKvxh877ZoIwZo"
COS_INSTANCE_CRN = "<service-instance-id>" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/025726c13d1a43a590f1823d2212b7fa:62370f56-6d45-4ff6-928a-ff6a6eb42aa1::"

# Create resource
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)
def get_bucket_contents(jrb-bucket04):
    print("Retrieving bucket contents from: {0}".format(jrb-bucket04))
    try:
        files = cos.Bucket(jrb-bucket04).objects.all()
        for file in files:
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))