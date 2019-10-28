import boto3
tagname = "Name"
tagvalue = "Value"
ec2 = boto3.resource('ec2')
ec2.instances.filter(Filters=[
    {'Name': 'tag': [tagname], 'Values': [tagvalue]},
    {'Name': 'instance-state-name', 'Values': ['running']}
]).start()

ec2.instances.filter(Filters=[
    {'Name': 'tag': [tagname], 'Values': [tagvalue]},
    {'Name': 'instance-state-name', 'Values': ['stopped']}
]).stop()