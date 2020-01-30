#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,caabaa
2,acabaaa
3,
4,cbcbcc
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|id=1,id=2|の$str$項目にマッチした部分文字列を\verb|MMM|に置換する。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexrep($s{str},"c.*aa","MMM")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

