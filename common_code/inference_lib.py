
def descirbe_endpoint(endpoint_name):
    import boto3
    import time
    
    sm_client = boto3.client("sagemaker")


    while(True):
        response = sm_client.describe_endpoint(
            EndpointName= endpoint_name
        )    
        status = response['EndpointStatus']
        if status == 'Creating':
            print("Endpoint is ", status)
            time.sleep(60)
        else:
            print("Endpoint is ", status)
            break


def invoke_inference(endpoint_name, prompt):
    import boto3
    client = boto3.client("sagemaker-runtime")
    
    content_type = "text/plain"
    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType=content_type, Body=prompt
    )
    #print(response["Body"].read())
    res = response["Body"].read().decode()
    print (eval(res)[0]['generated_text'])
            