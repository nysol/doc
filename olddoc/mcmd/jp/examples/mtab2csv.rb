#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.tab","w"){|fpw| fpw.write(
<<'EOF'
id	data	data2
A	1102	a
A	2203	aaa
B	1155	bbbb
B	3104	c
B	1206	de
EOF
)}

File.open("dat2.bar","w"){|fpw| fpw.write(
<<'EOF'
id-data-data2
A-1102-a
A-2203-aaa
B-1155-bbbb
B-3104-c
B-1206-de
EOF
)}



############## 例1
title="基本例"
comment=<<'EOF'
 タブ区切りデータをcsvへ変換
EOF
scp=<<'EOF'
more dat1.tab
mtab2csv i=dat1.tab o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="d=指定"
comment=<<'EOF'
\verb|d=|を使用してtab以外の区切り文字を使う
EOF
scp=<<'EOF'
more dat2.bar
mtab2csv d=- i=dat2.bar o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)




