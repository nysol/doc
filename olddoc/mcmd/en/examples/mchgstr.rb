#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,item
1,01
2,02
3,03
4,04
5,05
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
id,item
1,0111
2,0121
3,0231
4,0241
5,0151
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
id,city
1,奈良市
2,下市町
3,十津川村
4,五條市
5,山添村
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Replace values in the column from \verb|"01"| to \verb|"A"|, \verb|"03"| to \verb|"B"|, \verb|"04"| to \verb|"C"|. Other values that do not match the criteria are returned as NULL values in the output.
EOF
scp=<<'EOF'
more dat1.csv
mchgstr f=item c=01:A,03:B,05:C i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Replace values outside the criteria"
comment=<<'EOF'
Use the \verb|O=| parameter to replace character string that do not match the substitution criteria to \verb|"out of range"| in the output.
EOF
scp=<<'EOF'
mchgstr f=item c=01:A,03:B,05:C O="out of range" i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Example 3: Add new column in output"
comment=<<'EOF'
Define the name of new column (\verb|item info|) in output with \verb|-A| option.
EOF
scp=<<'EOF'
mchgstr f=item:"item info" c=01:A,03:B,05:C O="out of range" -A i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Display original value in field falls outside the criteria"
comment=<<'EOF'
When \verb|-F| option is specified, output value of the field remains the same if it does not match any of the substitution criteria.
EOF
scp=<<'EOF'
mchgstr f=item c=01:A,03:B,05:C -F i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Replace matching substrings"
comment=<<'EOF'
Replace substring with \verb|-sub| option specified. In following example, values where \verb|item| field contains \verb|"01"| will be substituted with \verb|"A"|.
EOF
scp=<<'EOF'
more dat2.csv
mchgstr f=item c=01:A -sub i=dat2.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## Example 6
title="Wide character substring match"
comment=<<'EOF'
Use the option \verb|-W| to replace wide-characters strings. However, if you are using UTF-8 encoding, it is not necessary to define \verb|-W|. Refer to the section "\hyperref[sect:multibyte]{Multibyte characters}" for details.
EOF
scp=<<'EOF'
more dat3.csv
mchgstr f=city c=市:01,町:02,村:02 -sub -W i=dat3.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)
