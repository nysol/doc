#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example1
title="Display help information"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcut --help
mcut --version
EOF
runfig(scp,title)

