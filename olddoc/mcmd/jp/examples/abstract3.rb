#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## 例1
title="ヘルプの表示"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcut --help
mcut --helpl
mcut --version
EOF
runfig(scp,title)

