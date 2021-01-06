import json
import logging
import boto3
import time
import os
 
def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.debug(json.dumps(event))
    
    allFiles = ['/*']
    client = boto3.client('cloudfront')
    invalidation = client.create_invalidation(
        DistributionId = os.environ['DistributionId']
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': allFiles
        },
        'CallerReference': str(time.time())
    })
    
    codepipeline = boto3.client('codepipeline')
    job_id = event['CodePipeline.job']['id']
 
    try:
        pipeline = boto3.client('codepipeline')
        jobId=event['CodePipeline.job']['id']
        response = pipeline.put_job_success_result(jobId=job_id)
        logger.debug(response)
    except Exception as error:
        logger.exception(error)
        response = codepipeline.put_job_failure_result(
            jobId=job_id,
            failureDetails={
              'type': 'JobFailed',
              'message': f'{error.__class__.__name__}: {str(error)}'
            }
        )
        logger.debug(response)
