#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,3.28
2,3.82
3,
4,-0.6
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,1341.28
2,188
3,1.235E+3
4,-1.235E+3
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Returns the highest integer by rounding up and truncating decimals.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='floor(${val})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Basic Example"
comment=<<'EOF'
Round up to the nearest decimal place.
EOF
scp=<<'EOF'
mcal c='floor(${val},0.1)' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Example of using 0.5 as base"
comment=<<'EOF'
Convert value to base 0.5.
EOF
scp=<<'EOF'
mcal c='floor(${val},0.5)' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Example of using 10 as base"
comment=<<'EOF'
一桁目を切り上げる。
EOF
scp=<<'EOF'
more dat2.csv
mcal c='round(${val},10)' a=rsl i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

