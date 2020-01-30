#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,item
1,01
2,02
3,03
4,04
5,05
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,item
1,0111
2,0121
3,0231
4,0241
5,0151
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,city
1,奈良市
2,下市町
3,十津川村
4,五條市
5,山添村
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|item|の値が
\verb|"01"|を\verb|"A"|に、
\verb|"03"|を\verb|"B"|に、
\verb|"04"|を\verb|"C"|に置換する。
その他はNULL値として出力する。
EOF
scp=<<'EOF'
more dat1.csv
mchgstr f=item c=01:A,03:B,05:C i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="条件に合致しない値を置換する文字列の指定"
comment=<<'EOF'
\verb|O=|パラメータを指定することで、
置換条件に合致しない場合は\verb|"out of range"|という文字列に置換して出力する。
EOF
scp=<<'EOF'
mchgstr f=item c=01:A,03:B,05:C O="out of range" i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="新しい項目として出力"
comment=<<'EOF'
\verb|-A|オプションを付けることで、新しい項目(\verb|item info|)として出力する。
EOF
scp=<<'EOF'
mchgstr f=item:"item info" c=01:A,03:B,05:C O="out of range" -A i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="条件外を項目の値として出力"
comment=<<'EOF'
\verb|-F|オプションを付けることで、
置換条件に合致しない場合は、元の値をそのまま出力する。
EOF
scp=<<'EOF'
mchgstr f=item c=01:A,03:B,05:C -F i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="条件を部分文字列マッチで置換"
comment=<<'EOF'
\verb|-sub|オプションをつけることで、部分文字列の置換となる。
以下の例では、\verb|item|項目に文字列\verb|"01"|が含まれていれば、それを\verb|"A"|に置換する。
EOF
scp=<<'EOF'
more dat2.csv
mchgstr f=item c=01:A -sub i=dat2.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## 例6
title="ワイド文字での部分文字列マッチ"
comment=<<'EOF'
ワイド文字の部分文字列置換をする場合は\verb|-W|オプションを用いる。
ただし、UTF-8エンコーディングを用いているのであれば\verb|-W|をつけなくても正しく動作する。
詳しくは「\hyperref[sect:multibyte]{マルチバイト文字}」の節を参照されたい。
EOF
scp=<<'EOF'
more dat3.csv
mchgstr f=city c=市:01,町:02,村:02 -sub -W i=dat3.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)
