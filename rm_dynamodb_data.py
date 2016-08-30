#########################################################################
#-*- coding:utf-8 -*-
# File Name: delete_enduser.py
#########################################################################
#!/bin/python
import boto3
from boto3.dynamodb.conditions import Key, Attr
import pprint

def read_table_items(table):
    response = table.scan(FilterExpression=Attr('oid').ne('*'))
    items = response['Items']
    for item in items:
        yield item

def delete_item(table, oid):
    table.delete_item(
            Key={
                'oid':oid
                }
            )

if __name__ == "__main__":
    dynamodb = boto3.resource("dynamodb", region_name="china", endpoint_url="http://localhost:8000")
    table = dynamodb.Table("table_name")
    for item in read_table_items(table):
        oid = item.get('oid')
        print oid
        print "-"*30
        delete_item(table, oid)
