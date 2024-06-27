#!/bin/bash
directory=$1
extension=$2
output_file=$3

echo "имена файлов с расширением $extension в каталоге $directory:"
find $directory -type f -name "*.$extension" -exec basename {} \; > $output_file
#task4