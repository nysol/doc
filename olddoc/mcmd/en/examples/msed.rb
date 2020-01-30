#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,zipCode
A,6230041
B,6240053
C,6330032
D,6230087
E,6530095
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
item,price
fruit:apple,100
fruit:peach,250
fruit:pineapple,300
fruit:orange,450
fruit:grapefruit,500
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
str1
abc
abbc
ac
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Replace the 4-digit substring in the \verb|zipCode| field starting 00 with \verb|####|.
EOF
scp=<<'EOF'
more dat1.csv
msed f=zipCode c=00.. v=#### i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Specify field name"
comment=<<'EOF'
Replace the 4-digit substring in the \verb|zipCode| field starting 00 with \verb|####|. Save output in column \verb|zipCode4|.
EOF
scp=<<'EOF'
msed f=zipCode:zipCode4 c='00\d\d' v=#### i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Global replacement"
comment=<<'EOF'
Global search using the regular expression \verb|-| to replace value of \verb|0| in \verb|zipCode|.
EOF
scp=<<'EOF'
msed f=zipCode c=0 v=- -g i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Replace substring"
comment=<<'EOF'
Delete \verb|fruit| from the beginning of the string in \verb|item|. Note that when first match (\verb|^|) is specified, the substring within the word \verb|grapefruit| in the last row is retained.
EOF
scp=<<'EOF'
more dat2.csv
msed f=item c='^fruit' v= -g i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Substitution using match results"
comment=<<'EOF'
Replaced 1 or more consecutive character strings of \verb|b| using \verb|$&| is defined in the \verb|v=|.
EOF
scp=<<'EOF'
more dat3.csv
msed f=str1 c='b+' v='#$&#' i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## Example 6
title="Combination of the global match"
comment=<<'EOF'
When performing a global match, each match is evaluated against the contents defined at \verb|v=|.
EOF
scp=<<'EOF'
msed f=str1 c=b v='#$&#' -g i=dat3.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)

############## Example 7
title="Prefix substitution"
comment=<<'EOF'
Replace the matching first character of b in the character string (prefix) using \verb|$`|.
EOF
scp=<<'EOF'
msed f=str1 c=b v='#$`#' i=dat3.csv o=rsl7.csv
more rsl7.csv
EOF
run(scp,title,comment)

############## Example 8
title="Suffix substitution"
comment=<<'EOF'
Replace the matching last character of b in the character string (suffix) using \verb|$'|.
EOF
scp=<<'EOF'
msed f=str1 c=b v="#$'#" i=dat3.csv o=rsl8.csv
more rsl8.csv
EOF
run(scp,title,comment)
