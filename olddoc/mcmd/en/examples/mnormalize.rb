#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity,amount
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Normalize (z score) \verb|quantity| and \verb|amount| field based on each \verb|customer|, label the column names of the output as \verb|qtyNominal| and \verb|amtNorminal| respectively.
EOF
scp=<<'EOF'
more dat1.csv
mnormalize c=z k=customer f=quantity:qtyNominal,amount:amtNorminal i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Deviation value"
comment=<<'EOF'
EOF
scp=<<'EOF'
mnormalize c=Z k=customer f=quantity:qtyNominal,amount:amtNorminal i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Linear transformation from 0 to 1"
comment=<<'EOF'
EOF
scp=<<'EOF'
mnormalize c=range k=customer f=quantity:qtyNominal,amount:amtNorminal i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
