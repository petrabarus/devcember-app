import json

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

def postComment(event, context):
    comment = {
        "id": 3,
        "name": 'Petra',
        "comment": 'Hello World!',
        "createdAt": 1481924300,
    }
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
