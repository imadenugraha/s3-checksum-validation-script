from botocore.exceptions import ClientError
from dotenv import load_dotenv
from session import new_session
import logging
import datetime
import os


def create_backup_folder() -> bool:
    load_dotenv()
    bucket_name = os.getenv('AWS_BUCKET_NAME')

    current_date = datetime.date.today()

    sess = new_session()

    s3_client = sess.client('s3')
    try:
        s3_client.create_folder(Bucket=bucket_name, Key=current_date)
    except ClientError as e:
        logging.error(e)
        return False
    return True
