#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
ブランド,数量10,数量11,数量12,数量123
A,10,15,9,1
B,20,16,8,2
C,30,17,7,3
D,40,18,6,4
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
A,10,15,9,1
B,20,16,8,2
C,30,17,7,3
D,40,18,6,4
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「数量*」にて、「数量」で始まる項目名(「数量10」、「数量11」、「数量12」、「数量123」)にマッチする。
EOF
scp=<<'EOF'
more dat1.csv
mcut f=数量* i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="?のワイルドカード"
comment=<<'EOF'
「数量」で始まる項目名のうち、1からはじまる任意の1文字にマッチする項目名が選択される。
「数量123」にはマッチしない。
EOF
scp=<<'EOF'
mcut f=数量1? i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

