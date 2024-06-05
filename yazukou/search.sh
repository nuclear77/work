#!/bin/bash


if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Необходимо указать строку для поиска и путь к каталогу в качестве первого и второго аргументов."
  exit 1
fi


if [ ! -d "$2" ]; then
  echo "Указанный каталог не существует."
  exit 1
fi


for file in "$2"/*; do
  if [ -f "$file" ]; then
    if grep -q "$1" "$file"; then
      echo "Файл: $file"
      echo "Размер: $(du -h "$file" | cut -f1)"
      echo "---"
    fi
  elif [ -d "$file" ]; then
    "$0" "$1" "$file" 
  fi
done
#ex2task2