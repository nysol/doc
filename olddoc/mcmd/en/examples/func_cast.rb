#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
1
2
3
4
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,v1,v2,v3
1,10,5,7
2,5,12,11
3,3,6,2
4,14,16,11
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,10
2,0
3,-5
4,0
EOF
)}


############## Example 1
title="Fixed length random number"
comment=<<'EOF'
Generate random numbers from 1 to 9999 as 4 digit fixed length string.
Integer data (results of randi) is not supported by \verb|fixlen| function, thus the data must be converted to character string with n2s function. 
EOF
scp=<<'EOF'
more dat1.csv
mcal c='fixlen(n2s(randi(1,9999,11)),4,"R","0")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="True false pattern"
comment=<<'EOF'
Detect unusual pattern in columns v1,v2,v3 and print as 01 in output.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='cat("",b2s(${v1}>=10),b2s(${v2}>=10),b2s(${v3}>=10))' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

