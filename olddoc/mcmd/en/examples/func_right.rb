#!/usr/bin/env ruby
# -*- encoding: utf-8 -*-
require "nysol/mcmd"
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
Extract the last 3 characters from the end in the \verb|str| column.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='right($s{str},3)' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Example of data containing multibyte characters"
comment=<<'EOF'
Use the function \verb|right| if the data contains multibyte characters.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='right($s{str},6)' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

