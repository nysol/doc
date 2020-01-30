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
\verb|dat1.csv|を入力データとして\verb|mcut|は実行される。
EOF
scp=<<'EOF'
more dat1.csv
mcut f=顧客,金額 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="出力項目名の指定"
comment=<<'EOF'
標準入力をリダイレクト(\verb|"<"|記号)して読み込む。
EOF
scp=<<'EOF'
mcut f=顧客,金額 o=rsl2.csv <dat1.csv
more rsl2.csv
EOF
run(scp,title,comment)

