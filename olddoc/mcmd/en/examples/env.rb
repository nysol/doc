#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat.csv","w"){|fpw| fpw.write(
<<'EOF'
k,v
A,1
B,2
EOF
)}

############## Example1
title="End message"
comment=<<'EOF'
The default setting of output message is set as \verb|KG_Verbose=4| which displays a message when the program finished processing normally or terminates upon an error.
EOF
scp=<<'EOF'
more dat.csv
mcut f=k,v i=dat.csv o=out.csv
mcut x=k,v i=dat.csv o=out.csv
EOF
run(scp,title,comment)

############## Example2
title="Only display error messages"
comment=<<'EOF'
If \verb|KG_Verbose=1|, the stop error message is displayed, but not the normal exit message.
EOF
scp=<<'EOF'
export KG_VerboseLevel=1
mcut f=k,v i=dat.csv o=out.csv
mcut x=k,v i=dat.csv o=out.csv
EOF
run(scp,title,comment)

############## Example3
title="Do not display any messages"
comment=<<'EOF'
If \verb|KG_Verbose=0|, no message will be displayed. 
EOF
scp=<<'EOF'
export KG_VerboseLevel=0
mcut f=k,v i=dat.csv o=out.csv
mcut x=k,v i=dat.csv o=out.csv
EOF
run(scp,title,comment)
