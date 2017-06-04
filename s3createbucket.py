#!/usr/bin/env python

import boto3
import sys

S3 = boto3.resource("s3")

for bucketname in sys.argv[1:]:
    try:
        response = S3.create_bucket(Bucket=bucketname)
        print response
    except Exception as error:
        print error
