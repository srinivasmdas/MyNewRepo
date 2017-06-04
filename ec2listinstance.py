#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
for myinstancelist in ec2.instances.all():
    print myinstancelist.id, myinstancelist.state

