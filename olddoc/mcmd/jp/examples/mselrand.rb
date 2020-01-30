#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,日付,金額
A,20081201,10
A,20081207,20
A,20081213,30
B,20081002,40
B,20081209,50
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,日付,金額
A,20081201,10
A,20081207,20
A,20081213,30
B,20081002,40
B,20081209,50
C,20081210,60
D,20081201,70
D,20081205,80
D,20081209,90
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
一人の顧客につきランダムに1行を選択する。
EOF
scp=<<'EOF'
more dat1.csv
mselrand k=顧客 c=1 S=1 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="ランダムに一定割合の行を選択"
comment=<<'EOF'
一人の顧客につきランダムに50\%の行を選択する。
また、それ以外の不一致データは\verb|oth2.csvと|いうファイルに出力する。
EOF
scp=<<'EOF'
mselrand k=顧客 p=50 S=1 u=oth2.csv i=dat1.csv o=rsl2.csv
more rsl2.csv
more oth2.csv
EOF
run(scp,title,comment)

############## 例3
title="キー単位の選択"
comment=<<'EOF'
以下の例は、顧客\verb|A,B,C,D|の4人からランダムに2人を選ぶ。
顧客\verb|D|が選ばれると、顧客\verb|D|の行は全て出力される。
EOF
scp=<<'EOF'
more dat2.csv
mselrand k=顧客 c=2 S=1 -B i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
