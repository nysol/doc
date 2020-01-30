#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,egg,milk
A,1,1
B,,1
C,1,
D,1,1
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|egg|と\verb|milk|項目の値がNULL値以外なら、それら項目名を要素としたベクトルを作成する。
EOF
scp=<<'EOF'
more dat1.csv
mtraflg f=egg,milk a=transaction i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例2"
comment=<<'EOF'
出力された結果を\verb|-r|をつけて再実行し元に戻す。
EOF
scp=<<'EOF'
mtraflg -r f=egg,milk a=transaction i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="区切り文字の指定"
comment=<<'EOF'
区切り文字を-(ハイフン）で連結し、\verb|transaction|という項目名で出力する。
EOF
scp=<<'EOF'
mtraflg f=egg,milk a=transaction delim=- i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
