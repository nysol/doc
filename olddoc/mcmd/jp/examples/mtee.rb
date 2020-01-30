#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity,price
A,1,10
A,2,20
B,1,15
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|dat1.csv|ファイルを\verb|rsl1.csv|と\verb|rsl2.csv|という２つのファイルにコピーする。
また、標準出力に出力されるので、画面上に内容が出力される。
EOF
scp=<<'EOF'
more dat1.csv
mtee i=dat1.csv o=rsl1.csv,rsl2.csv
more rsl1.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例2
title="標準出力なし"
comment=<<'EOF'
\verb|-nostdout|を指定すると、\verb|rsl1.csv|と\verb|rsl2.csv|という２つのファイルにコピーのみ行い、
標準出力には出力しない。
EOF
scp=<<'EOF'
mtee i=dat1.csv o=rsl1.csv,rsl2,csv -nostdout
EOF
run(scp,title,comment)
