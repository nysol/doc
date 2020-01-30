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
ここでは、\verb|"&"|が入力項目名である「\verb|ブランド|」に置換され、「\verb|f=ブランド:ブランドコード|」と指定したことと同等となる。
EOF
scp=<<'EOF'
more dat1.csv
mcut f="ブランド:&コード" i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="ワイルドカードとの併用"
comment=<<'EOF'
出力項目名指定における\verb|売上&|の\verb|&|が入力項目名(例えば「数量10」)に置き換わる。
結果として、「\verb|数量|」で始まる項目全てに対して「\verb|売上|」を先頭に加えて出力することになる。
EOF
scp=<<'EOF'
mcut f="ブランド,数量*:売上&" i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

