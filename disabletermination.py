#!/usr/bin/env python

import boto3
import sys

ec2 = boto3.resource('ec2', region_name='us-east-1')
for myinstance in sys.argv[1:]:
    instance = ec2.Instance(myinstance)
    response = instance.modify_attribute(
        Attribute='disableApiTermination',
        Value='True')
    print response



