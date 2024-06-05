oldIFS=$IFS
IFS=$'\n'
for line in $(cat /var/users)
do
  user=$(echo $line | cut -d' ' -f1)
  group=$(echo $line | cut -d' ' -f2)
  echo Username: $user Group: $group
done
IFS=$oldIFS
