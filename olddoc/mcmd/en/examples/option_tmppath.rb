#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
A,1
B,2
B,2
A,1
B,2
EOF
)}

############## Example1
title="Basic Example"
comment=<<'EOF'
Set the \verb|tmp| directory under the current directory for temporary files.
EOF
scp=<<'EOF'
msortf f=val tmpPath=./tmp i=dat1.csv o=rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Specify the environment variable"
comment=<<'EOF'
The settings of the environment variable will be applied to subsequent commands.
EOF
scp=<<'EOF'
export KG_TmpPath=~/tmp
msortf f=val i=dat1.csv o=rsl1.csv
EOF
run(scp,title,comment)

