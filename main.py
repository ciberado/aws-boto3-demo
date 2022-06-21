import boto3
from botocore.exceptions import ClientError
import io

s3_client = boto3.client('s3', region_name='eu-west-1')

file_binary = open("./README.md", "rb").read()
file_content = io.BytesIO(file_binary)

s3_client.upload_fileobj(file_content, "aws-boto3-demo-bucket", "README.md")

