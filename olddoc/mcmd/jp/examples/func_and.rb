#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,b1,b2,b3
1,1,0,1
2,1,1,1
3,1,,1
4,1,1,1
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='and($b{b1},$b{b2},$b{b3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="ワイルドカードを利用した例"
comment=<<'EOF'
\verb|b|から始まる項目(\verb|b1,b2,b3|)をワイルドカード「\verb|b*|」によって指定している。
EOF
scp=<<'EOF'
mcal c='and($b{b*})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

