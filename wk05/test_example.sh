#/bin/dash

# an example of a _very_ simple test 

# initialise the repository
./pushy-init

# check that the directory exists
if ![ -e '.pushy' ]
then
    echo "Error: .pushy not created" 1>&2
    exit 1

exit 0