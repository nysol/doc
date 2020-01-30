#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
ブランド,数量
A,10
B,20
C,30
D,40
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
「数量：売上数量」の指定により、項目名が「数量」から「売上数量」に変換されて出力される。
EOF
scp=<<'EOF'
more dat1.csv
mcut f=ブランド,数量:売上数量 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="追加項目名"
comment=<<'EOF'
以下のmaccumコマンドでは、「ブランド」項目で並べ替えた後、
「数量」項目の値を累積し、「累積数量」項目として追加出力する。
もし、「f=数量」とだけすれば、累積結果も「数量」という名の項目となり、
オリジナルの「数量」項目とダブってしまいエラーとなる。
EOF
scp=<<'EOF'
maccum s=ブランド f=数量:累積数量 i=dat1.csv o=rsl2.csv
more rsl2.csv
maccum s=ブランド f=数量 i=dat1.csv o=rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="番号指定との混在"
comment=<<'EOF'
番号指定と出力項目名指定を混在させることも可能である。
EOF
scp=<<'EOF'
mcut f=0,1:売上数量 -x i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

