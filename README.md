# invalidate-cache-lambda

Lambda function which is invoked as one of the jobs in a codepipeline for a static website

Using python3 and [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html) to invalidate the CloudFront distribution cache and set the pipline job to complete.

# CI/CD

Continuous integration and delivery to Lamda Functions is ensured with Git Actions 

![Lambda CI/CD](https://github.com/smeubank/invalidate-cache-lambda/blob/smeubank/assets/lamda-cicd.PNG?raw=true)

# Reference

[Modern CI/CD Pipeline: Github Actions with AWS Lambda Serverless Python Functions and API Gateway](https://towardsdatascience.com/modern-ci-cd-pipeline-git-actions-with-aws-lambda-serverless-python-functions-and-api-gateway-9ef20b3ef64a)
