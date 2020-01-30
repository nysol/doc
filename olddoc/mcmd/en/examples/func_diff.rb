#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,date
1,19641010
2,20000101
3,20130831
4,20130901
5,20130902
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,time
1,20120101000000
2,20120101011112
3,
4,20111231235000
5,20111231235000.123456
EOF
)}

############## Example 1
title="Compute the interval in terms of months"
comment=<<'EOF'
Compute the number of months during the period between the value in the \verb|date| column and September 1, 2013.
EOF
scp=<<'EOF'
more dat1.csv
mcal c='diffday(0d20130901,$d{date})' a=rsl i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Compute the interval in terms of minutes"
comment=<<'EOF'
Compute the minutes between the value in the \verb|time| column and January 1, 2012 00 hours 00 minutes 00 seconds.
EOF
scp=<<'EOF'
more dat2.csv
mcal c='diffmonth(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="Compute the interval in terms of microseconds"
title="Compute the interval in terms of microseconds"
comment=<<'EOF'
Compute the seconds and microseconds between the value in the \verb|time| column and January 1, 2012 00 hours 00 minutes 00 seconds.
EOF
scp=<<'EOF'
mcal c='diffsecond(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl3.csv
more rsl3.csv
mcal c='diffusecond(0t20120101000000,$t{time})' a=rsl i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

