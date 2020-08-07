# port-scanner-api

WIP

## Context

## Setup

```bash
npm install
```

## Deployment

In order to deploy the endpoint simply run:

```bash
serverless deploy --profile XXX
```

## Usage

You can create, retrieve, update, or delete scans with the following commands:

### Create a scan

```bash
curl -X POST https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/main/scans -H "x-api-key: XXX" --data "{ ""text"": ""This is a scan."", ""user_id"": ""555"" }"

```

No output

### List all scans

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans
```

### Get one scan

```bash
# Replace the <id> part with a real id from your scans table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans/<id>
```

### Update a scan

```bash
# Replace the <id> part with a real id from your scans table
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans/<id> --data "{ ""text"": ""This is a new scan."", ""user_id"": ""555"" }"
```

### Delete a scan

```bash
# Replace the <id> part with a real id from your scans table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans/<id>
```

No output
