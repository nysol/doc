#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,quantity,price
A,20081201,1,10
A,20081202,2,20
A,20081203,3,30
B,20081201,4,40
B,20081203,5,50
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|item|項目を単位に\verb|date|項目を横に展開し、
\verb|quantity|項目を出力する。
EOF
scp=<<'EOF'
more dat1.csv
mcross k=item f=quantity s=date i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="元の入力データに戻す例"
comment=<<'EOF'
例1の出力結果を元に戻すには、同じく\verb|mcross|を以下のよう用いればよい。
EOF
scp=<<'EOF'
more rsl1.csv
mcross k=item f=2008* s=fld a=date i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例1
title="複数の値を出力"
comment=<<'EOF'
\verb|quantity,price|の2項目を出力する。
EOF
scp=<<'EOF'
mcross k=item f=quantity,price s=date i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


############## 例3
title="並びを逆順する例"
comment=<<'EOF'
横に展開する項目名の並びを逆順にする。
EOF
scp=<<'EOF'
mcross k=item f=quantity,price s=date%r i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
