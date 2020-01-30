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
f=5*a*b*c - 3*a*b + 2*b*c + c
f.show
ZDD::constant(0).show
EOF
run(scp,title,comment)

############## 例2
title="bit"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
f=5*a*b*c - 3*a*b + 2*b*c + c
f.show

f.bit

# "a b c"の重み5の(-2)進数は101となる。
# 1*(-2)^2+0*(-2)^1+1*(-2)^0 = 5
# よって0桁目と2桁目にアイテム集合"a b c"が表示されている。
# "a b"の重み-3の(-2)進数は1101となる。
# 1*(-2)^3+1*(-2)^2+0*(-2)^1+1*(-2)^0 = -3
# よって0,2,3桁目にアイテム集合"a b"が表示されている。
EOF
run(scp,title,comment)

############## 例3
title="hex"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
d=ZDD::itemset("d")

f=a*b+11*b*c+30*d+4
f.show
f.hex
EOF
run(scp,title,comment)

############## 例4
title="map"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
d=ZDD::itemset("d")
f=2*a*b+3*b+4
f.show
f.map
# アイテムaが１列目のビット列に、アイテムbが１行目のビット列に対応してアイテム集合が表現されている。
# セルの値は重みを表す。左上のセルはaが0、bが0、すなわち定数項が4であることが示されている。

# 4アイテムでは以下の通り。
g=a*b + 2*b*c + 3*d + 4
g.show
g.map
EOF
run(scp,title,comment)

############## 例5
title="rmap"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# 4つのアイテムa,b,c,dを宣言
ZDD::symbol("a")
ZDD::symbol("b")
ZDD::symbol("c")
ZDD::symbol("d")

f=ZDD::itemset("a b") + 2*ZDD::itemset("b c") + 4
f.show

# mapで表示させると以下の通り。
f.map

# rmapで表示させるとdが省かれて表示される。
f.rmap
EOF
run(scp,title,comment)

############## 例6
title="case"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
f=5*a*b*c - 3*a*b + 2*b*c + 5*c
f.show

f.case
EOF
run(scp,title,comment)

############## 例7
title="decomp"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")

f1=(a*b*c)
f1.show
f1.decomp
# a,b,cのANDということでa*b*c=a b c

f2=((a*b*c)+(a*b))
f2.show
f2.decomp
# c,1のORにて(c+1)、それとa bとのANDで(a b)*(c+1)=a b c + a b

f3=((a*b*c)+(a*b)+(b*c))
f3.show
f3.decomp
# [ a c ]はaとcによる全組合せ集合、すなわち(a c + a + c)。
# それとbとのANDで b*(a c + a + c) = a b c + a b + b c

f4=((a*b*c)+(a*b)+(b*c)+(c*a))
f4.show
f4.decomp
# [ a b c ]はa,b,cによる全組合せ集合、すなわち(a b c + a b + b c + c a)
EOF
run(scp,title,comment)
