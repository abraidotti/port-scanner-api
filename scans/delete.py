import json

from pynamodb.exceptions import DoesNotExist, DeleteError
from scans.scan_model import ScanModel


def delete(event, context):
    try:
        found_scan = ScanModel.get(hash_key=event['path']['user_id'], range_key=event['path']['scan_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'scan was not found'})}
    try:
        found_scan.delete()
    except DeleteError:
        return {'statusCode': 400,
                'body': json.dumps({'error_message': 'Unable to delete the scan'})}

    # create a response
    return {'statusCode': 204}
