#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abc
2,123
3,
4,1234567
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,こんにちは
2,大阪
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
str項目を5文字の固定長文字列に変換する。
5文字に満たない文字列は右詰(\verb|"R"|)で\verb|"#"|を埋める。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='fixlen($s{str},5,"R","#")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="左詰め例"
comment=<<'EOF'
左詰(\verb|"L"|)で\verb|"#"|を埋める。
EOF
scp=<<'EOF'
mcal c='fixlen($s{str},5,"L","#")' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="マルチバイト文字を含む場合"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='fixlenw($s{str},4,"R","埋")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

