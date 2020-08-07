import json
import logging
import uuid

from scans.scan_model import ScanModel


def create(event, context):
    data = json.loads(event['body'])
    print(event)
    if 'text' not in data:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the scan item.'})}

    if not data['text']:
        logging.error('Validation Failed - text was empty. %s', data)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the scan item. No text.'})}

    a_scan = ScanModel(user_id=data['user_id'],
                       scan_id=str(uuid.uuid1()),
                       text=data['text'])

    # write the scan to the database
    a_scan.save()

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(dict(a_scan))}
