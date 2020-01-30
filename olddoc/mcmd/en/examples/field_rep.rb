#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
brand,quantity10,quantity11,quantity12,quantity123
A,10,15,9,1
B,20,16,8,2
C,30,17,7,3
D,40,18,6,4
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
A,10,15,9,1
B,20,16,8,2
C,30,17,7,3
D,40,18,6,4
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
In this example, \verb|"&"| is replaced with “\verb|brand|” in the input field name, which is equivalent to the expression "\verb|f=brand:brand code|".
EOF
scp=<<'EOF'
more dat1.csv
mcut f="brand:& code" i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Combine with wildcard"
comment=<<'EOF'
Attach “\verb|&|” after \verb|sales&| to replace the character with input field name (e.g. "quantity10") in the output field name.  For all input fields name beginning with “\verb|quantity|”, attach “\verb|sales|” as the prefix in the output field name. 
EOF
scp=<<'EOF'
mcut f="brand,quantity*:sales&" i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

