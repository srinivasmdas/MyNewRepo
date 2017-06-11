#!/usr/bin/env python

import boto3
import sys
ec2 = boto3.resource('ec2', region_name='us-east-1')

for instanceid in sys.argv[1:]:
    instance = ec2.Instance(instanceid)
    tagkey = instance.tags[0]['Key']
    tagvalue = instance.tags[0]['Value']
    print "instance %s has %s as tagkey and %s as tagvalue"%(instanceid, tagkey, tagvalue)


