#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,a b
2,ab	c
3,ab　c
4,
5,"aa
bb"
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Returns true if \verb|str| column contains white space characters. The first row where \verb|id=1|contains single-byte space character, in addition, the second row where \verb|id=2| contains tab character, thus, these two rows return true. However, records where the function returns false are \verb|id=4| which contains carriage return, and \verb|id=3| which contains double-byte space character.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='hasspace($s{str})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Multibyte character"
comment=<<'EOF'
Use \verb|hasspacew| function to detect double character space.
EOF
scp=<<'EOF'
mcal c='hasspacew($s{str})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

