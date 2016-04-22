#!/bin/bash
echo "λ"
echo "---"

if [ "$1" = 'open' ]; then
	/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl ~/Code/BitBar/status.sh
fi

serv_status ()
{
	ping -c 1 $1 &>-
	STATUS=$(echo $?)
	if [[ $STATUS == 0 ]] ; then
		echo $1 online!
	else
		echo No Connection to $1!
	fi
}

serv_status sarick.tech
serv_status github.com
serv_status gitlab.com
serv_status 93.174.95.27
echo "Edit servers | bash=$0 param1=open terminal=false"