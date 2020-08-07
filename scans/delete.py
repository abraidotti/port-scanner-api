
import os

import boto3
dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        table.delete_item(
            Key={
                'user_id': event['pathParameters']['user_id'],
                'scan_id': event['pathParameters']['scan_id'],
            }
        )
    except:
        print("Error deleting.")
        response = {
            "statusCode": 404
        }
        return response

    response = {
        "statusCode": 200
    }

    return response
