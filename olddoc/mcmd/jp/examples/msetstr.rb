#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
顧客,日付
A,20081202
A,20081204
B,20081203
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
日付計算で必要となる基準日を(2007年01月01日と定義した場合)すべての行に「\verb|20070101|」という文字列を追加し「基準日」という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
msetstr v=20070101 a=基準日 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="複数項目を追加"
comment=<<'EOF'
EOF
scp=<<'EOF'
msetstr v=20070101,20070201 a=基準日1,基準日2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="null値項目追加"
comment=<<'EOF'
EOF
scp=<<'EOF'
msetstr v= a=追加項目 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
