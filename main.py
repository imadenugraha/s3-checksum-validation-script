from uploadBackup import upload_backup
from getChecksumS3 import getChecksumS3
from validateChecksum import validateChecksum
import os
import subprocess
import logging
import datetime


def main():
    now = datetime.date.today()

    # Run backup.sh
    try:
        subprocess.run(["./backup.sh"], shell=True, stderr=True)
    except PermissionError as pe:
        logging.error(pe)
        log_entry = f"{now},STATUS=ERROR ({pe})"

        with open('log', 'a') as f:
            f.write(log_entry + '\n')
            f.close()

        return exit(1)

    # Upload backup and validated the MD5
    try:
        list_backup = os.listdir("temp")
        os.chdir("temp")

        for file in list_backup:
            upload_backup(file)
            with open("../MD5_S3_CHECKSUM", 'a') as f:
                f.write(getChecksumS3(file) + "\n")
                f.close()

        os.chdir("..")

        valid = validateChecksum("LOCAL_MD5", "MD5_S3_CHECKSUM")
        subprocess.run(["rm", "-rf", "temp", "LOCAL_MD5", "MD5_S3_CHECKSUM"], stdout=True)

        if valid is True:
            log_entry = f"{now},STATUS=SUCCESS (All file are validated!)"

            with open('log', 'a') as f:
                f.write(log_entry + '\n')
                f.close()
            return exit(0)
        else:
            log_entry = f"{now},STATUS=FAIL (Some file is not validated!)"

            with open('log', 'a') as f:
                f.write(log_entry + '\n')
                f.close()
            return exit(0)
    except Exception as e:
        logging.error(e)
        log_entry = f"{now},STATUS=ERROR ({e})"

        with open('log', 'a') as f:
            f.write(log_entry + '\n')
            f.close()

        return exit(1)


if __name__ == "__main__":
    main()
