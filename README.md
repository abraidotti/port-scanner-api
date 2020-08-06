# port-scanner-api

WIP

## Structure

This service has a separate directory for all the scan operations. For each operation exactly one file exists e.g. `scans/delete.py`. In each of these files there is exactly one function defined.

The idea behind the `scans` directory is that in case you want to create a service containing multiple resources e.g. users, notes, comments you could do so in the same service. While this is certainly possible you might consider creating a separate service for each resource. It depends on the use-case and your preference.

## Use-cases

- API for a Web Application
- API for a Mobile Application

## Setup

```bash
npm install
```

## Deploy

In order to deploy the endpoint simply run

```bash
serverless deploy
```

The expected result should be similar to:

```bash
Serverless: Packaging service…
Serverless: Uploading CloudFormation file to S3…
Serverless: Uploading service .zip file to S3…
Serverless: Updating Stack…
Serverless: Checking Stack update progress…
Serverless: Stack update finished…

Service Information
service: serverless-rest-api-with-pynamodb
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  POST - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/scans
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/scans
  GET - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/scans/{id}
  PUT - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/scans/{id}
  DELETE - https://45wf34z5yf.execute-api.us-east-1.amazonaws.com/dev/scans/{id}
functions:
  serverless-rest-api-with-pynamodb-dev-update: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-pynamodb-dev-update
  serverless-rest-api-with-pynamodb-dev-get: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-pynamodb-dev-get
  serverless-rest-api-with-pynamodb-dev-list: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-pynamodb-dev-list
  serverless-rest-api-with-pynamodb-dev-create: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-pynamodb-dev-create
  serverless-rest-api-with-pynamodb-dev-delete: arn:aws:lambda:us-east-1:488110005556:function:serverless-rest-api-with-pynamodb-dev-delete
```

## Usage

You can create, retrieve, update, or delete scans with the following commands:

### Create a scan

```bash
curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans --data '{ "text": "Learn Serverless" }'
```

No output

### List all scans

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans
```

Example output:
```bash
[{"text":"Deploy my first service","id":"ac90feaa11e6-9ede-afdfa051af86","checked":true,"updatedAt":1479139961304},{"text":"Learn Serverless","id":"206793aa11e6-9ede-afdfa051af86","createdAt":1479139943241,"checked":false,"updatedAt":1479139943241}]%
```

### Get one scan

```bash
# Replace the <id> part with a real id from your scans table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans/<id>
```

Example Result:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":false,"updatedAt":1479138570824}%
```

### Update a scan

```bash
# Replace the <id> part with a real id from your scans table
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans/<id> --data '{ "text": "Learn Serverless", "checked": true }'
```

Example Result:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":true,"updatedAt":1479138570824}%
```

### Delete a scan

```bash
# Replace the <id> part with a real id from your scans table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans/<id>
```

No output

