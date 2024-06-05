#!/bin/bash


if [ -z "$1" ]; then
  echo "Необходимо указать путь к каталогу в качестве первого аргумента."
  exit 1
fi


if [ ! -d "$1" ]; then
  echo "Указанный каталог не существует."
  exit 1
fi

for file in "$1"/*; do
  if [ -f "$file" ]; then
    echo "Файл: $file"
    echo "Размер: $(du -h "$file" | cut -f1)"
    echo "Права доступа: $(stat -c %A "$file")"
    echo "---"
  elif [ -d "$file" ]; then
    "$0" "$file" 
  fi
done
#ex2task1