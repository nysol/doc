#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,dob
1,19641010
2,20000101
3,
4,19770812
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Compute the age from date of birth to a fixed point on calendar on September 1, 2013.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='age($d{dob},0d20130901)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

