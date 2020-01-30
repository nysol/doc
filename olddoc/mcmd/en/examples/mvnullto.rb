#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items
b a  c
 c c
e a   b 
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
items
b.a..c
.c.c
e.a...b.
EOF
)}


############## Example1
title="Example1: Replace null characters to the character string ’null’"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mvnullto vf=items v=null i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Example 2: Use .(dot) as delimiting character"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mvnullto vf=items v=null delim=. i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example3
title="Example 3: Replace null with the previous value"
comment=<<'EOF'
EOF
scp=<<'EOF'
mvnullto vf=items -p i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example4
title="Example 4: Replace all values except null by specifying O="
comment=<<'EOF'
EOF
scp=<<'EOF'
mvnullto vf=items v=null O=X i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
