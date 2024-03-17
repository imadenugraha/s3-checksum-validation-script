# S3 File Integrity Validation Script

## How to Use
1. Make sure you have AWS Account to access S3
2. Create Access Key from your AWS Account
3. Rename .env.example to .env
4. Insert Access Key, Secret Key, Region, and Bucket Name to .env file
5. Make sure after cloning this project, give proper permission to backup.sh

```bash
$ chmod u+x backup.sh
```

6. You need to install poetry on your local system. After that, you can install the dependencies

```bash
$ poetry install --no-root
```

7. Create user for backup. Grant connect to database that you want to backup.
8. Insert your backup user credential to .env file
9. Run script using poetry

```bash
$ poetry run python main.py
```