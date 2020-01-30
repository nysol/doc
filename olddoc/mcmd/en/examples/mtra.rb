#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,item
A,a
A,b
B,c
B,d
B,e
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Combine the corresponding \verb|item| for each \verb|customer| in a string using a space as the delimiter, and save output in the column named \verb|transaction|.
EOF
scp=<<'EOF'
more dat1.csv
mtra k=customer f=item:transaction i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Use hyphen (-) as item delimiter"
comment=<<'EOF'
EOF
scp=<<'EOF'
mtra k=customer f=item:transaction delim=- i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


############## 例3
title="Convert items in descending sort order"
comment=<<'EOF'
EOF
scp=<<'EOF'
mtra k=customer s=item%r f=item:transaction i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)