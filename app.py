import boto3
client = boto3.client('ec2')
response = client.run_instances(
    ImageId = 'ami-0c80e2b6ccb9ad6d1',
    InstanceType = 't2.micro',
    KeyName='demo',
    MaxCount=1,
    MinCount=1,
)

