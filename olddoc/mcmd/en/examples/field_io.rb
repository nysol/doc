#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
brand,quantity
A,10
B,20
C,30
D,40
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
By specifying "quantity:unit sales", the field name is converted from “quantity” to “unit sales” in the output.
EOF
scp=<<'EOF'
more dat1.csv
mcut f=brand,quantity:salesquantity i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Add field name"
comment=<<'EOF'
The maccum command accumulates the values in the "quantity" field, and add the field name "cumulative quantity" in the output results. If the parameter is specified as "f=quantity", the field name of the cumulative result will remain as "quantity", thus results in error because the same field name “quantity” exists in the output. 
EOF
scp=<<'EOF'
maccum f=quantity:accumulationquantity i=dat1.csv o=rsl2.csv
more rsl2.csv
maccum f=quantity i=dat1.csv o=rsl2.csv
EOF
run(scp,title,comment)

############## Example3
title="Mixing field name and field number"
comment=<<'EOF'
The field name and field number can be specified at the same time.
EOF
scp=<<'EOF'
mcut f=0,1:salesquantity -x i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

