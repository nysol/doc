#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,price,quantity
A,198,1
B,325,2
C,200,3
D,450,2
E,100,1
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,price,quantity
A,198,1
B,,2
C,200,
D,450,2
E,,
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
\verb|price|と\verb|quantity|項目を1つの文字列として連結し、
\verb|transaction|という項目名で出力する。
EOF
scp=<<'EOF'
more dat1.csv
mtrafld a=transaction f=price,quantity i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="基本例2"
comment=<<'EOF'
出力された結果を\verb|-r|をつけて再実行し元に戻す。
EOF
scp=<<'EOF'
mtrafld -r a=transaction f=price,quantity i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="区切り文字の指定"
comment=<<'EOF'
\verb|price|と数量\verb|quantity|項目を\_(アンダーバー）で区切り1つの文字列として連結し、
項目名とデータは：（コロン）で区切り\verb|transaction|という項目名で出力する。
EOF
scp=<<'EOF'
mtrafld a=transaction f=price,quantity delim=_ delim2=':' i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="NULL値を含む場合"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mtrafld a=transaction f=price,quantity i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="NULL値を含む場合2"
comment=<<'EOF'
出力された結果を\verb|-r|をつけて再実行し元に戻す。
EOF
scp=<<'EOF'
mtrafld -r a=transaction f=price,quantity i=rsl4.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## 例6
title="-valOnlyの指定"
comment=<<'EOF'
EOF
scp=<<'EOF'
mtrafld -valOnly f=price,quantity a=transaction i=dat2.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)
