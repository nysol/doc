#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
Generate a dataset with 5 sequential numbers starting from 1 incremented by 1. Name the sequence as \verb|No.|.
EOF
scp=<<'EOF'
mnewnumber a=No. I=1 S=1 l=5 o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Change the starting number and interval "
comment=<<'EOF'
Generate a dataset consisting of 5 sequential numbers starting from 10 with an incremental interval of 5. Name the sequence as \verb|No.|.
EOF
scp=<<'EOF'
mnewnumber a=No. I=5 S=10 l=5 o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Generate series of alphabet"
comment=<<'EOF'
Generate a dataset consisting of 5 alphabet sequence starting from A with 1 alphabet in between. Name the sequence as \verb|No.|.
EOF
scp=<<'EOF'
mnewnumber a=No. I=1 S=A l=5 o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Generate data without header"
comment=<<'EOF'
Generate a dataset consisting of 11 alphabet sequence starting from B with 3 alphabets in between. Exclude the header from the output.
EOF
scp=<<'EOF'
mnewnumber  -nfn  I=3 l=11 S=B o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)
