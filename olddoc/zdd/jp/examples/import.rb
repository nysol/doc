#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
f=5*a*b*c+3*a*b+2*b*c+c
f.show
f.export("dat.zdd")
# エキスポートされたファイルdat.zddの内容は以下の通り。
# _i 3
# _o 3
# _n 7
# 4 1 F T
# 248 2 F 5
# 276 3 4 248
# 232 2 F 4
# 2 2 F T
# 272 3 232 2
# 268 3 232 248
# 276
# 272
# 268
EOF
run(scp,title,comment)

title="正しい復元例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# 以下のようにsymbolを順番に宣言した後にimportすれば正しく復元される。
ZDD::symbol("a")
ZDD::symbol("b")
ZDD::symbol("c")
g1=ZDD::import("dat.zdd")
g1.show
EOF
run(scp,title,comment)

title="正しくない復元例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# もしアイテムb,cの宣言順序を入れ替えると結果においてもbとcが入れ替わってしまう。
ZDD::symbol("a")
ZDD::symbol("c")
ZDD::symbol("b")
g2=ZDD::import("dat.zdd")
g2.show
EOF
run(scp,title,comment)

title="symbol宣言なしでの復元例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# 宣言せずにインポートすると、x1,x2,x3のようなアイテム名が使われる。
# この時、各アイテムの後ろに付いた数字は、アイテムの宣言の逆順による連番となる。
# 以下の例では、x1=c, x2=b, x3=cである。
g3=ZDD::import("dat.zdd")
g3.show
EOF
run(scp,title,comment)

