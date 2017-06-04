#!/usr/bin/env python

import boto3
import sys

S3 = boto3.resource("s3")
for bucket_iterator in S3.buckets.all():
    print bucket_iterator.name


