#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
brand,quantity01,quantity02,quantity03,quantity04,quantity05,quantity06,quantity07,quantity08,quantity09,quantity10
A,10,50,90,130,170,210,250,290,330,370
B,20,60,100,140,180,220,260,300,340,380
C,30,70,110,150,190,230,270,310,350,390
D,40,80,120,160,200,240,280,320,360,400
EOF
)}

############## Example1
title="Specify range"
comment=<<'EOF'
By specifying "0-4", fields 0,1,2,3,4 are specified.  
EOF
scp=<<'EOF'
more dat1.csv
mcut -x f=0-4 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Specify range in reverse order"
comment=<<'EOF'
By specifying “4-0”,  fields 0,1,2,3,4 are specified.
EOF
scp=<<'EOF'
mcut -x f=4-0 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example3
title="Specify Multiple ranges"
comment=<<'EOF'
By specifying “1-0,2-4”, fields “1,0,2,3,4” are specified.EOF
scp=<<'EOF'
mcut -x f=1-0,2-4 i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example4
title="Specified field from the end"
comment=<<'EOF'
By specifying "2L", the second field from the end is specified (quantity 08).
EOF
scp=<<'EOF'
mcut -x f=2L i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example5
title="Specify the range of fields from the end"
comment=<<'EOF'
By specifying "5-3L", the 5th to the 3rd item from end is specified, i.e. "5,6,7".
EOF
scp=<<'EOF'
mcut -x f=5-3L i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

