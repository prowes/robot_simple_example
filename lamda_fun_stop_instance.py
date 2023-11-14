import boto3

REGION = 'eu-north-1'
INSTANCES = ['i-0c9a7348dc231335b']
EC2 = boto3.client('ec2', region_name=REGION)

def lambda_handler(event, context):
    EC2.stop_instances(InstanceIds=INSTANCES)
    print(f'started your instances {str(INSTANCES)}')
