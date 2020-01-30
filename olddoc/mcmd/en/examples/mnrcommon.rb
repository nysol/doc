#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Date,Amount
20080123,10
20080203,10
20080203,20
20080203,45
200804l0,50
EOF
)}

File.open("ref1.csv","w"){|fpw| fpw.write(
<<'EOF'
Date,AmountF,AmountT
20080203,5,15
20080203,40,50
EOF
)}

############## Example 1
title="Basic Example"
comment=<<'EOF'
Select records where the transaction date is \verb|20080203| with transaction "Amount" greater than \verb|5| and less than \verb|15| or greater than \verb|40| and less than \verb|50|.
EOF
scp=<<'EOF'
more dat1.csv
more ref1.csv
mnrcommon k=Date m=ref1.csv R=AmountF,AmountT r=Amount%n i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Reverse selection"
comment=<<'EOF'
Add \verb|-r| option to reverse selection criteria.
EOF
scp=<<'EOF'
mnrcommon k=Date m=ref1.csv R=AmountF,AmountT r=Amount%n -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)
