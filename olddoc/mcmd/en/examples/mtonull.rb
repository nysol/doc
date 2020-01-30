#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,quantity,price
A,0,1
B,1,0
C,2,200
D,3,0
E,0,298
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,price
fruit:apple,100
fruit:peach,250
fruit:grape,300
fruit:pineapple,450
fruit:orange,500
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Replace 0 with NULL value in columns \verb|quantity| and \verb|price|.
EOF
scp=<<'EOF'
more dat1.csv
mtonull f=quantity,price v=0 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Replace a specified number with NULL value"
comment=<<'EOF'
Replace 0 or 1 with NULL value in columns \verb|quantity| and \verb|price|.
EOF
scp=<<'EOF'
mtonull f=quantity,price v=0,1 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Substitute substring match"
comment=<<'EOF'
Replace with a NULL value where \verb|quantity| and \verb|price| columns contain 0.
EOF
scp=<<'EOF'
mtonull -sub f=quantity,price v=0 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Substitute character string"
comment=<<'EOF'
Replace the string in the \verb|item| field that matches character string \verb|apple, orange, pineapple| with NULL value.
EOF
scp=<<'EOF'
more dat2.csv
mtonull f=item v=apple,orange,pineapple -sub i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
