import json
import boto3
import botocore.exceptions

sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:eu-west-2:659206698074:cetm67-odip-sub-v1-dev'

def lambda_handler(event, context):
    try:
        data = get_data(event)
        send_to_sns(data)
        
        return {
            'statusCode': 200,
            'body': "Message Sent"
        }
    except Exception as e:
        return {
            'statusCode': 200,
            'headers': {},
            'body': json.dumps(str(e))
        }
    
def get_data(event):
    try:
        body = json.loads(event['body'])
        
        return body
    except:
        raise

def send_to_sns(data):
    sns.publish(
        TopicArn=topic_arn,
        Message=json.dumps(data)
        )