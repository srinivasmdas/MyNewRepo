#!/usr/bin/env python

import boto3
import sys

SNS = boto3.client('sns', region_name='us-east-1')
for topicarnname in sys.argv[1:]:
    response = SNS.subscribe(
    TopicArn=topicarnname,
    Protocol='email',
    Endpoint='srinivas.m.das@gmail.com')
    print response
