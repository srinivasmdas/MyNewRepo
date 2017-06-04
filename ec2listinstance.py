#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2')
for myinstancelist in ec2.instances.all():
    print myinstancelist.id, myinstancelist.state

