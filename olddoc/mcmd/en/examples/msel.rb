#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Quantity,Amount
A,1,10
A,2,20
B,1,30
B,3,40
B,1,50
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
a,b
A,-1
B,
C,1
EOF
)}

############## Example 1
title="Basic example"
comment=<<'EOF'
Select records where "Amount" is greater than 40. Write the unmatched records to a different output file file \verb|unmatch1.csv|.
EOF
scp=<<'EOF'
more dat1.csv
msel c='${Amount}>40' u=unmatch1.csv i=dat1.csv o=match1.csv
more match1.csv
more unmatch1.csv
EOF
run(scp,title,comment)

############## 例2
title="Selecting records with null value(s)"
comment=<<'EOF'
No records will be selected when the condition defined \verb|c=| returned a null value. Records that do not match the condition will be written to a separate file defined in \verb|u=|. 
 
In the following example, the first three rows of data from column \verb|b| are \verb|-1|, null, and \verb|1|. When selecting records where \verb|b| is greater than 0, the query record with a null value will be treated as an exception saved in the unmatched records file. 
EOF
scp=<<'EOF'
more dat2.csv
msel c='${b}>0' i=dat2.csv o=match2.csv u=unmatch2.csv
more match2.csv
more unmatch2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Specify -r option"
comment=<<'EOF'
Null value is always evaluated as a unknown value regardless of the condition. Thus,  records with null value is not selected.

In the following example, the reverse selection parameter \verb|-r| is used with the same condition in the previous example. Even though the selection criteria is inverted, the query record with a null value will be treated as an exception saved in the unmatched records file as in the previous example.
EOF
scp=<<'EOF'
msel -r c='${b}>0' i=dat2.csv o=match3.csv u=unmatch3.csv
more match3.csv
more unmatch3.csv
EOF
run(scp,title,comment)
