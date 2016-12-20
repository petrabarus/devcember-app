import json
import time
import boto3

def fetchCommentFromDatabase():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('DevcemberAppComments')
    response = table.scan()
    json_serializable = map(
        lambda item: {
            'id': item['id'],
            'name': item['name'],
            'comment': item['comment'],
            'createdAt': int(item['createdAt'])
        },
        response['Items'])
    return json_serializable

def getListComment(event, context):
    comments = fetchCommentFromDatabase();
    body = {
        "comments": comments
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            'Access-Control-Allow-Origin': '*'
        }
    }

    return response

def putCommentToDatabase(comment):
    client = boto3.client('dynamodb')
    return client.put_item(
        TableName='DevcemberAppComments',
        Item={
            'id': {
                'S': str(comment['id'])
            },
            'name': {
                'S': str(comment['name'])
            },
            'comment': {
                'S': str(comment['comment'])
            },
            'createdAt': {
                'N': str(comment['createdAt'])
            }
        }
    )

def postComment(event, context):
    timestamp = int(time.time())
    postedComment = json.loads(event['body'])
    comment = {
        "id": timestamp,
        "name": postedComment['name'],
        "comment": postedComment['comment'],
        "createdAt": timestamp
    }
    response = putCommentToDatabase(comment)

    body = {
        "comment": comment
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            'Access-Control-Allow-Origin': '*'
        }
    }

    return response
