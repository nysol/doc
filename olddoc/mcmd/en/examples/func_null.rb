#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id
1
2
3
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,a
2,
3,b
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Print NULL values to column \verb|rsl|. 
EOF
scp=<<'EOF'
more dat1.csv
mcal c='nulls()' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Use of if statement"
comment=<<'EOF'
Use nulln() function to match the value specified in the second parameter.
EOF
scp=<<'EOF'
mcal c='if(${id}==1,1,nulln())' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Equivalent to isnull function"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='if(${val}==nulln(),"null","notNull")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

