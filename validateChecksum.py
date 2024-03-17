import logging


def validateChecksum(md5_local, md5_s3) -> bool:
    md5_local_list = []
    md5_s3_list = []
    try:
        with open(md5_local, 'r') as f:
            md5_local_list.append(f)
            f.close()

        with open(md5_s3, 'r') as f:
            md5_s3_list.append(f)
            f.close()

        if md5_local_list == md5_s3_list:
            return True
    except Exception as e:
        logging.error(e)
        return False
