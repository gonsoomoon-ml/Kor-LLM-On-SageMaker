# Kor-LLM-On-SageMaker

아래와 같은 4개의 노트북과 3개의 한국어 LLM 및 1개의 한국어 임베딩 모델을 배포 해볼 수 있습니다.

## 1-Lab01-Deploy-LLM

- 1.Deploy-Kor-LLM-PythonSDK.ipynb  
    - Python SDK 로 오픈 소스 LLM 을 호스팅 및 실제 추론 결과를 보실 수 있습니다.
    - 아래 2번을 먼저 실행하시고, 1번은 참조 확인 하세요.
- 2.Deploy-Kor-LLM-Boto3.ipynb
    - Boto3 로 오픈 소스 LLM 을 호스팅 및 실제 추론 결과를 보실 수 있습니다.
    - 다음의 모델을 노트북에서 모델을 선택하여 배포할 수 있습니다.
        - Kullm-polyglot-12-8b-v2
        - KoAlpaca-12-8B
        - Polyglot-Kor-5-8B
- 3.Deploy-LLM-JS-AI21.ipynb  
    - AI21 Contexture Aware 모델 호스팅 입니다.
    - 현재 유료이기에 참조만 하세요.
- 4.Kor-Embedding-Model.ipynb  
    - 허깅 페이스의 'BM-K/KoSimCSE-roberta' 한국어 임베딩 모델을 배포 및 추론 하는 예제 입니다.



## Reference:
- Blog: Deploy BLOOM-176B and OPT-30B on Amazon SageMaker with large model inference Deep Learning Containers and DeepSpeed
    - https://aws.amazon.com/blogs/machine-learning/deploy-bloom-176b-and-opt-30b-on-amazon-sagemaker-with-large-model-inference-deep-learning-containers-and-deepspeed/
- Blog: Deploy large models on Amazon SageMaker using DJL Serving and DeepSpeed model parallel inference
    - https://aws.amazon.com/blogs/machine-learning/deploy-large-models-on-amazon-sagemaker-using-djlserving-and-deepspeed-model-parallel-inference/
- SageMaker Large model inference tutorials
    - https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference-tutorials.html
- Use DJL with the SageMaker Python SDK
    - https://sagemaker.readthedocs.io/en/stable/frameworks/djl/using_djl.html
- Example notebooks: AWS SageMaker examples GitHub repository.
    - https://github.com/aws/amazon-sagemaker-examples/tree/7bcbec65be55a8c160bc757b051d7508c9114846/inference/nlp/realtime/llm