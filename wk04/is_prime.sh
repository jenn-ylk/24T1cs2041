#! /bin/dash

# error checks for if there are enough args (and valid format)
if [ $# -ne 1 ]
then
    echo "Usage: $0 <num>" 1>&2
    exit 1
fi

num="$1"

# 
for i in $(seq 2 $((num / 2)))
do
    # echo $i
    if [ $((num % i)) -eq 0 ]
    then
        echo "$num is not prime"
        exit 1
    fi 
done

echo "$num is prime"
# default exit value is 0

