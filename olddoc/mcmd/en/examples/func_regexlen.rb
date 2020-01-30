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
Find out the length of the longest substring that matches with the regular expression \verb|c.*a|. Since the same input data is used for matching substring in the \verb|regexstr| function, it is easier to compare the results.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='regexlen($s{str},"c.*a")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Multibyte characters"
comment=<<'EOF'
Find out the length of the longest substring that matches \verb|"い.*あ"|. However, since regexlen function do not support multibyte character, it returns the number of bytes instead of number of characters.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='regexlen($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Multibyte characters 2"
comment=<<'EOF'
Find out the length of the longest substring that matches \verb|"い.*あ"|. The \verb|regexlenw| function is able to process multibyte characters to count the number of characters.
EOF
scp=<<'EOF'
mcal c='regexlenw($s{str},"あ.*い")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

