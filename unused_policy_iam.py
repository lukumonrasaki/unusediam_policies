import boto3
#  When you create access key remember the key must have IAM full access
iam_client = boto3.client('iam', aws_access_key_id="<put your access key>",
                       aws_secret_access_key="<put your secret access key>")

response = iam_client.list_policies(
    Scope='Local',
    PathPrefix='/'
)

for each_policy in response['Policies']:
    if each_policy['AttachmentCount'] == 0:
        print(each_policy['PolicyName'])
