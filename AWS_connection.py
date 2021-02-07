"""
Created on Nov 10, 2020

@author: Behnaz Poursartip
"""

import sklearn
import boto3
from boto3.dynamodb.conditions import Key, Attr
from matplotlib import pyplot as plt
import datetime
import pandas as pd
import csv
import numpy as np
import json, codecs
import base64

def read_s3_data(access_key, secret_access_key, region, file_name):

    client = boto3.client('s3', aws_access_key_id=access_key,
                          aws_secret_access_key=secret_access_key,
                          region_name=region)
    response = client.get_object(Bucket='data-XX', Key=file_name)
    lines = response['Body'].read()

    return lines


def list_s3_files(access_key, secret_access_key, region):
    """

    Input: AWS access information

    """
    s3 = boto3.resource('s3', aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_access_key,
                                     region_name=region)

    bucket = s3.Bucket('data-XX')
    s3_info_list = []
    for my_bucket_object in bucket.objects.all():
        x_file_name = my_bucket_object.key
        name_items = x_file_name.split('-')
        pod_id = name_items[1]
        try:
            time_stamp = int(name_items[2])
            s3_info_list.append([x_file_name, pod_id, time_stamp])

        except:
            print('invalid time stamp: ', name_items[2])
    return s3_info_list


def query_metrics(pod_id, access_key, secret_access_key, region, dynamodb=None):
    if not dynamodb:

        my_dynamodb = boto3.resource('dynamodb', aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_access_key,
                                     region_name=region)
    table = my_dynamodb.Table('Metric')
    response = table.query(KeyConditionExpression=Key('podId').eq(pod_id))

    return response['Items']

def query_data(pod_id, target_ts, access_key, secret_access_key, region, dynamodb=None):

    if not dynamodb:
        my_dynamodb = boto3.resource('dynamodb', aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_access_key,
                                     region_name=region)
    table = my_dynamodb.Table('XX_Data')
    response = table.scan(FilterExpression=Attr('podId').eq(pod_id))
    response = table.scan(FilterExpression=Attr('timestamp').eq(target_ts) & Attr('podId').eq(pod_id))

    items = response['Items']
    return items



if __name__ == '__main__':


    access_key = 'ABCDEF'
    secret_access_key = 'ABCDEF'
    region = 'us'

    pod_id = '123'
    date_str = '2018-12-20 20:10:00'

    str_to_dt = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    target_ts = int(str_to_dt.timestamp()*1000)

    metrics = query_metrics(pod_id, access_key, secret_access_key, region)
    dynamo_ch_info = query_data(pod_id, target_ts, access_key, secret_access_key, region, dynamodb=None)
