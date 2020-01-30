#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
brand,quantity10,quantity11,quantity12,quantity123
A,10,15,9,1
B,20,16,8,2
C,30,17,7,3
D,40,18,6,4
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
A,10,15,9,1
B,20,16,8,2
C,30,17,7,3
D,40,18,6,4
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
The expression "quantity*" matches field names starting with quantity ("quantity10", "quantity11", "quantity12" and "quantity123").  
EOF
scp=<<'EOF'
more dat1.csv
mcut f= quantity* i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Wildcard character “?”"
comment=<<'EOF'
Select field names which begin with "quantity" followed by 1, and match any single character after 1. In this case, the wildcard does not match with field name “quantity123”. 
EOF
scp=<<'EOF'
mcut f= quantity 1? i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

