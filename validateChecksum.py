import logging


def validateChecksum(md5_local, md5_s3) -> bool:
    md5_local_list = []
    md5_s3_list = []
    try:
        with open(md5_local, 'r') as f:
            data = f.readlines()
            md5_local_list.extend(data)
            f.close()

        with open(md5_s3, 'r') as f:
            data = f.readlines()
            md5_s3_list.extend(data)
            f.close()

        if md5_local_list == md5_s3_list:
            return True
    except Exception as e:
        logging.error(e)
        return False
