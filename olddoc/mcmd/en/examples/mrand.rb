#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer
A
B
C
D
E
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer
A
A
A
B
B
C
D
D
D
EOF
)}


############## Example 1
title="Basic example"
comment=<<'EOF'
Generate random real numbers between 0.0 to 1.0.
EOF
scp=<<'EOF'
more dat1.csv
mrand a=rand i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Basic Example 2"
comment=<<'EOF'
Generate random integers with -int.
EOF
scp=<<'EOF'
mrand a=rand -int i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Specify the minimum and maximum value of the random number"
comment=<<'EOF'
Generate a random number with a minimum value of 10 and maximum value of 100. Add the random numbers to a new column named \verb|rand|.
EOF
scp=<<'EOF'
mrand a=rand -int min=10 max=100 S=1 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)
############## Example 4
title="Generate random number by key"
comment=<<'EOF'
Given 4 customers \verb|A,B,C,D|, same random number is generated for same customer.
EOF
scp=<<'EOF'
more dat2.csv
mrand k=Customer -int min=0 max=1 a=rand i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
