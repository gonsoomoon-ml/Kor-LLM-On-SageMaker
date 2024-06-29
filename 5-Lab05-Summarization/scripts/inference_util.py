import boto3
import json
from io import StringIO
import sys
import textwrap

def print_json(data):
    print(json.dumps(data, indent = 4))


def create_messages_parameters(system_prompt, user_prompt, verbose=False):
  # Prompt to generate
  messages=[
      { "role": "system", "content": f"{system_prompt}" },
      { "role": "user", "content":  user_prompt}
    ]

  # Generation arguments
  parameters = {
      "model": "meta-llama-3-fine-tuned", # placeholder, needed
      "top_p": 0.6,
      "temperature": 0.0,
      "max_tokens": 512,
      "stop": ["<|eot_id|>"],
  }

  if verbose:
    print("messages:")
    print_json(messages)
    print("parameters:")
    print_json(parameters)

  return messages, parameters


def create_boto3_request_body(system_prompt, user_prompt):
    request_body = {
        "messages": [
            {"role": "system", "content": f"{system_prompt}"},
            {"role": "user", "content": f"{user_prompt}"},
        ],
        "model": "meta-llama-3-fine-tuned",
        "parameters": {"max_tokens":256,
                    "top_p": 0.6,
                    "temperature": 0.0,
                    "max_tokens": 512,
                    "stop": ["<|eot_id|>"]}
    }

    return request_body    


def invoke_endpoint_sagemaker(endpoint_name, pay_load):

    # Set up the SageMaker runtime client
    sagemaker_runtime = boto3.client('sagemaker-runtime')
    # Set the endpoint name
    endpoint_name = endpoint_name


    # Invoke the endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',
        Body=json.dumps(pay_load)
    )
    # Get the response from the endpoint
    result = response['Body'].read().decode('utf-8')

    return result




def print_ww(*args, width: int = 100, **kwargs):
    """Like print(), but wraps output to `width` characters (default 100)"""
    buffer = StringIO()
    try:
        _stdout = sys.stdout
        sys.stdout = buffer
        print(*args, **kwargs)
        output = buffer.getvalue()
    finally:
        sys.stdout = _stdout
    for line in output.splitlines():
        print("\n".join(textwrap.wrap(line, width=width)))
