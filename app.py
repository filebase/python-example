import os
import boto3
import logging
from pprint import pprint

from botocore.config import Config
from botocore.exceptions import ClientError

boto_config = Config(
    region_name = 'us-east-1',
    signature_version = 's3v4',
)

s3 = boto3.client('s3',
                  endpoint_url='https://s3.filebase.com',
                  aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                  config=boto_config)

response = s3.list_buckets()
pprint(response)
