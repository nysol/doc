#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abcdefg
2,12345678
3,
4,12
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,あいうえお
2,1あ2345678
3,1あ
4,ああ
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
str項目の先頭から3文字を切り出す。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='left($s{str},3)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="マルチバイト文字を含む例"
comment=<<'EOF'
マルチバイト文字を含む場合はleftwを使う。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='leftw($s{str},3)' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

