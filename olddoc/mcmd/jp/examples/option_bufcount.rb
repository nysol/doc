#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat.csv","w"){|fpw| fpw.write(
<<'EOF'
id
a
b
EOF
)}

File.open("ref.csv","w"){|fpw| fpw.write(
<<'EOF'
id,name
a,A
b,B
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
参照ファイルのキーサイズが80MB(4MB×20)以内であれば、一時ファイルは使われない。
EOF
scp=<<'EOF'
mnjoin k=id m=ref.csv f=name i=dat.csv o=rsl.csv bufcount=20
EOF
run(scp,title,comment)

