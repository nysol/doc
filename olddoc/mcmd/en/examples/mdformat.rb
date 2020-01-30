#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
fld
a:20120304:b:121212
a:20101204:b:011309
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
fld,fld2
2010/11/20,2010/11/21
2010/1/1,2010/1/2
2011/01/01,2010/01/02
2010/1/01,2010/1/02
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
fld
2010 11 20 12:34:56

2011 01 01 23:34:56
2010  1 01 123455
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Extract and convert time and date information from \verb|fld| field.
Save the converted format as
"a:yearmonthday:b:timeminutesecond", by specifying "\verb|a:%Y%m%d:b:%H%M%S|"
in the \verb|c=| parameter.
EOF
scp=<<'EOF'
more dat1.csv
mdformat f=fld c=a:%Y%m%d:b:%H%M%S i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Add Results to New Column"
comment=<<'EOF'
Store results in \verb|fld2| from format conversion in \verb|fld1| field,
specify the format by "\verb|%Y/%m/%d|" in \verb|c=| parameter.
Use \verb|-A| option to save results in \verb|f2| field.
EOF
scp=<<'EOF'
more dat2.csv
mdformat f=fld:f1,fld2:f2 c=%Y/%m/%d i=dat2.csv -A o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Case of failed extraction"
comment=<<'EOF'
The date format in \verb|fld| field is saved as "Year Month Day Time:Minute:Second",
"\verb|%Y %m %d %H:%M:%S|" is specified in \verb|c=| parameter.
However, it failed since the format is different in different rows.
EOF
scp=<<'EOF'
more dat3.csv
mdformat f=fld:f1 c='%Y %m %d %H:%M:%S' i=dat3.csv -A o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


