import boto3
from pprint import pprint
iam_client = boto3.client('iam', aws_access_key_id="AKIA4BI6MA4YOFTMCMIT",
                       aws_secret_access_key="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")

response = iam_client.list_policies(
    Scope='Local',
    PathPrefix='/'
)

for each_policy in response['Policies']:
    if each_policy['AttachmentCount'] == 0:
        print(each_policy['PolicyName'])