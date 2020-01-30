#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
A
B
C
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
精算日という新しい項目を追加する。
EOF
scp=<<'EOF'
more dat1.csv
msetstr v=20070101 a=精算日 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="複数項目を追加"
comment=<<'EOF'
id項目のデータ\verb|A,B,C|の2つの組合わせを2つの項目(id1,id2)として出力する。
EOF
scp=<<'EOF'
mcombi f=id n=2 a=id1,id2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

