#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity,Amount
A,1,
B,,15
A,2,20
B,3,10
B,1,20
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Calculate the total \verb|Quantity| and total \verb|Amount| for each \verb|Customer| using the hash function.
EOF
scp=<<'EOF'
more dat1.csv
mhashsum k=Customer f=Quantity,Amount i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="NULL value in output"
comment=<<'EOF'
The output returns NULL if NULL value is present in \verb|Quantity| and \verb|Amount|. Use \verb|-n| option to print the null value.
EOF
scp=<<'EOF'
mhashsum k=Customer f=Quantity,Amount -n i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
