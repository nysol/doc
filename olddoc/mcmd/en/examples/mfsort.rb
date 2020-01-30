#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,v1,v2,v3
1,b,a,c
2,a,b,a
3,b,,e
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Arrange the values in \verb|v1,v2,v3| in ascending order for each record, and output the data items in sequential order corresponding to fields \verb|v1,v2,v3|.
EOF
scp=<<'EOF'
more dat1.csv
mfsort f=v* i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Descending Order"
comment=<<'EOF'
Add \verb|-r| to arrange in descending order.
EOF
scp=<<'EOF'
mfsort f=v* -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

