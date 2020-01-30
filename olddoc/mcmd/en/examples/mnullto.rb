#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,birthday
A,19690103
B,
C,19500501
D,
E,
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,date
A,19690103
B,
C,19500501
D,
E,
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Replace NULL values in the ¥verb|birthday| field with the string \verb|“no value”|.
EOF
scp=<<'EOF'
more dat1.csv
mnullto f=birthday v="no value" i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Replace non-NULL values"
comment=<<'EOF'
Replace Null values in the \verb|birthday| field with the string \verb|"no value"| and change non-null values to the string ¥verb|"value"|, and rename the output column as \verb|entry|.
EOF
scp=<<'EOF'
mnullto f=birthday:entry v="no value" O="value" i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
############## Example 3
title="Add new column"
comment=<<'EOF'
Replace Null values in the \verb|birthday| field with the string \verb|"no value"| and change non-null values to the string \verb|"value"|. Output the replacement strings in a new column named \verb|entry|.
EOF
scp=<<'EOF'
mnullto f=birthday:entry v="no value" O="value" -A i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Replace values in previous row"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat2.csv
mnullto f=date -p i=dat2.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
