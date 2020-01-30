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

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str
1,漢漢あbbbいyy
2,漢あbいいy
3,
4,bあいあbbいあ
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Find out the position of the longest substring that matches the regular expression \verb|c.*a|. Note that the first character starts at position 0. Since the same input data and substring are used in the \verb|regexstr| function, it is easy to compare the results and understand the differences.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexpos($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Multibyte character"
comment=<<'EOF'
Find out the longest substring that matches the regular expression \verb|"い.*あ"|. However, since regexpos does not support multibyte characters, the function returns the position of bytes instead of characters.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='regexpos($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Multibyte character 2"
comment=<<'EOF'
Find out the longest substring that matches the regular expression \verb|"い.*あ"|. The regexposw function is able to process multibyte characters accurately.
EOF
scp=<<'EOF'
mcal c='regexposw($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

