#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id1
1
2
3
4
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
id2
a
b
c
d
EOF
)}

File.open("ref2.csv","w"){|fpw| fpw.write(
<<'EOF'
id2
a
b
EOF
)}

File.open("ref3.csv","w"){|fpw| fpw.write(
<<'EOF'
id2,val
a,R0
b,R1
c,R2
d,R3
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mpaste m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Example of merging data of different sizes"
comment=<<'EOF'
If the number of rows in the input file is different from the reference file , merge records according to the smaller file.
EOF
scp=<<'EOF'
more ref2.csv
mpaste m=ref2.csv i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Outer join"
comment=<<'EOF'
If there are less number of rows in the reference file, NULL values will be assigned to records that did not match with the input file when \verb|-n| option is specified.
EOF
scp=<<'EOF'
mpaste m=ref2.csv -n i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Define fields to join"
comment=<<'EOF'
EOF
scp=<<'EOF'
more ref3.csv
mpaste f=val m=ref3.csv i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
