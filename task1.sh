#!/bin/bash
filename="$1"
word_count=$(wc -w < "$filename")
echo "количество слов в файле $filename: $word_count"

