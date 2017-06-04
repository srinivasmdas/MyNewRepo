#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
myinstance = ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    ImageId='ami-c58c1dd3',
    KeyName='Srini_GitKey',
    InstanceType='t2.micro',
    Placement={
        'AvailabilityZone': 'us-east-1b'
    }
)

    
