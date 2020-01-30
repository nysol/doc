#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,itemID,october
a,xx,11
b,yy,122
c,zz,
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
a,xx,11
b,yy,122
c,zz,
EOF
)}


File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
customer%r,itemID,october
c,zz,
b,yy,122
a,xx,11
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Change column name from “customer” to “cust”, and “october” to “oct”.
EOF
scp=<<'EOF'
more dat1.csv
mfldname f=customer:cust,october:oct. i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Rename column"
comment=<<'EOF'
Change field names to \verb|x,y,z|.
EOF
scp=<<'EOF'
mfldname n=x,y,z i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Data without field names"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mfldname -nfni n=x,y,z i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Remove sort order symbols in field names"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat3.csv
mfldname -q  i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
