#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
\hyperref[sect:termsEQ]{termsEQ} Refer to example of the method.
EOF
scp=<<'EOF'
EOF
run(scp,title,comment)

