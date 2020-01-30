#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
key1,key2,v1,v2
A,X,1,a
A,Y,2,b
A,Y,3,c
B,X,4,d
B,Y,5,e
EOF
)}

File.open("form1.txt","w"){|fpw| fpw.write(
<<'EOF'
%LINEDATA
%key1% %v1%
%LINEEND
EOF
)}

File.open("form2.txt","w"){|fpw| fpw.write(
<<'EOF'
%LINEDATA
%key1% %v1%
       %key2% %v2%
%LINEEND
EOF
)}

File.open("form3.txt","w"){|fpw| fpw.write(
<<'EOF'
Head Area
%KEYHEAD
KeyHead=%key1% %key2% %v1% %v2%
%KEYEND
%LINEDATA
%v1%-%v2%
%LINEEND
%KEYFOOT
KeyFoot=%key1% %key2% %v1% %v2%
%KEYEND
Foot Area
EOF
)}

File.open("form4.txt","w"){|fpw| fpw.write(
<<'EOF'
\documentclass{article}
\begin{document}
\begin{table}
\begin{tabular}{l|l|r|r}
\hline
key1 & key2 & v1 & v2 \\
\hline
%KEYHEAD
%key1% & %key2% & %v1% & %v2% \\
%KEYEND
%LINEDATA
  & %key2% & %v1% & %v2% \\
%LINEEND
%KEYFOOT
\hline
%KEYEND
\end{tabular}
\end{table}
\end{document}
EOF
)}

############## 例1
title="Example 1: Basic example 1"
comment=<<'EOF'
Two fields in the CSV file, \verb|key1| and \verb|v1|, are output with spaces as delimiters.
EOF
scp=<<'EOF'
more dat1.csv
more form1.txt
mcsvconv m=form1.txt i=dat1.csv o=rsl1.txt
more rsl1.txt
EOF
run(scp,title,comment)

############## 例2
title="Example 2: Basic example 2"
comment=<<'EOF'
Data is output in two rows, with the second rows indented.
EOF
scp=<<'EOF'
more dat1.csv
more form2.txt
mcsvconv m=form2.txt i=dat1.csv o=rsl2.txt
more rsl2.txt
EOF
run(scp,title,comment)

############## 例3
title="Example 3: Specifying keys"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more form3.txt
mcsvconv k=key1 m=form3.txt i=dat1.csv o=rsl3.txt
more rsl3.txt
EOF
run(scp,title,comment)

############## 例4
title="Example 4: Outputting results as tex data"
comment=<<'EOF'
EOF
scp=<<'EOF'
more dat1.csv
more form3.txt
mcsvconv k=key1 m=form4.txt i=dat1.csv o=rsl4.tex
more rsl4.tex
EOF
run(scp,title,comment)

