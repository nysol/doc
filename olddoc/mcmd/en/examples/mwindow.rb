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

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
store,date,val
a,20130406,1
a,20130407,2
a,20130408,3
a,20130409,4
b,20130406,11
b,20130407,12
b,20130408,13
b,20130409,14
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mwindow wk=date:win t=2 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Use first row as baseline data"
comment=<<'EOF'
EOF
scp=<<'EOF'
mwindow wk=date:win t=3 -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Print all window intervals even if the window size is less than the defined parameter"
comment=<<'EOF'
EOF
scp=<<'EOF'
mwindow wk=date:win t=3 -r -n i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Example of specifying key field"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mwindow k=store wk=date:win t=2 i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Find out the moving averages between current day and previous day"
comment=<<'EOF'
In the above example, moving average is calculated based on the last day of the window.  \verb|mslide| can be used for instances to calculate the moving averages of current day and previous day. The example is as follows:
EOF
scp=<<'EOF'
mslide f=date:date2 -q i=dat1.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## Example 6
title="Find out the moving averages from the previous day"
comment=<<'EOF'
EOF
scp=<<'EOF'
mwindow wk=date2:win t=2 i=rsl5.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)
