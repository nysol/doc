#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,000103
2,235959
3,
4,000000
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,date
1,20130901000103
2,20130902000103
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcal c='tseconds($t{time})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="The result is the same using on date values"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='tseconds($t{date})' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

