import boto3

vol_status = []
session = boto3.session.Session(profile_name="default")
ec2_console_handler = session.client(service_name="ec2", region_name="us-east-1")
#print(dir(ec2_console_handler))
vol = ec2_console_handler.describe_volumes()
#print(vol)
vol_dict = vol['Volumes']
#print(vol_dict)
for v in vol_dict:
    new_var = v['Attachments']
    #print(new_var)
    for st_vol in new_var:
        #print(st_vol)
        vol_status = st_vol['State']
        vol_id = st_vol['VolumeId']
        instance = st_vol['InstanceId']
        print(vol_status , vol_id, instance)
