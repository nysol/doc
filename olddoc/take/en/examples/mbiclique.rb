#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTexEn.rb"

File.open("dat.csv","w"){|fpw| fpw.write(
<<'EOF'
node1,node2
a,A
a,B
a,C
b,A
b,B
b,D
c,A
c,D
d,B
d,C
d,D
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Example illustrated from the previous section.
EOF
scp=<<'EOF'
more dat.csv
mbiclique.rb i=dat.csv f=node1,node2 o=result1.csv
more result1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Example with size limit"
comment=<<'EOF'
Enumerate maximal bipartite clique with size of 2 in columns \verb|node1,node2|.
EOF
scp=<<'EOF'
mbiclique.rb i=dat.csv f=node1,node2 o=result2.csv l=2,2 u=2,2
more result2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Example to limit the partial size"
comment=<<'EOF'
Enumerate maximal bipartite clique where column \verb|node1| with lower limit of 1 (Since the default lower limit is 1, this example does not reflect additional meaning),
and column \verb|node2| has a upper limit of 3.
The first value at \verb|u=| parameter is null, since the upper limit of column \verb|node1|. 
EOF
scp=<<'EOF'
mbiclique.rb i=dat.csv f=node1,node2 o=result3.csv l=1, u=,3
more result3.csv
EOF
run(scp,title,comment)

