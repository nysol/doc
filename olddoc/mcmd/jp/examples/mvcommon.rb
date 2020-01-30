#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
items1,items2
b a c,b b
c c,a d
e a a,a a
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
item
a
c
e
EOF
)}


############## 例1
title="複数項目に対して結合する例"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mvcommon vf=items1,items2 K=item m=ref1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## 例2
title="項目名を変更する例"
comment=<<'EOF'
\verb|item2|に新項目名\verb|new2|を指定しているので、
項目名が変更され出力される。
EOF
scp=<<'EOF'
mvcommon vf=items1,items2:new2 K=item m=ref1.csv i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## 例3
title="項目を追加する例"
comment=<<'EOF'
\verb|item1|に新項目名\verb|new1|を、
\verb|item2|に新項目名\verb|new2|を指定し、
\verb|-A|オプションを付けているので
新項目\verb|new1|と\verb|new2|が追加され出力される。
EOF
scp=<<'EOF'
mvcommon vf=items1:new1,items2:new2 -A K=item m=ref1.csv i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)


