#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example1
title="Generate data with mdata command"
scp=<<'EOF'
mdata man0 >man0.csv
more man0.csv
EOF
runfig(scp,title)
