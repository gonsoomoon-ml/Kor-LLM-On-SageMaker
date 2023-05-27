import boto3
import time

    
def descirbe_endpoint(endpoint_name):
    '''
    엔드폰인트 생성 유무를 확인. 생성 중이면 기다림.
    '''
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
    '''
    프롬프트를 제공하여 엔드포인트 호출
    '''
    client = boto3.client("sagemaker-runtime")
    
    content_type = "text/plain"
    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType=content_type, Body=prompt
    )
    #print(response["Body"].read())
    res = response["Body"].read().decode()
    print (eval(res)[0]['generated_text'])
            