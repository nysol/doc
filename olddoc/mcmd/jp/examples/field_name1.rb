#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
key,val
a,2
b,5
b,4
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
a,2
b,5
b,4
EOF
)}

############## 例1
title="-nfn指定"
comment=<<'EOF'
\verb|-nfn|(no field names)を指定すると，先頭行を項目名行と見なさない。
そして項目は必ず番号で指定する(番号は0から始まることに注意する)。
EOF
scp=<<'EOF'
more dat2.csv
msum -nfn k=0 f=1 i=dat2.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="-nfno指定"
comment=<<'EOF'
\verb|-nfno|(no field names for output)を指定すると，入力データの先頭行は項目名行として扱うが，出力データには項目名を出力しない．
EOF
scp=<<'EOF'
more dat1.csv
msum k=key f=val -nfno i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="-nfni指定"
comment=<<'EOF'
\verb|-nfni|(no field name for input)の指定はmcutでのみ可能であるオプションである．
このオプションは-nfnoと逆の働きをする．
すなわち，入力データの先頭行は項目名行として扱わないが，
出力データには項目名を出力する．
よって、入力項目番号に続けて出力項目名を":"に続けて指定する必要がある．
EOF
scp=<<'EOF'
mcut f=0:key,1:val -nfni i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4
title="-x指定"
comment=<<'EOF'
項目名行があるCSVデータに対して、項目番号で指定したい場合は\verb|-x|オプションを利用する。
EOF
scp=<<'EOF'
msum -x k=0 f=1 i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

