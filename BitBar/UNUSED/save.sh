#!/bin/bash
echo "G"
echo "---"

if [ "$1" = 'comm' ]; then
  cd /Users/Sir/Schoolwork_15-16/EE 
  /usr/bin/git add .
  /usr/bin/git commit -m "Done work on EE (auto save)"

elif [ "$1" = 'push' ]; then
  cd /Users/Sir/Schoolwork_15-16/EE 
  /usr/bin/git push
fi

echo "Add/Commit EE | bash=$0 param1=comm terminal=false"
echo "Push EE | bash=$0 param1=push terminal=false"