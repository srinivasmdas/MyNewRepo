#!/usr/bin/env python

import boto3
import sys

S3 = boto3.resource('s3')
for bucketname in sys.argv[1:]:
    bucket = S3.Bucket(bucketname)
try:
        response = bucket.delete()
        print response
except Exception as error:
    print error
