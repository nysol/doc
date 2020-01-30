#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,price,quantity
A,198,1
B,325,2
C,200,3
D,450,2
E,100,1
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,price,quantity
A,198,1
B,,2
C,200,
D,450,2
E,,
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Join the fields \verb|price| and \verb|quantity| to a string, rename output field as \verb|transaction|.

EOF
scp=<<'EOF'
more dat1.csv
mtrafld a=transaction f=price,quantity i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Basic Example 2"
comment=<<'EOF'
Use \verb|-r| option to revert the output results back to the original data.
EOF
scp=<<'EOF'
mtrafld -r a=transaction f=price,quantity i=rsl1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Specify the delimiter"
comment=<<'EOF'
\verb|Price| and \verb|quantity| field is separated by “\_” (underscore) character and connected by 1 character string. Use colon and name the output field as \verb|transaction|.
EOF
scp=<<'EOF'
mtrafld a=transaction f=price,quantity delim=_ delim2=':' i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="When data contains NULL value"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mtrafld a=transaction f=price,quantity i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="When data contains NULL value 2"
comment=<<'EOF'
Use \verb|-r| option to revert the output results back to the original data.
EOF
scp=<<'EOF'
mtrafld -r a=transaction f=price,quantity i=rsl4.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## Example 6
title="Specify -valOnly option"
comment=<<'EOF'
EOF
scp=<<'EOF'
mtrafld -valOnly f=price,quantity a=transaction i=dat2.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)
