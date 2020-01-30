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

############## 例1
title="基本例"
comment=<<'EOF'
概要にて解説した例。
/a/bをキー要素として、5つのCSV項目を出力する。
EOF
scp=<<'EOF'
more dat1.xml
mxml2csv k=/a/b f=@att:b_att,c@p:c_p,c@p%f:c_p_f,d:d,/a:a i=dat1.xml  o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="絶対パス"
comment=<<'EOF'
基本例と同じ要素を絶対パスで指定する例。
/a/bをキー要素として、5つのCSV項目を出力する。
EOF
scp=<<'EOF'
mxml2csv k=/a/b f=/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a i=dat1.xml  o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="キー要素の変更"
comment=<<'EOF'
絶対パスの例でキー要素をaに変更した例。
aの終了タグは一つしかないので、一行だけ出力されている。
f=で指定した/a/b@attは、2回出現しているが、最後に出現した値が出力されている。
EOF
scp=<<'EOF'
mxml2csv k=/a f=/a/b@att:b_att,/a/b/c@p:c_p,/a/b/c@p%f:c_p_f,/a/b/d:d,/a:a i=dat1.xml o=rsl3.csv
more rsl3.csv
EOF

run(scp,title,comment)
