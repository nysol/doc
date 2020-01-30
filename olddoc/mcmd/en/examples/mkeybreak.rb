#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,k1,k2,val
1,A,a,1
2,A,b,2
3,A,b,3
4,B,a,4
5,B,a,5
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Sort the records by ¥verb|k1| field, add an indicator (\verb|1|) to the first record (\verb|top| field) and last record (\verb|bottom| field) where \verb|k1| is key field.
EOF
scp=<<'EOF'
more dat1.csv
mkeybreak k=k1 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="2 key fields"
comment=<<'EOF'
After fields \verb|k1| and \verb|k2| are sorted, the beginning of key field \verb|k1| (\verb|top|field) and end (\verb|bottom|field) is marked (\verb|1|).
EOF
scp=<<'EOF'
mkeybreak s=k1,k2 k=k1 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

