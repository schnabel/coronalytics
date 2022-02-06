import boto3
import os
from rki import urls

QUEUE_NAME = os.getenv("SQSqueueName")
sqs = boto3.resource('sqs')
queue = sqs.Queue(QUEUE_NAME)

def lambda_handler(event, context):
    try:
        for state in urls.keys():
            queue.send_message(MessageBody=state)
    except Exception as e:
        print(e)
        raise e