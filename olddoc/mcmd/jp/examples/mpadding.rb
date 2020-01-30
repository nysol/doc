#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
no
3
6
8
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
date,dummy
20130929,a
20131002,b
20131004,c
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
\verb|no|項目が整数(\%n)として連続するようにレコードをパディングする。
\verb|1|とverb|4|の間に\verb|2,3|を、\verb|4|と\verb|2|の間に\verb|3|が挿入されている。
EOF
scp=<<'EOF'
more dat1.csv
mpadding f=no%n i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="開始値、終了値の指定"
comment=<<'EOF'
行間のパディングだけでなく、先頭行/終端行の前後もパディングする。
前後の範囲は\verb|S=,E=|で指定する。
EOF
scp=<<'EOF'
mpadding f=no%n S=1 E=10 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## 例3
title="日付パディング"
comment=<<'EOF'
\verb|date|項目が日付(\%d)として連続するようにレコードをパディングする。
\verb|k=,f=|で指定した以外の項目は、直前の行の項目値でパディングする。
EOF
scp=<<'EOF'
more dat2.csv
mpadding f=date%d i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="パディング用文字列指定"
comment=<<'EOF'
\verb|v=|にてパディング文字列を指定することもできる。
EOF
scp=<<'EOF'
mpadding f=date%d v=padding i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## 例5
title="パディングにNULL値を指定"
comment=<<'EOF'
\verb|-n|を指定してNULL値でパディングすることも可能。
EOF
scp=<<'EOF'
mpadding f=date%d -n i=dat2.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

