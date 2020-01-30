#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
key,val
a,2
b,5
b,4
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
a,2
b,5
b,4
EOF
)}

############## Example1
title="Specify -nfn"
comment=<<'EOF'
When \verb|-nfn| (no field name) is specified, the first row in the data will not be considered as field names. Thus, each field is specified as a number (note that the number starts from 0). 
EOF
scp=<<'EOF'
more dat2.csv
msum -nfn k=0 f=1 i=dat2.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Specify -nfno"
comment=<<'EOF'
When \verb|-nfno| (no field name for output) is specified, the first row of input data is initialized as field names, but the field names is removed from the output data.
EOF
scp=<<'EOF'
more dat1.csv
msum k=key f=val -nfno i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example3
title="Specify -nfni"
comment=<<'EOF'
The option \verb|-nfni| (no field names or input) is only available in the mcut command. This option does the opposite of - nfno; the first row of input data is not treated as a fieldname row, but the fieldnames will be shown in the output data. Thus, you need to specify an output fieldname after a colon (:) following an input field number.
EOF
scp=<<'EOF'
mcut f=0:key,1:val -nfni i=dat2.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example4
title="Specify -x"
comment=<<'EOF'
For CSV data with a field names, use the \verb|-x| option to specify the field number.
EOF
scp=<<'EOF'
msum -x k=0 f=1 i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

