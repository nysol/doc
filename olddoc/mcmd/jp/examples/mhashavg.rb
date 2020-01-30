#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,
B,,15
A,2,20
B,3,10
B,1,20
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「顧客」項目を単位にして、「数量」と「金額」項目の平均を計算する。
EOF
scp=<<'EOF'
more dat1.csv
mhashavg k=顧客 f=数量,金額 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="NULL値の出力"
comment=<<'EOF'
\verb|-n|オプションを指定することで、NULL値が含まれている場合は、結果もNULL値として出力する。
EOF
scp=<<'EOF'
mhashavg k=顧客 f=数量,金額 -n i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
