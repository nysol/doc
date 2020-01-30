#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,5
A,2,20
B,1,15
B,,10
B,5,20
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「顧客」項目を単位に「数量」と「金額」項目の平均値を計算し、「数量平均」と「金額平均」という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
mavg k=顧客 f=数量:数量平均,金額:金額平均 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="NULL値がある場合の出力"
comment=<<'EOF'
「顧客」項目を単位に「数量」と「金額」項目の平均値を計算し、「数量平均」と「金額平均」という項目名で出力する。
\verb|-n|オプションを指定することで、NULL値が含まれている場合は、結果もNULL値として出力する。
EOF
scp=<<'EOF'
mavg k=顧客 f=数量:数量平均,金額:金額平均 -n i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="顧客項目を単位としない例"
comment=<<'EOF'
「数量」と「金額」項目の平均値を計算し、「数量平均」と「金額平均」という項目名で出力する。
EOF
scp=<<'EOF'
mavg f=数量:数量平均,金額:金額平均 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
