#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,v1,v2,v3
1,1,2,3
2,-5,2,1
3,1,,3
4,,,
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='sqsum(${v1},${v2},${v3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="ワイルドカードを利用した例"
comment=<<'EOF'
\verb|v|から始まる項目(\verb|v1,v2,v3|)をワイルドカード「\verb|v*|」によって指定している。
EOF
scp=<<'EOF'
mcal c='sqsum(${v*})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="-nを利用した例"
comment=<<'EOF'
\verb|v2|にNULL値を含む\verb|id=3|の行の結果もNULLとなる。
EOF
scp=<<'EOF'
mcal c='sqsum(${v1},${v2},${v3},"-n")' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

