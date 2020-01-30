#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,zipCode
A,6230041
B,6240053
C,6330032
D,6230087
E,6530095
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,price
fruit:apple,100
fruit:peach,250
fruit:pineapple,300
fruit:orange,450
fruit:grapefruit,500
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
str1
abc
abbc
ac
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|zipCode|項目の値が00から始まる4桁文字列を\verb|####|に置換する。
EOF
scp=<<'EOF'
more dat1.csv
msed f=zipCode c=00.. v=#### i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="項目名指定"
comment=<<'EOF'
\verb|zipCode|の値が00から始まる4桁の数字を\verb|####|に置換し、\verb|zipCode4|という項目名で出力する。
EOF
scp=<<'EOF'
msed f=zipCode:zipCode4 c='00\d\d' v=#### i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="グローバル置換"
comment=<<'EOF'
\verb|zipCode|の値が\verb|0|を全て\verb|-|にグローバル置換する。
EOF
scp=<<'EOF'
msed f=zipCode c=0 v=- -g i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="部分置換"
comment=<<'EOF'
\verb|item|の先頭の\verb|fruit|を削除する。
先頭一致(\verb|^|)を指定しているので、最後の行の\verb|grapefruit|は削除されていないことに注意する。
EOF
scp=<<'EOF'
more dat2.csv
msed f=item c='^fruit' v= -g i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="マッチ結果を用いた置換"
comment=<<'EOF'
\verb|v=|の中で\verb|$&|を用いれば、マッチした文字列(連続した\verb|b|)に置き換わる。
EOF
scp=<<'EOF'
more dat3.csv
msed f=str1 c='b+' v='#$&#' i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## 例6
title="グローバルマッチとの組み合せ"
comment=<<'EOF'
グローバルマッチにすると、個々のマッチ毎に\verb|v=|の内容が評価される。
EOF
scp=<<'EOF'
msed f=str1 c=b v='#$&#' -g i=dat3.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)

############## 例7
title="プレフィックス置換"
comment=<<'EOF'
\verb|$`|にて、マッチした箇所の前の文字列(プレフィックス)に置換される。
EOF
scp=<<'EOF'
msed f=str1 c=b v='#$`#' i=dat3.csv o=rsl7.csv
more rsl7.csv
EOF
run(scp,title,comment)

############## 例8
title="サフィックス置換"
comment=<<'EOF'
\verb|$'|にて、マッチした箇所の後の文字列(サフィックス)に置換される。
EOF
scp=<<'EOF'
msed f=str1 c=b v="#$'#" i=dat3.csv o=rsl8.csv
more rsl8.csv
EOF
run(scp,title,comment)
