#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
id,val
1,123456789
2,1234.56789
3,0.123456789
4,0.000123456789
5,0.0000123456789
EOF
)}

############## Examples1
title="Basic Example"
comment=<<'EOF'
The exponential notation of id=1 is 1.2345678e +08, the exponent bits is more than 6 significant figures when the significant figures of mantissa is set at 6.   
The exponential notation of id=2 is 1.23456789e +03, the exponent bits is more than 7 significant figures when the significant figures of integer bits + decimal bits is set at 6. 
The exponential notation of id=4 is 1.23456789e-04, the exponent bits is less than -4 when the significant figures is set at 6. 
The exponential notation of id=5 is 1.23456789e-05, the exponent bits is less than -4 when the significant figures of mantissa is set at 6. 
EOF
scp=<<'EOF'
more dat1.csv
mcal c='${val}' a=result precision=6 i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example2
title="Case when precision=2"
comment=<<'EOF'
EOF
scp=<<'EOF'
mcal c='${val}' a=result precision=2 i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example3
title="Specify the environment variable"
comment=<<'EOF'
When the environment variable is set, the setting will be applied to all commands in subsequent processes.
EOF
scp=<<'EOF'
export KG_Precision=4
mcal c='${val}' a=result i=dat1.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

