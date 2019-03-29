| => cat Check_OOM.py
#!/usr/bin/python
import boto3
import time
import datetime
import re
import sys
#from datetime import datetime, timedelta
from boto3.resources import response
regions = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "eu-central-1", "eu-west-1", "ca-central-1", "eu-west-2"]
try:
    import botocore
    import boto3
    UseBoto = True
except:
    UseBoto = False
    print ("-------------------------------------------")
    print ("Unable to load Boto.  Please install Botot3")
    print ("-------------------------------------------")
    sys.exit(1)
def describe_log_streams(region):
        if UseBoto:
                session = boto3.session.Session(profile_name="default")
                client = session.client('logs', region_name=region)

                try:
                        response = client.describe_log_groups(
                        logGroupNamePrefix='pe-prod-ROOT-PEGACLOUD',
                        limit=50
                                )
                except:
                        print ("Error in getting log_group_names")
                        sys.exit(1)


                while True:
                        for each in response['logGroups']:
                                group_name=each['logGroupName']
                                try:
                                    response1 = client.describe_log_streams(logGroupName=group_name,limit=50)

                                except:
                                    print ("Error in getting log_group_names")
                                    sys.exit(1)
                                while True:
                                    for idx in range(0, len(response1['logStreams'])):
                                        log_stream_name=response1['logStreams'][idx]['logStreamName']
                                        if (("messages" in log_stream_name) and ("PEGAWEB" in log_stream_name) and (int(response1['logStreams'][idx]['lastEventTimestamp']) >= int(1541010600000))) or (("messages" in log_stream_name) and ("PegaAppTier" in log_stream_name) and (int(response1['logStreams'][idx]['lastEventTimestamp']) >= int(1541010600000))):
                                            time.sleep(1)
                                            response2 = client.filter_log_events(logGroupName=group_name,logStreamNames=[log_stream_name],limit=1,filterPattern='Out of memory')
                                            for log in response2['events']:
                                                if log['logStreamName'] is not None:
                                                    log_stream_name1=response1['logStreams'][idx]['logStreamName']
                                                    instancetype=''
                                                    version, tier, instanceid, internal, infra, messages = log_stream_name.split('/')
                                                    if ((instanceid in log_stream_name1) and ("cfn-init-cmd" in log_stream_name1)):
                                                        time.sleep(1)
                                                        print ('a')
                                                        response3 = client.filter_log_events(logGroupName=group_name,logStreamNames=[log_stream_name1],limit=1,filterPattern='InstanceType')
                                                        print (response3['events'])
                                                        for event in response3['events']:
                                                            instancetype=event['message']
                                                    print (log['logStreamName']+', '+group_name+', '+str(log['timestamp'])+', '+'True'+', '+instancetype)
                                            if not response2['events']:
                                                print (log_stream_name+', '+group_name+', '+'None'+', '+'False')
                                    try:
                                        response1 = client.describe_log_streams(logGroupName=group_name,nextToken=response1['nextToken'],limit=50)
                                    except:
                                        break

                        try:
                                response = client.describe_log_groups(
                                        nextToken=response["nextToken"],
                                limit=50
                                        )
                        except:
                                break




def main():
        global regions
        global instancetype
        print ("logStreamName, LogGroupName, TimeStamp, Is_OOM_exist")
        for region in regions:
            output = describe_log_streams(region)


if __name__ == "__main__":
        main()
