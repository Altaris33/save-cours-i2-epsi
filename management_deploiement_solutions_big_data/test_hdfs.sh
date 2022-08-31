#!/bin/bash
# Create overall treemap

mkdir logs
logs_creation=$(date)
backup_dir=$(date +'%m-%d-%Y')
mkdir $backup_dir
cat $logs_creation > logs/$backup_dir/logs-$backup_dir