#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,date,amount
A,20081201,10
B,20081002,40
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,date,amount
A,20081207,20
A,20081213,30
B,20081209,50
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
customer,date,quantity
A,20081201,3
B,20081002,1
EOF
)}

############## Example 1
title="Concatenate files with the same header"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more dat2.csv
mcat i=dat1.csv,dat2.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="Concatenate files with different header"
comment=<<'EOF'
The first file \verb|dat1.csv| defined at \verb|i=| contains columns "customer,date,amount". However, since "amount" is not present in \verb|dat3.csv|, it will return an error. Nevertheless, the contents in the first file \verb|dat1.csv| is merged and saved in the output.
EOF
scp=<<'EOF'
more dat3.csv
mcat i=dat1.csv,dat3.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Concatenate files with different header2"
comment=<<'EOF'
When previous example is attached with \verb|-nostop| option, the command will continue processing and return NULL value for the data item not found. Other options such as \verb|skip,force| handle conditions when the field name is not found. For details, refer to the description of parameters.
EOF
scp=<<'EOF'
more dat3.csv
mcat -nostop i=dat1.csv,dat3.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Concatenate specific field names from input files"
comment=<<'EOF'
Merge field names specified at \verb|f=|.
EOF
scp=<<'EOF'
mcat f=customer,date i=dat2.csv,dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Merge from standard input"
comment=<<'EOF'
Read file \verb|dat2.csv| from standard input by specifying \verb|-stdin| option.

EOF
scp=<<'EOF'
mcat -stdin i=dat1.csv o=rsl5.csv <dat2.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## Example 6
title="Add file name as new column"
comment=<<'EOF'
When \verb|-add_fname| is specified, the original file name \verb|fileName| is added as a new column.
File name of standard input is \verb|/dev/stdin|.
EOF
scp=<<'EOF'
mcat -add_fname -stdin i=dat1.csv o=rsl6.csv <dat2.csv
more rsl6.csv
EOF
run(scp,title,comment)

############## Example 7
title="Specify wild card"
comment=<<'EOF'
Specifying wild card \verb|dat*.csv| to concatenate the three CSV files \verb|dat1.csv,dat2.csv,dat3.csv| in the current directory.
EOF
scp=<<'EOF'
more dat1.csv
more dat2.csv
more dat3.csv
mcat -force i=dat*.csv o=rsl7.csv
more rsl7.csv
EOF
run(scp,title,comment)

############## Example 8
title="Concatenate the same file multiple times"
comment=<<'EOF'
Same file can be specified more than one time.
EOF
scp=<<'EOF'
mcat i=dat1.csv,dat1.csv,dat1.csv o=rsl8.csv
more rsl8.csv
EOF
run(scp,title,comment)

