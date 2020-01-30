#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,date
1,20000101
2,20121021
3,
4,19770812
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,20000101000000
2,20121021111213
3,
4,19770812122212
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='month($d{date})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Fixed length character string"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='months($d{date})' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


############## Example 3
title="Month in English"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='monthe($d{date})' a=rsl i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Abbreviation of month in English"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='monthes($d{date})' a=rsl i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Extract month from time formatted data"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='month($t{time})' a=rsl i=dat2.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

