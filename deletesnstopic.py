#!/usr/bin/env python

import boto3
import sys

SNS = boto3.client('sns', region_name='us-east-1')

for snstopicarn in sys.argv[1:]:
    response = SNS.delete_topic(
    TopicArn=snstopicarn
)
    print response
