import json
import time
import logging
import os

import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.update_item(
        Key={
            'user_id': event['pathParameters']['user_id'],
            'scan_id': event['pathParameters']['scan_id'],
        },
        ExpressionAttributeNames={
            '#scan_text': 'text',
        },
        ExpressionAttributeValues={
            ':text': data['text'],
            ':updatedAt': timestamp,
        },
        UpdateExpression='SET #scan_text = :text, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'])
    }

    return response
