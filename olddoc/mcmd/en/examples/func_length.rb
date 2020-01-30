#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,abc
2,3.1415
3,
4,hello world!
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
EOF
scp=<<'EOF'
more dat1.csv
mcal c='length($s{str})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Include multibyte character"
comment=<<'EOF'
The following example uses Japanese in UTF-8 encoding. Each UTF-8 Japanese character is encoded in 3 bytes, thus, the length function returns the number of bytes rather than the number of Japanese characters.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='length($s{str})' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Initialize wide character"
comment=<<'EOF'
The \verb|lengthw| function converts each wide characters internally into multibyte character for computation.
EOF
scp=<<'EOF'
mcal c='lengthw($s{str})' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

