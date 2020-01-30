#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,xcbbbayy
2,xxcbaay
3,
4,bacabbca
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Extract the longest substring that matches the regular expression \verb|c.*a|. At row where \verb|id=2|, the regular expression matches the string \verb|cba| and \verb|cbaa|, however, the longer substring is returned.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexstr($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

