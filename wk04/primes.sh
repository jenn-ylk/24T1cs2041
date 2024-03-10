#! /bin/dash

if [ $# -ne 1 ]
then
    echo "Usage: $0 <num>" 1>&2
    exit 1
fi

i=2

while [ $i -lt $1 ]
do
    sh is_prime.sh "$i" > /dev/null
    # check return value
    if [ $? -eq 0 ]
    then
        echo $i
    fi
    # increment
    i=$((i + 1))
done