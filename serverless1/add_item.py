import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('properties')
# add new items to the table using DynamoDB.Table.put_item():
table.put_item(
   item={
        'str_address': '1045 S Maguire Street',
        'zip': '64093',
        'city': 'Warrensburg',
        'state': 'MO',
    }
)


