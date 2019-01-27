#!/bin/sh

min=$1
max=$2
for (( i=$min; i < $max; i=i+1000 ))
do
	if [ "$(($i+1000))" -le $max ]
	then 
		Maxi=$(($i+1000))
	else
		Maxi=$max
	fi
	echo "Start from $i"
    nodejs scriptWithProxy.js $i $Maxi
done
