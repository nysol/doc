#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
Refer to example in \hyperref[sect:freqpatA]{freqpatA}.
EOF
scp=<<'EOF'
EOF
run(scp,title,comment)
