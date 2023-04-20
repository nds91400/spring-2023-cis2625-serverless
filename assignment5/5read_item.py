import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('Students1')
# retreive a table item using DynamoDB.Table.get_item()
response = table.get_item(
    Key={
        'SID': '91400',
        'email': 'nds91400@ucmo.edu'
    })
# print(type(response))
# print(response)
item = response['Item']
print(item)