#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val1,val2
1,12,36
2,6,5
3,,
4,12.1,36.2
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='gcd(${val1},${val2})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="定数を与える例"
comment=<<'EOF'
val1項目と36の最大公約数を求める。
EOF
scp=<<'EOF'
mcal c='gcd(${val1},36)' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

