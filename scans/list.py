import json

from scans.scan_model import ScanModel


def scan_list(event, context):
    # fetch all scans from the database
    results = ScanModel.scan()

    # create a response
    return {'statusCode': 200,
            'body': json.dumps({'items': [dict(result) for result in results]})}
