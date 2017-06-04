#!/usr/bin/env python

import boto3
import sys

SNS = boto3.client('sns')

for snstopicarn in sys.argv[1:]:
    response = SNS.delete_topic(
    TopicArn=snstopicarn
)
    print response
