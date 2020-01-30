#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,data
A,1 10 2
A,2 20 3
B,1 15 5
B,3 10 4
B,1 20 6
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,data
A,1 10 2
A,2 20 3
B,1 15 5
B,3 4
B,1
EOF
)}


File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,data
A,1_10_3
A,2_20_5
B,1_15_6
B,3_10_7
B,1_20_8
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
 半角スペースで分割
EOF
scp=<<'EOF'
more dat1.csv
msplit f=data a=d1,d2,d3 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="-r利用"
comment=<<'EOF'
\verb|-r|を指定することで、\verb|f=|で項目を削除できる。
EOF
scp=<<'EOF'
msplit f=data a=d1,d2,d3 -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="分割数不一致"
comment=<<'EOF'
\verb|a=|で指定した項目数よりも分割できる項目数が少ない場合は、NULLが追加され、
多い場合、先頭から指定した分割数まで出力する
EOF
scp=<<'EOF'
more dat2.csv
msplit f=data a=d1,d2 i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="delim指定"
comment=<<'EOF'
\verb|delim=|を使用して半角スペース以外の文字で分割する
EOF
scp=<<'EOF'
more dat3.csv
msplit f=data a=d1,d2,d3 delim=_ i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

