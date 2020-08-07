import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    print(event)
    data = json.loads(event['body'])
    print(data)
    if 'text' not in data:
        logging.error("Validation Failed - no text")
        raise Exception("Couldn't create the scan item.")

    if 'user_id' not in data:
        logging.error("Validation Failed - no user_id")
        raise Exception("Couldn't create the scan item.")

    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'user_id': data['user_id'],
        'scan_id': str(uuid.uuid1()),
        'text': data['text'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
