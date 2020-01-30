#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,a b
2,ab	c
3,ab　c
4,
5,"aa
bb"
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|str|項目に空白類文字列が含まれていれば真を返す。
\verb|id=1|の行は半角スペース文字が含まれ、
\verb|id=2|の行はtab文字が含まれ、
そして\verb|id=4|の行は改行文字が含まれているために真となっている。
ここで、\verb|id=3|の行は全角スペースのため、検知できていない。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='hasspace($s{str})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="マルチバイト文字"
comment=<<'EOF'
hasspacew関数を使えば全角スペースも正しく検知できる。
EOF
scp=<<'EOF'
mcal c='hasspacew($s{str})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

