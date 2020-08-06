import json
import logging

from pynamodb.exceptions import DoesNotExist
from scans.scan_model import ScanModel


def update(event, context):
    # scan: Figure out why this is behaving differently to the other endpoints
    # data = json.loads(event['body'])
    data = event['body']

    if 'text' not in data and 'checked' not in data:
        logging.error('Validation Failed %s', data)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t update the scan item.'})}

    try:
        found_scan = ScanModel.get(hash_key=event['path']['user_id'], range_key=event['path']['scan_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'scan was not found'})}

    scan_changed = False
    if 'text' in data and data['text'] != found_scan.text:
        found_scan.text = data['text']
        scan_changed = True

    if scan_changed:
        found_scan.save()
    else:
        logging.info('Did not update.')

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(found_scan))}

