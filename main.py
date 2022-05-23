import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)

try:
    s3_resource = boto3.resource(
        's3',
        endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
        aws_access_key_id='3a1dc232-c5de-43b3-abd4-a3f722b02ca0',
        aws_secret_access_key='12e9dac19354abf4521141056ff090b6b226ee8e6d93b55800f855ad40cc8513'
    )

except Exception as exc:
    logging.error(exc)
else:
    try:
        bucket = s3_resource.Bucket('telegramfiles')
        file_path = 'test.txt'
        object_name = 'test.txt'

        with open(file_path, "rb") as file:
            bucket.put_object(
                ACL='private',
                Body=file,
                Key=object_name
            )
    except ClientError as e:
        logging.error(e)
