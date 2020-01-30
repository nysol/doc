#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,caabaa
2,acabaaa
3,
4,cbcbcc
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Records that contain the regular expression starting with \verb|c| until \verb|aa| includes \verb|id=1,id=2|. The function returns true for matching records.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexs($s{str},"c.*aa")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Match start of string"
comment=<<'EOF'
The regular expression \verb|.*c| which matches the value in the $str$ column for all records except \verb|id=3|.
EOF
scp=<<'EOF'
mcal c='regexs($s{str},".*c")' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


