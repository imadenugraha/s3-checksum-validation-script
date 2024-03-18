#!/usr/bin/bash

backup_dir="temp"
backup_date=$(date +"%Y-%m-%d")
database=$(sudo -u postgres psql -U postgres -l -t 2> /dev/null | cut -d \| -f 1 | grep -vE '^(template0|template1|postgres)$')

if [[ -d ".env" ]]; then
  echo "File .env didn't exist!"
else
  source .env
fi

mkdir "$backup_dir"

for db in $database; do
    if [[ "$db" != "template"* && "$db" != "postgres" ]]; then
        backup_file="$db"_"$backup_date".backup
        PGPASSWORD="$POSTGRES_PASS" pg_dump -U "$POSTGRES_USER" -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -Fc -b "$db" | sudo tee "$backup_dir/$backup_file" > /dev/null
        touch LOCAL_MD5 MD5_S3_CHECKSUM log
        md5sum "$backup_dir/$backup_file" | awk '{print $1}' | tee -a LOCAL_MD5 > /dev/null
    fi
done
