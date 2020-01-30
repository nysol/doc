#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,数量,金額
A,1,10
A,2,20
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|mcut|の実行結果は\verb|o=|で指定した\verb|rsl1.csv|に出力される。
EOF
scp=<<'EOF'
more dat1.csv
mcut f=顧客,金額 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="リダイレクト"
comment=<<'EOF'
標準出力をリダイレクト(\verb|">"|記号)して書き込む。
EOF
scp=<<'EOF'
mcut f=顧客,金額 i=dat1.csv >rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

