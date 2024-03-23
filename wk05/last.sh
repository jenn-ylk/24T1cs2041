#! /bin/dash

unsw_conns=0

z0=0
z1=1
z2=0
z3=0
z4=0
z5=0
z6=0
z7=0
z8=0
z9=0

#for line in $(cat logins)
while read -r zid _ connection datetime
do
    case "$connection" in
    uniwide*)
        unsw_conns=$((unsw_conns + 1));;
    esac

    case "$zid" in
        z0*) z0=$((z0 + 1));;
        z1*) z1=$((z1 + 1));;
        z2*) z2=$((z2 + 1));;
        z3*) z3=$((z3 + 1));;
        z4*) z4=$((z4 + 1));;
        z5*) z5=$((z5 + 1));;
        z6*) z6=$((z6 + 1));;
        z7*) z7=$((z7 + 1));;
        z8*) z8=$((z8 + 1));;
        z9*) z9=$((z9 + 1));;
    esac
    echo "$zid"
done

echo "$unsw_conns connections from UNSW"

echo "$z5 zIDs starting with 5"

