#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,x,y
A,2,7
B,6,7
C,5,6
D,7,5
E,6,4
F,1,3
G,3,3
H,4,2
I,7,2
J,2,1
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,x,y
A,2,7
A,6,7
A,5,6
B,7,5
B,6,4
B,1,3
C,3,3
C,4,2
C,7,2
C,2,1
EOF
)}


############## Example 1
title="Basic Example"
comment=<<'EOF'
Partition x and y into two subsets of equal extent and save the output file as rng.csv
EOF
scp=<<'EOF'
more dat1.csv
mbucket f=x:xb,y:yb n=2 O=rng1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more rng1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Partition by equal range"
comment=<<'EOF'
Use \verb|-rng| option to partition the data by uniform value ranges.
EOF
scp=<<'EOF'
mbucket f=x:xb,y:yb n=2 -rng O=rng2.csv i=dat1.csv o=rsl2.csv
more rsl2.csv
more rng2.csv
EOF
run(scp,title,comment)


############## Example 3
title="Example using key field"
comment=<<'EOF'
Partition x and y into two subsets of equal extent using "id" as the key parameter.
By specifying \verb|n=2,3|, field \verb|x| is divided into 2 buckets, and field
\verb|y| is divided into 3 buckets.
Include bucket numbers and value range of buckets in the output file (\verb|F=2|).
EOF
scp=<<'EOF'
more dat2.csv
mbucket k=id f=x:xb,y:yb n=2,3 F=2 i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


