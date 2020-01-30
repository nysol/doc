#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val1,val2
A,1,2
B,2,3
C,3,4
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
項目\verb|val1|と\verb|val2|を切り出す。
EOF
scp=<<'EOF'
more dat1.csv
mcut f=val1,val2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="出力項目名の指定"
comment=<<'EOF'
\verb|val1,val2|を集計し、\verb|sum1,sum2|という項目名で出力する。
EOF
scp=<<'EOF'
msum f=val1:sum1,val2:sum2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

