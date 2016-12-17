import json
import time
import boto3

client = boto3.client('dynamodb')

def fetchCommentFromDatabase():
    return [
        {
            "id": 1,
            "name": 'Petra',
            "comment": 'Hello World!',
            "createdAt": 1481924490,
        },
        {
            "id": 2,
            "name": 'Petra',
            "comment": 'Hello World!',
            "createdAt": 1481924300,
        }
    ];

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
