#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abc
2,123
3,
4,1234567
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,こんにちは
2,大阪
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Convert values in the \verb|str| column to 5 character fixed-length string. Right justified (\verb|"R"|) the strings and fill the empty positions with \verb|"#"| for strings with less than 5 characters.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='fixlen($s{str},5,"R","#")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Left justified"
comment=<<'EOF'
Fill empty positions for left justified (\verb|"L"|) text with \verb|"#"|.
EOF
scp=<<'EOF'
mcal c='fixlen($s{str},5,"L","#")' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Multibyte string"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='fixlenw($s{str},4,"R","埋")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

