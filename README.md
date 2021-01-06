# invalidate-cache-lambda

Lambda function which is invoked as one of the jobs in a codepipeline for a static website

Using python3 and [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html) to invalidate the cash and set the pipline job to completed
