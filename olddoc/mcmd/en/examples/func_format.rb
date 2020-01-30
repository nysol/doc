#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,0.00726
2,123.456789
3,
4,-0.335
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,amount
1,1000
2,250
3,
4,960
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Format \verb|val| as real number with 3 decimal places.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='format(${val},"%8.3f")' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Display the exponent"
comment=<<'EOF'
Format \verb|val| in exponential notation.
EOF
scp=<<'EOF'
mcal c='format(${val},"%e")' a=rsl i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Combination of character strings"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mcal c='format(${amount},"total amount is %g yen.")' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment,"dat2.csv","rsl3.csv")
