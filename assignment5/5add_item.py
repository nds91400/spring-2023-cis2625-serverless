import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('Students1')
# add new items to the table using DynamoDB.Table.put_item():
table.put_item(
   Item={
        'SID': '91400',
        'first_name': 'Nate',
        'last_name': 'Saluri',
        'age': 19,
        'email': 'nds91400@ucmo.edu'
    }
)