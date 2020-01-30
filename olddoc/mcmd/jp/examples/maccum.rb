#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,2,20
B,1,15
B,3,10
B,1,20
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,,20
B,1,15
B,3,
B,1,20
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「数量」と「金額」項目の累積値を計算し、「数量累計」と「金額累計」という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
maccum s=顧客 f=数量:数量累計,金額:金額累計 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="キー項目を指定する例"
comment=<<'EOF'
「顧客」項目を単位に「数量」と「金額」項目の累積値を計算し、「数量累計」と「金額累計」という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
maccum k=顧客 s=顧客 f=数量:数量累計,金額:金額累計 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="NULL値を含む累計"
comment=<<'EOF'
「数量」と「金額」項目の累積値を計算し、「数量累計」と「金額累計」という項目名で出力する。
NULLは無視される。結果もNULLが出力される。
EOF
scp=<<'EOF'
more dat2.csv
maccum s=顧客 f=数量:数量累計,金額:金額累計 i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
