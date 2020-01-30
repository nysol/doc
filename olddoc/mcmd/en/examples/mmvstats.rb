#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,value
1,5
2,1
3,3
4,4
5,4
6,6
7,1
8,4
9,7
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Calculate sum of sliding window.
The first row is not printed as there is less than the required nubmer of intervals for computation.
EOF
scp=<<'EOF'
more dat1.csv
mmvstats s=id f=value t=2 c=sum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
