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
Find out the prefix of the longest substring that matches with the regular expression \verb|c.*a|. For example, in record \verb|id=4|, the function matches \verb|cabbca| in the  column and returns the prefix \verb|ba|. Since the same input data and substring are used in the \verb|regexstr,regexpfx| function, it is easy to compare the results.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexpfx($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

