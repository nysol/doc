#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
B,5,20
B,2,10
C,1,15
C,3,10
C,1,21
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「顧客」項目を単位に「数量」と「金額」項目の
各統計量合計値を計算する。
EOF
scp=<<'EOF'
more dat1.csv
mstats k=顧客 f=数量,金額 c=sum i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例2"
comment=<<'EOF'
各統計量最大値を計算する。
EOF
scp=<<'EOF'
mstats k=顧客 f=数量,金額 c=max i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
