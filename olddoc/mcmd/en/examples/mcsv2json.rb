#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
key1,key2,v1,v2
A,X,1,a
A,Y,2,b
A,Y,3,c
B,X,4,d
B,Y,5,e
EOF
)}

############## 例1
title="Example 1: Outputting arrays"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
mcsv2json f=v1,v2 i=dat1.csv
EOF
run(scp,title,comment)

############## 例2
title="Example 2: Outputting objects (key-value pairs)"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcsv2json h=v1,v2 i=dat1.csv
EOF
run(scp,title,comment)

############## 例3
title="Example 3: Outputting objects according to field specification"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcsv2json p=v2:v1 i=dat1.csv
EOF
run(scp,title,comment)

############## 例4
title="Example 4: Specifying a key field"
comment=<<'EOF'
The three rows whose \verb|key1| field is \verb|A| are output as a single array. Then, the two rows whose \verb|key1| field is \verb|B| are output as a single array.
EOF
scp=<<'EOF'
mcsv2json k=key1 f=v1 i=dat1.csv
EOF
run(scp,title,comment)

############## 例5
title="Example 5: Nesting key fields"
comment=<<'EOF'
One row where \verb|key1=A| and \verb|key2=X| is output as a single array, two rows where \verb|key1=A| and \verb|key2=Y| are output as a single array, and the two arrays (that is, rows where \verb|key1=A|) are bundled as a single array.
EOF
scp=<<'EOF'
mcsv2json k=key1,key2 f=v1 i=dat1.csv
EOF
run(scp,title,comment)

############## 例6
title="Example 6: Outputting rows flatly without bundling them as an array"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcsv2json f=v1,v2 -flat i=dat1.csv
EOF
run(scp,title,comment)


