#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTexEn.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
node1,node2
a,b
a,c
a,e
b,c
b,e
b,g
c,d
c,g
d,e
e,f
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Use resemblance(sim=R) as similarity measure, the polished graph is obtained by extending the branch at th=0.4.
The number of polishing iterations are converged 3 times as shown in \verb|log1.csv| (iter,4)。
The output result is shown in Figure \ref{fig:resemblance04}.
EOF
scp=<<'EOF'
more dat1.csv
mpolishing.rb i=dat1.csv f=node1,node2 sim=R th=0.4 o=result1.csv log=log1.csv
more result1.csv
more log1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Polishing by PMI"
comment=<<'EOF'
Use normalized PMI(sim=P) as similarity measure, the polished graph is obtained by extending the branch at th=0.2.
The output result is shown in Figure \ref{fig:pmi02}.

EOF
scp=<<'EOF'
mpolishing.rb i=dat1.csv f=node1,node2 sim=P th=0.2 o=result2.csv
more result2.csv
EOF
run(scp,title,comment)


############## Example 3
title="Polish once at intersection"
comment=<<'EOF'
Based on the explanation in the previous example. Use intersection(sim=T) as similarity measure, consider cases with 2 or more (th=2) branch extension with direct connection. Polish graph with 1 iteration (iter=1).
The output result is shown in Figure \ref{fig:polished2}.

EOF
scp=<<'EOF'
mpolishing.rb i=dat1.csv f=node1,node2 sim=T th=2 iter=1 o=result3.csv
more result3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Exclude direct connection"
comment=<<'EOF'
When \verb|-indirect| is specified, direct connection is ignored when calculating degree of similarity.
The output graph is shown in Figure \ref{fig:polished1}, to remove all branches, branch data is not returned after polishing.
EOF
scp=<<'EOF'
mpolishing.rb i=dat1.csv f=node1,node2 sim=T th=2 o=result4.csv -indirect
more result4.csv
EOF
run(scp,title,comment)


