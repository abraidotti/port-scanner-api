import os
import json

import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.get_item(
        Key={
            'user_id': event['pathParameters']['user_id'],
            'scan_id': event['pathParameters']['scan_id'],
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
    }

    return response
