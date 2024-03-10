#! /bin/dash

# Q2 of Wk 4 Tutorial

# Check exit value of the last program using #?

hour=$(date +%H)

if [ $hour -ge 9 ] && [ $hour -lt 17 ]
then
    exit 0
fi

# if 17:00:00 is still "business"
minute=$(date +%M)
second=$(date +%S)
if [ $minute -eq 0 ] && [ $second -eq 0 ]
then
    exit 0
fi

exit 1
