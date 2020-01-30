#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTexEn.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
tid,time,item
T1,0,C
T1,2,B
T1,3,A
T1,7,C
T2,2,D
T2,3,A
T2,5,B
T2,6,C
T3,1,C
T3,2,B
T3,4,D
T3,8,E
T4,2,A
T4,5,C
T4,6,B
T5,0,B
T5,1,A
T5,2,D
T5,3,D
T5,7,C
T5,9,C
T6,0,A
T6,5,B
T6,6,D
T6,8,B
T6,9,C
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
tid,time,item,class
T1,0,C,cls1
T1,2,B,cls1
T1,3,A,cls1
T1,7,C,cls1
T2,2,D,cls1
T2,3,A,cls1
T2,5,B,cls1
T2,6,C,cls1
T3,1,C,cls1
T3,2,B,cls1
T3,4,D,cls1
T3,8,E,cls1
T4,2,A,cls1
T4,5,C,cls1
T4,6,B,cls1
T5,0,B,cls2
T5,1,A,cls2
T5,2,D,cls2
T5,3,D,cls2
T5,7,C,cls2
T5,9,C,cls2
T6,0,A,cls2
T6,5,B,cls2
T6,6,D,cls2
T6,8,B,cls2
T6,9,C,cls2
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Display sequential patterns which occured more than 2 times.
Note that the field names in the input data are the same as default parameters and thus the specification of field names is not required.
EOF
scp=<<'EOF'
more dat1.csv
msequence.rb  O=result1 i=dat1.csv S=2
more result1/patterns.csv
EOF
run(scp,title,comment)

############## Example 2
title="Limit of pattern length"
comment=<<'EOF'
Enumerate sequential patterns with length of 2 which occurred more than 3 or more times.
EOF
scp=<<'EOF'
msequence.rb  O=result2 i=dat1.csv S=3 l=2 u=2
more result2/patterns.csv
more result2/tid_pats.csv
EOF
run(scp,title,comment)

############## Example 3
title="Specify gap length and window size"
comment=<<'EOF'
Enumerate sequential patterns with length above 2 which occurred more than 2 or more times, with gap length at 2 and window size at 4.
EOF
scp=<<'EOF'
msequence.rb  O=result3 i=dat1.csv S=2 l=2 gap=2 win=4
more result3/patterns.csv
EOF
run(scp,title,comment)

############## Example 4
title="Dealing with time with padding"
comment=<<'EOF'
Given the same criteria as example 3, when -padding is specified, enumerate sequential patterns in consideration of time based on gap length and window size constraints.
EOF
scp=<<'EOF'
msequence.rb  O=result4 i=dat1.csv S=2 l=2 gap=2 win=4 -padding
more result4/patterns.csv
EOF
run(scp,title,comment)

############## Example 5
title="Enumerate emerging patterns\\label{ex:ep1}"
comment=<<'EOF'
Given the same criteria as in example 1, enumerate emerging patterns by specifying class field. 
EOF
scp=<<'EOF'
more dat2.csv
msequence.rb  O=result5 i=dat2.csv S=2 class=class -padding
more result5/patterns.csv
EOF
run(scp,title,comment)

