#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
date,val
20130406,1
20130407,2
20130408,3
20130409,4
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mslide s=date f=val:newVal i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Slide rows in reverse direction"
comment=<<'EOF'
EOF
scp=<<'EOF'
mslide s=date f=val:newVal -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Slide records more than once"
comment=<<'EOF'
EOF
scp=<<'EOF'
mslide s=date f=val t=2 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Display output from the last column shifted"
comment=<<'EOF'
EOF
scp=<<'EOF'
mslide s=date f=val t=2 -l i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Change multiple field names"
comment=<<'EOF'
EOF
scp=<<'EOF'
mslide s=date f=date:d_,val:v_ t=2 i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)
