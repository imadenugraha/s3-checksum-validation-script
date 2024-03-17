from uploadBackup import upload_backup
import os
import subprocess
import logging
import datetime


def main():
    now = datetime.date.today()

    try:
        subprocess.run(["./backup.sh"], shell=True, stdout=True)
    except PermissionError as pe:
        logging.error(pe)
        log_entry = f"{now},STATUS=ERROR({pe})"
        with open('log', 'a') as f:
            f.write(log_entry + '\n')
        return exit(1)

    try:
        list_backup = os.listdir("temp")
        os.chdir("temp")
        for file in list_backup:
            upload_backup(file)
        log_entry = f"{now},STATUS=SUCCESS(ALL DATA ARE VALIDATED)"
        with open('log', 'a') as f:
            f.write(log_entry + '\n')
        return exit(0)
    except Exception as e:
        logging.error(e)
        log_entry = f"{now},STATUS=ERROR({e})"
        with open('log', 'a') as f:
            f.write(log_entry + '\n')
        return exit(1)


if __name__ == "__main__":
    main()
