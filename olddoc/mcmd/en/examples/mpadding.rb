#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
no
3
6
8
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
date,dummy
20130929,a
20131002,b
20131004,c
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Create padding with integer values (\verb|type=int|) between records in \verb|no| column.
Insert \verb|4,5| between \verb|3| and \verb|6|, and \verb|7| between \verb|6| and \verb|8|.
EOF
scp=<<'EOF'
more dat1.csv
mpadding f=no%n i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Specify the starting and ending value"
comment=<<'EOF'
Insert padding between records as well as before and after the first and last records from the input data.
Specify the starting and ending range at \verb|S=,E=|.
EOF
scp=<<'EOF'
mpadding f=no%n S=1 E=10 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## Example 3
title="Padding with date"
comment=<<'EOF'
Create padding to fill in values between dates (\verb|type=date|) in the \verb|date| column.
Create padding values in columns other than those specified at \verb|k=,f=|.
EOF
scp=<<'EOF'
more dat2.csv
mpadding f=date%d i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Specify character string for padding"
comment=<<'EOF'
Specify the character string padding value at \verb|v=|.
EOF
scp=<<'EOF'
mpadding f=date%d v=padding i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Specify NULL value as padding character"
comment=<<'EOF'
NULL value can be used as padding when the \verb|-n| option is specified.
EOF
scp=<<'EOF'
mpadding f=date%d -n i=dat2.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

