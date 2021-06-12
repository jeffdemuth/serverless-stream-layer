import json
import boto3
import time
client = boto3.client('lambda')

def lambda_handler(event, context):
    if event['requestContext']['routeKey'] == '$connect':
        client.invoke(FunctionName='ws-default', InvocationType='Event', Payload=json.dumps(event))
    return { 'statusCode': 200, 'headers': {'Content-Type':'application/json','Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': '*' } }