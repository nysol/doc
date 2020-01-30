#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity,price
A,1,10
A,2,20
B,1,15
EOF
)}

############## Example 1
title="Basic Examples"
comment=<<'EOF'
Copy \verb|dat1.csv| file to two files \verb|rsl1.csv| and \verb|rsl2.csv| In addition, display output on screen through standard output.
EOF
scp=<<'EOF'
more dat1.csv
mtee i=dat1.csv o=rsl1.csv,rsl2.csv
more rsl1.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 2
title="Do not print to standard output "
comment=<<'EOF'
When \verb|-nostdout| is specified, the command only copy the two files \verb|rsl1.csv| and \verb|rsl2.csv| but not to standard output.
EOF
scp=<<'EOF'
mtee i=dat1.csv o=rsl1.csv,rsl2,csv -nostdout
EOF
run(scp,title,comment)
