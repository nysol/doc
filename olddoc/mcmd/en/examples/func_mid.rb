#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abcdefg
2,12345678
3,
4,12
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,あいうえお
2,1234567あ8
3,1あ
4,ああ
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Extract the first 3 characters from the beginning in the str column.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='mid($s{str},2,3)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Cases containing multibyte character"
comment=<<'EOF'
Use midw function if the string contains multibyte characters.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='midw($s{str},2,3)' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

