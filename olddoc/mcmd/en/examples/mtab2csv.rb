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



############## 例1 基本例
title="Example 1: Basic example"
comment=<<'EOF'
TSV data is converted into CSV data.
EOF
scp=<<'EOF'
more dat1.tab
mtab2csv i=dat1.tab o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2 d=指定
title="Example 2: Specifying d="
comment=<<'EOF'
The \verb|d=| parameter is specified to use a delimiter other than the tab.
EOF
scp=<<'EOF'
more dat2.bar
mtab2csv d=- i=dat2.bar o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
