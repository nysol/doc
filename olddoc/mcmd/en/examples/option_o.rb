#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,quantity,amount
A,1,10
A,2,20
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
The result of \verb|mcut| is saved to \verb|rsl1.csv| as specified in \verb|o=| parameter.
EOF
scp=<<'EOF'
more dat1.csv
mcut f=customer,amount i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Redirect"
comment=<<'EOF'
Write to standard input using redirection (\verb|">"|).
EOF
scp=<<'EOF'
mcut f=customer,amount i=dat1.csv >rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

