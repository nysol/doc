#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.xml","w"){|fpw| fpw.write(
<<'EOF'
<a att="aa">
  <b att="bb1">
    <c p="pp1" q="qq1"/>
    <d>text1</d>
  </b>
  <b att="bb2">
    <c q="qq2"></c>
    <d>text2</d>
  </b>
  <b>
    <c p="pp3"/>
    <d>text3</d>
  </b>
</a>
EOF
)}

############## Example1
title="Example 1: Basic example"
comment=<<'EOF'
The example below is illustrated in the summary above. Output the 5 CSV fields with /a/b set as the key elements.
EOF
scp=<<'EOF'
more dat1.xml
mxml2csv k=/a/b f=@att:b_att,c@p:c_p,c@p%f:c_p_f,d:d,/a:a i=dat1.xml  o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Example 2: Absolute path"
comment=<<'EOF'
Specification of same element as in the basic example with an absolute path. Output the 5 CSV fields with /a/b as the key elements.
EOF
scp=<<'EOF'
mxml2csv k=/a/b f=/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a i=dat1.xml  o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example3
title="Example 3: Changing key elements"
comment=<<'EOF'
Example of changing a key element to a using an absolute path. Since there is only one end tag a, one row of record will be returned as output. /a/b@att specified at f= appeared twice, the last value is returned as output.
EOF
scp=<<'EOF'
mxml2csv k=/a f=/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a i=dat1.xml o=rsl3.csv
more rsl3.csv
EOF

run(scp,title,comment)
