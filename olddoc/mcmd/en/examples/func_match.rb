#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,f1,f2,f3
1,1,1,1
2,1,0,1
3,,,
4,1,,1
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,s1,s2,s3
1,ab,abx,x
2,abc,xaby,xxab
3,,,
4,#ac,x,x
EOF
)}


############## Example 1
title="OR exact match"
comment=<<'EOF'
Returns true if either column \verb|f1,f2,f3| contains \verb|1|.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='match("1",$s{f1},$s{f2},$s{f3})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="AND exact match"
comment=<<'EOF'
Returns true if columns \verb|f1,f2,f3| contains the character \verb|"1"|.
EOF
scp=<<'EOF'
mcal c='matcha("1",$s{f1},$s{f2},$s{f3})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="OR partial match"
comment=<<'EOF'
Returns true if the character string \verb|ab| exists in either column \verb|s1,s2,s3|.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='matchs("ab",$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="AND partial match"
comment=<<'EOF'
Returns true if the character string \verb|ab| exists in columns \verb|s1,s2,s3|.
EOF
scp=<<'EOF'
mcal c='matchas("ab",$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Search for NULL value"
comment=<<'EOF'
Return true if \verb|str| column contains NULL value.
EOF
scp=<<'EOF'
mcal c='match(nulls(),$s{s1},$s{s2},$s{s3})' a=rsl i=dat2.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

