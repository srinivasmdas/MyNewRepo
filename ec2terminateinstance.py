#!/usr/bin/env python

import boto3
import sys

ec2 = boto3.resource('ec2')

for instance_id in sys.argv[1:]:
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print response

