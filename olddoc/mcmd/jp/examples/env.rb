#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat.csv","w"){|fpw| fpw.write(
<<'EOF'
k,v
A,1
B,2
EOF
)}

############## 例1
title="終了メッセージ"
comment=<<'EOF'
デフォルトでは \verb|KG_Verbose=4| なので、正常終了時のメッセージもエラー終了メッセージも出力される。
EOF
scp=<<'EOF'
more dat.csv
mcut f=k,v i=dat.csv o=out.csv
mcut x=k,v i=dat.csv o=out.csv
EOF
run(scp,title,comment)

############## 例2
title="エラーメッセージのみ出力"
comment=<<'EOF'
\verb|KG_Verbose=1|とすると、エラー終了メッセージは表示されるが、正常終了メッセージは表示されない。
EOF
scp=<<'EOF'
export KG_VerboseLevel=1
mcut f=k,v i=dat.csv o=out.csv
mcut x=k,v i=dat.csv o=out.csv
EOF
run(scp,title,comment)

############## 例3
title="メッセージを一切表示させない"
comment=<<'EOF'
\verb|KG_Verbose=0|とすると、いずれのメッセージも表示されない。
EOF
scp=<<'EOF'
export KG_VerboseLevel=0
mcut f=k,v i=dat.csv o=out.csv
mcut x=k,v i=dat.csv o=out.csv
EOF
run(scp,title,comment)
