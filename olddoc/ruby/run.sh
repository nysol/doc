#!/bin/bash

rm -rf ./outdat
mkdir -p ./outdat
#p=/usr/local/bin/

#RFLAG="-I/Users/hamuro/kgmod/jindoji/ruby -d -w"
#RFLAG="-I/Users/hamuro/kgmod/jindoji/ruby"

#${p}ruby -r profile $RFLAG test.rb 2>&1 | tee out_endlog.txt
${p}ruby $RFLAG test.rb

clear
./check.sh

