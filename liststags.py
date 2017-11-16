import boto3
ec2 = boto3.resource('ec2')
instid = []
instid = ec2.instances.all()
for i in instid:
	inslist = i.id
instance = ec2.Instance(inslist)
for tags in instance.tags:
    if tags['Key'] == 'InstanceRole':
        val = tags['Value']
print val
