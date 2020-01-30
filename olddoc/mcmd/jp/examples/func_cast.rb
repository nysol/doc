#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
1
2
3
4
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,v1,v2,v3
1,10,5,7
2,5,12,11
3,3,6,2
4,14,16,11
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,10
2,0
3,-5
4,0
EOF
)}


############## 例1
title="乱数の固定長化"
comment=<<'EOF'
1から9999の整数乱数を発生させ、4桁固定長で出力する。
fixlen関数は整数型のデータ(ここではrandiの結果)には対応していないので、
n2s関数で文字列型に変換する必要がある。
EOF
scp=<<'EOF'
more dat1.csv
mcal c='fixlen(n2s(randi(1,9999,11)),4,"R","0")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="真偽パターン"
comment=<<'EOF'
項目v1,v2,v3が10異常かどうかを判定し、01のパターンを出力する。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='cat("",b2s(${v1}>=10),b2s(${v2}>=10),b2s(${v3}>=10))' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

