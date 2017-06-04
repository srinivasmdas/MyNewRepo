#!/usr/bin/env python

import boto3
import sys

SNS = boto3.client('sns')
for topicname in sys.argv[1:]:
    response = SNS.create_topic(Name=topicname)
    print response
