#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,101215
2,210110
3,
4,120001
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,1
2,0
3,
4,-2
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,10
2,0
3,-5
4,0
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
If the value in time column is less than 120000, return "AM", otherwise, return "PM".
EOF
scp=<<'EOF'
more dat1.csv
mcal c='if(${time}<=120000,"AM","PM")' a=ampm i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Different parameter types"
comment=<<'EOF'
The function returns an error if the character format is different in the second and third parameter.
EOF
scp=<<'EOF'
mcal c='if(${time}<=120000,"am",1)' a=ampm i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


############## Example 3
title="Return boolean value on conditional statements"
comment=<<'EOF'
Read the value in the column using \verb|$b{fieldname}|, if the value is “1” return true, if it is “0” return false, other values will be treated as NULL.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='if($b{val},"ture","false")' a=bool i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Time format comparison"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='if($t{time}<=0t120000,"am","pm")' a=ampm i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Nested if function"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat3.csv
mcal c='if(${val}>0,"plus",if(${val}<0,"minus","zero"))' a=sign i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

