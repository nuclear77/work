#!/bin/bash

# Variables
DB_NAME="mydatabase"
BACKUP_DIR="/home/lirik12/backups"
BACKUP_FILE="$BACKUP_DIR/backup_$(date +%F).sql"
REMOTE_USER="lirik"
REMOTE_HOST="192.168.1.**"
REMOTE_DIR="/home/remote/backups"

mysqldump -u root -p'frgQsy12' $DB_NAME > $BACKUP_FILE

scp $BACKUP_FILE $REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR

rm $BACKUP_FILE
