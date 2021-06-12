import json
import boto3
import time
import datetime
client = boto3.client('location')

def lambda_handler(event, context):
    time.sleep(1)
    response = {'statusCode': 200}
    connection_id = event.get('requestContext', {}).get('connectionId')
    domain = event.get('requestContext', {}).get('domainName')
    stage = event.get('requestContext', {}).get('stage')
    apig_management_client = boto3.client('apigatewaymanagementapi', endpoint_url=f'https://{domain}/{stage}')
    for x in range(70, 175):
        message = '{"geometry":{"x":' + str(x) + '.57909994591,"y":-16.585220799794,"z":425.04900130983,"spatialReference":{"wkid":4326}},"attributes":{"name":"iss","ObjectId":2' + str(x) + '44,"TRACKID":25544,"visibility":"daylight","timestamp":' + str(time.time() * 1000) + ',"globalid":"{A886847F-2620-153D-102E-EDC' + str(x) + 'FD6A7A0}"}}'
        client.batch_update_device_position( TrackerName='mytracker', Updates=[ { 'DeviceId': 'DeathStar', 'Position': [ float(str(x) + '.57909994591'), -16.585220799794 ], 'SampleTime': datetime.datetime.now() }])
        send_response = apig_management_client.post_to_connection(Data=message, ConnectionId=connection_id)
        time.sleep(2)
    return { 'statusCode': 200, 'headers': {'Content-Type':'application/json','Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': '*' } }