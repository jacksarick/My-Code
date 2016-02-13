#!/bin/bash
echo "λ"
echo "---"

serv_status ()
{
	ping -c 1 $1 &>-
	STATUS=$(echo $?)
	if [[ $STATUS == 0 ]] ; then
		echo $1 online!
	else
		echo No Connection!
	fi
}

serv_status sarick.tech
serv_status github.com