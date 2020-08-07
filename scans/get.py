import json

from pynamodb.exceptions import DoesNotExist
from scans.scan_model import ScanModel


def get(event, context):
    try:
        found_scan = ScanModel.get(
            hash_key=event['path']['user_id'], range_key=event['path']['scan_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'scan was not found'})}

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(found_scan))}
