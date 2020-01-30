#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("tra.txt","w"){|fpw| fpw.write(
<<'EOF'
1 2 3 6
4 5 6
1 2 4 6
2 4 6
1 2 4 5
EOF
)}

File.open("order.txt","w"){|fpw| fpw.write(
<<'EOF'
1 2 3 4 5 6
EOF
)}


############## 例1
title="基本例"
comment=<<'EOF'
EOF
scp=<<'EOF'
require 'zdd'
# tra.txtの内容
# 1 2 3 6
# 4 5 6
# 1 2 4 6
# 2 4 6
# 1 2 4 5
# order.txtの内容
# 1 2 3 4 5 6
p1=ZDD::lcm("FQ","tra.txt",3,"order.txt")
p1.show

# オーダファイルを省略した場合、得られる頻出アイテム集合は同じであるが
# そのアイテム番号がトランザクションファイルのアイテム番号と異なったものとなることに注意する。
p2=ZDD::lcm("FQ","tra.txt",3)
p2.show
EOF
run(scp,title,comment)

