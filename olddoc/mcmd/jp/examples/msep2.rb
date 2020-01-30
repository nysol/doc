#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,no
A,1
A,1
A,2
B,1
B,2
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|item|項目別にデータを分割する。
出力ファイル名は0から始まる連番であり、どの番号がどのキーに対応しているかが\verb|table.csv|に出力される。
EOF
scp=<<'EOF'
more dat1.csv
msep2 k=item O=./output a=fileName o=table.csv i=dat1.csv
ls ./output
more table.csv
more output/0
more output/1
EOF
run(scp,title,comment)

############## 例2
title="複数キー項目"
comment=<<'EOF'
複数のキー項目\verb|item,no|を設定しても同様に各ファイル名は連番で作成される。
\verb|table.csv|に複数のキー項目と番号の対応表が出力されている。
EOF
scp=<<'EOF'
more dat1.csv
msep2 k=item,no O=./output2 a=fileName o=table.csv i=dat1.csv
ls ./output2
more table.csv
more output/0
EOF
run(scp,title,comment)
