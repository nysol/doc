#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,data
A,1 10 2
A,2 20 3
B,1 15 5
B,3 10 4
B,1 20 6
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,data
A,1 10 2
A,2 20 3
B,1 15 5
B,3 4
B,1
EOF
)}


File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,data
A,1_10_3
A,2_20_5
B,1_15_6
B,3_10_7
B,1_20_8
EOF
)}


############## 例1 基本例
title="Example 1: Basic example"
comment=<<'EOF'
Fields are partitioned by en spaces.
EOF
scp=<<'EOF'
more dat1.csv
msplit f=data a=d1,d2,d3 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2 -r利用
title="Example 2: Using -r"
comment=<<'EOF'
The \verb|-r| option is specified to delete the fields specified by the \verb|f=| parameter.
EOF
scp=<<'EOF'
msplit f=data a=d1,d2,d3 -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3 分割数不一致
title="Example 3: Unmatched partition counts"
comment=<<'EOF'
If the partitionable fields are fewer than the number of fields specified by the \verb|a=| parameter, NULL will be added. If they are more than the number of fields specified by the \verb|a=| parameter, they are output from the beginning until the specified number of partitions is reached.
EOF
scp=<<'EOF'
more dat2.csv
msplit f=data a=d1,d2 i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## 例4 delim指定
title="Example 4: Specifying delim"
comment=<<'EOF'
The \verb|delim=| parameter is used to partition fields by a character other than the en space.
EOF
scp=<<'EOF'
more dat3.csv
msplit f=data a=d1,d2,d3 delim=_ i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

