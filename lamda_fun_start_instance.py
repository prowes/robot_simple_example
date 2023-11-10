import boto3
region = 'eu-north-1'
instances = ['i-0c9a7348dc231335b']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
