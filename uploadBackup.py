from botocore.exceptions import ClientError
from dotenv import load_dotenv
from session import new_session
import datetime
import logging
import os


def upload_backup(file_name, object_name=None) -> bool:
    load_dotenv()
    bucket_name = os.getenv("AWS_BUCKET_NAME")

    current_date = datetime.date.today()
    sess = new_session()

    if object_name is None:
        object_name = os.path.basename(file_name)

    key = f"{current_date.strftime('%Y-%m-%d')}/{file_name}"

    s3_client = sess.client('s3')
    try:
        s3_client.upload_file(
            Filename=file_name,
            Bucket=bucket_name,
            Key=key)
    except ClientError as e:
        logging.error(e)
        return False
    return True
