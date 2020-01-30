#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
a=ZDD::itemset("a b")
a.show
b=ZDD::itemset("b")
b.show
c=ZDD::itemset("")
c.show

# 数字をアイテム名として利用することも可能
x0=ZDD::itemset("2")
x0.show

# ただし、表示上重みと区別がつかなくなるので注意が必要。
(2*x0).show

# こんな記号ばかりのアイテム名もOK。
x1=ZDD::itemset("!#%&'()=~|@[;:]")
x1.show

# ただし、rubyで特殊な意味を持つ記号はエスケープする必要がある。
# 以下では、\,$,"の3つの文字をエスケープしている例である。
x2=ZDD::itemset("\\\$\"")
x2.show

# もちろん日本語も利用可。
x3=ZDD::itemset("りんご ばなな")
x3.show
EOF
run(scp,title,comment)

