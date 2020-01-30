#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTexEn.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
tid,item
T1,C
T1,E
T2,D
T2,E
T2,F
T3,A
T3,B
T3,D
T3,F
T4,B
T4,D
T4,F
T5,A
T5,B
T5,D
T5,E
T6,A
T6,B
T6,D
T6,E
T6,F
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Display similarity graph with 2 or more occurrence.
The example is shown above.
EOF
scp=<<'EOF'
more dat1.csv
mtra2g.rb  S=2 tid=tid item=item i=dat1.csv oe=edge1.csv
more edge1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Add resemblance"
comment=<<'EOF'
Based on example 1, add the degree of similarity criteria where resemblance is above 0.4.
By specifying \verb|on=|, only the frequency of appearance of item is returned as node information.
EOF
scp=<<'EOF'
mtra2g.rb  S=2 sim=R th=0.4 tid=tid item=item i=dat1.csv oe=edge2.csv on=node2.csv
more node2.csv
more edge2.csv
EOF
run(scp,title,comment)

