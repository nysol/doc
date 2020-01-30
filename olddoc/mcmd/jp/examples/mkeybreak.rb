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

############## 例1
title="基本例"
comment=<<'EOF'
\verb|k1|項目で並べ替えた後、\verb|k1|キー項目の先頭(\verb|top|項目)と終端(\verb|bottom|項目)に印(\verb|1|)をつける。
EOF
scp=<<'EOF'
more dat1.csv
mkeybreak k=k1 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="2項目キー"
comment=<<'EOF'
\verb|k1|・\verb|k2|項目で並べ替えた後、\verb|k1|キー項目の先頭(\verb|top|項目)と終端(\verb|bottom|項目)に印(\verb|1|)をつける。
EOF
scp=<<'EOF'
mkeybreak s=k1,k2 k=k1 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

