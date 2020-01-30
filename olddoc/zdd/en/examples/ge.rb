#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Eaxample "
comment=<<'EOF'
Refer to the example in\hyperref[sect:eq]{==}.
EOF
scp=<<'EOF'
EOF
run(scp,title,comment)

