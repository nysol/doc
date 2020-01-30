#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,str1,str2,str3
1,abc,def,ghi
2,A,,CDE
3,,,
4,,,XY
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Concatenate 3 columns \verb|str1,str2,str3| with the inclusion of \verb|"#"| as delimiter token in between characters.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='cat("#",$s{str1},$s{str2},$s{str3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Empty token"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='cat("",$s{str1},$s{str2},$s{str3})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


############## Example 3
title="Example using wildcard"
comment=<<'EOF'
Use wildcard to specify columns names that start with \verb|str| (\verb|str1,str2,str3|) such as \verb|str*|.
EOF
scp=<<'EOF'
mcal c='cat("",$s{str*})' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

