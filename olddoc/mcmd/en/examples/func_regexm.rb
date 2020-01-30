#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,caabaa
2,acabaaa
3,
4,bbcbcc
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Both records where \verb|id=1,id=2| contains regular expression beginning with \verb|c| and ends with \verb|aa|, in record \verb|id=2|, there is only partial match (matches from \verb|c| at the second position to the end) with the regular expression.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexm($s{str},"c.*aa")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="String ends with same substring"
comment=<<'EOF'
The full string in column $str$ that matches the regular expression \verb|.*c| is only found in the record where \verb|id=4|.
EOF
scp=<<'EOF'
mcal c='regexm($s{str},".*c")' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Match blank characters"
comment=<<'EOF'
Match the blank characters at \verb|id=3| using the regular expression \verb|^$|.
EOF
scp=<<'EOF'
mcal c='regexm($s{str},"^$")' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


