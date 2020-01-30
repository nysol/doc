#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val1,val2
A,1,2
B,2,3
C,3,4
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
Extract fields \verb|val1| and \verb|val2|.
EOF
scp=<<'EOF'
more dat1.csv
mcut f=val1,val2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Specify name of output field"
comment=<<'EOF'
Aggregate \verb|val1,val2|, and rename the fields in the output as \verb|sum1,sum2| respectively.
EOF
scp=<<'EOF'
msum f=val1:sum1,val2:sum2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

