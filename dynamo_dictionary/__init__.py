import time
import json
import boto3

class DynamoDictionary():
    def __init__(self, table_name, region_name=None, aws_access_key_id=None, aws_secret_access_key=None):

        self.client = boto3.client(
            'dynamodb', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
            
        self.table_name = table_name
        self.create_table()

    def create_table(self):
        try:
            self.client.describe_table(TableName=self.table_name)
        except:
            self.client.create_table(**{
                "AttributeDefinitions": [
                    {
                        "AttributeName": "Name",
                        "AttributeType": "S"
                    },
                ],
                "TableName": self.table_name,
                "KeySchema": [
                    {
                        "AttributeName": "Name",
                        "KeyType": "HASH",
                    }                 
                ],

                "BillingMode": "PAY_PER_REQUEST",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "Auto Created"
                    }
                ]
            })
            print("waiting for create table. . .")
            time.sleep(10)

    def get(self, keys):

        if not isinstance(keys, list):
            keys = [keys]

        items = {}
        for key in keys:
            resp = self.client.get_item(TableName=self.table_name, Key={
                "Name": {
                    "S": key
                }
            })
            print(key)

            try:
                items[key] = json.loads(resp["Item"]["Value"]["S"])
            except:
                pass

        return items

    def get_all(self):
        items = {}
        resp = self.client.scan(TableName=self.table_name)
        for raw_item in resp["Items"]:

            try:
                items[raw_item["Name"]["S"]] = json.loads(
                    raw_item["Value"]["S"])
            except:
                pass

        return items

    def put(self, key, value):
        return self.client.put_item(TableName=self.table_name, Item={
            "Name": {
                "S": key
            },
            "Value": {
                "S": json.dumps(value, ensure_ascii=False, default=str)
            }
        })

    def delete(self, keys):
        if not isinstance(keys, list):
            keys = [keys]
                    
        list_delete_resp = []
        for key in keys:
            list_delete_resp.append(self.client.delete_item(TableName=self.table_name, Key={
                "Name": {
                    "S": key
                }
            }))

        return list_delete_resp