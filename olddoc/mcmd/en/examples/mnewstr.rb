#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
Generate a new dataset with characters strings \verb|custNo| and \verb|A0001| printed in 5 rows, and name the fields as \verb|attribute| and \verb|code| respectively.
EOF
scp=<<'EOF'
mnewstr a=attribute,code v=custNo,A0001 l=5 o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)
