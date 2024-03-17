from botocore.exceptions import ClientError
from session import new_session
from dotenv import load_dotenv
import os
import datetime
import logging


def getChecksumS3(file_name):
    load_dotenv()
    bucket_name = os.getenv("AWS_BUCKET_NAME")
    current_date = datetime.date.today()

    sess = new_session()
    s3_client = sess.client('s3')

    key = f"{current_date.strftime('%Y-%m-%d')}/{file_name}"

    try:
        response = s3_client.head_object(
            Bucket=bucket_name,
            Key=key
        )
        md5_checksum = response['ETag'].strip('"')
        return md5_checksum
    except ClientError as e:
        return logging.error(e)


def main():
    file = os.listdir("temp")
    os.chdir("temp")
    for file_name in file:
        with open("../MD5_S3_CHECKSUM", "a") as f:
            f.write(getChecksumS3(file_name) + "\n")
            f.close()


if __name__ == "__main__":
    main()
