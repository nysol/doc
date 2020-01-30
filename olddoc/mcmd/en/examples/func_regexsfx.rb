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
Extract the suffix of the longest substring that matches the regular expression \verb|c.*a|. For example, in row where \verb|id=4|, the regular expression matches \verb|cabbca| till the ending position in the  column, there is no suffix to the matching string, thus NULL character is returned.
Since the same input data and substring are used as in the \verb|regexstr,regexpfx| function, it is easy to compare the results and understand the differences.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexsfx($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

