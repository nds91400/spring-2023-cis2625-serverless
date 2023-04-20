import boto3
# Get the service resource
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('Students1')
# update attributes of the item in the table using DynamoDB.Table.update()
table.update_item(
    Key={
        'SID': '91400'
        'email': 'nds91400@ucmo.edu'
    },
    UpdateExpression = 'SET age = :val1'
    ExpressionAttributeVlaues={
        ':val1': 26
    }
)