#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
item,date,quantity,price
A,20081201,1,10
A,20081202,2,20
A,20081203,3,30
B,20081201,4,40
B,20081203,5,50
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Expand the array of \verb|date| horizontally and itemize \verb|quantity|
to the corresponding \verb|item|.
EOF
scp=<<'EOF'
more dat1.csv
mcross k=item f=quantity s=date i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Restore the original input data"
comment=<<'EOF'
Restore the output from Example 1 to the original input data with \verb|mcross|.
EOF
scp=<<'EOF'
more rsl1.csv
mcross k=item f=2008* s=fld a=date i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Crosstab with multiple fields"
comment=<<'EOF'
Display crosstab results on two fields \verb|quantity,price|.
EOF
scp=<<'EOF'
mcross k=item f=quantity,price s=date i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


############## Example 4
title="Reverse data sequence"
comment=<<'EOF'
Restore the sequence of the items that was expanded horizontally.
EOF
scp=<<'EOF'
mcross k=item f=quantity,price s=date%r i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
