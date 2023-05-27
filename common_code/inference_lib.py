import boto3
import time
import json

    
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
    KoAlpaca 프롬프트를 제공하여 엔드포인트 호출
    '''
    client = boto3.client("sagemaker-runtime")
    
    content_type = "text/plain"
    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType=content_type, Body=prompt
    )
    #print(response["Body"].read())
    res = response["Body"].read().decode()
    print (eval(res)[0]['generated_text'])

            
def query_endpoint_with_json_payload(encoded_json, endpoint_name, content_type="application/json"):
    client = boto3.client("runtime.sagemaker")
    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType=content_type, Body=encoded_json
    )
    return response
        
        
def query_endpoint_with_json_payload(encoded_json, endpoint_name, content_type="application/json"):
    client = boto3.client("runtime.sagemaker")
    response = client.invoke_endpoint(
        EndpointName=endpoint_name, ContentType=content_type, Body=encoded_json
    )
    return response


def parse_response_model_KoAlpaca(query_response):
    model_predictions = json.loads(query_response["Body"].read())
#    generated_text = model_predictions["generated_texts"]
#    return generated_text
    return model_predictions


def parse_response_multiple_texts_bloomz(query_response):
    generated_text = []
    model_predictions = json.loads(query_response["Body"].read())
    for x in model_predictions[0]:
        generated_text.append(x["generated_text"])
    return generated_text        