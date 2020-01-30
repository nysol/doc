#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Val,Sum
A,29,300
B,35,250
C,15,200
D,23,150
E,10,100
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
Date
20090101
20090101
20090102
20090103
20090103
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Val,Sum
A,3,300
B,1,250
C,2,250
D,1,150
E,1,100
EOF
)}

File.open("dat4.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Val,Sum
A,1,100
B,1,150
C,1,250
D,2,250
E,3,300
EOF
)}

############## Example 1
title="Sequential numbers"
comment=<<'EOF'
Generate sequential numbers for each value in ascending order in the \verb|Customer| column. Name the sequence as \verb|No| in a new column.
EOF
scp=<<'EOF'
more dat1.csv
mnumber s=Customer a=No i=dat1.csv o=rsl1.csv
more rsl1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Serialize the Date column"
comment=<<'EOF'
Sequentially number items in the \verb|Date| column according to earliest date to latest date. Use same sequence number (\verb|No|) for same \verb|Date|. Save the sequence in a new column named \verb|"No"|.
EOF
scp=<<'EOF'
more dat2.csv
mnumber k=Date a=No -B i=dat2.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)

############## Example 3
title="Serialize the Sum column (use same alphabet for same Rank order)"
comment=<<'EOF'
Create a alphabetical sequence according to the \verb|Sum| column which is arranged in descending order. Save the sequence in a new column named \verb|“Rank”|. Assign the same alphabet character to items with the same values.
EOF
scp=<<'EOF'
more dat3.csv
mnumber a=Rank e=same s=Sum%nr S=A  i=dat3.csv o=rsl3.csv
more rsl3.csv
EOF
run(scp,title,comment)

############## Example 4
title="Serialize the Sum column (sequential numbers for same Rank order)"
comment=<<'EOF'
Number records sequentially according to \verb|Sum| column (sum arranged in descending order), and save serials in the \verb|"Rank"| column. For items with same rank order, assign sequential numbers according to sort order.
EOF
scp=<<'EOF'
mnumber a=Rank e=seq s=Sum%nr i=dat3.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Serialize the Sum column (Same No for same Rank)"
comment=<<'EOF'
Number records sequentially according to \verb|Sum| column (sum arranged in descending order), and save the numbers in the \verb|“Rank”| column. Assign the same No to records with the same Rank order.
EOF
scp=<<'EOF'
mnumber a=Rank e=same s=Sum%nr i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## Example 6
title="Serialize the Sum column (duplicate numbers for same Rank and skip number for next record)"
comment=<<'EOF'
Number records sequentially according to \verb|Sum| column (sum arranged in descending order), and save the numbers is the “Rank” column. Assign same \verb|RankNo| number to records with same rank order, subsequent No is skipped for the following record.
EOF
scp=<<'EOF'
mnumber a=Rank e=skip s=Sum%nr i=dat3.csv o=rsl6.csv
more rsl6.csv
EOF
run(scp,title,comment)

############## Example 7
title="Number sequence starting from 10"
comment=<<'EOF'
Serialize the \verb|Sum| column sequentially from 10 with items, where values of sum is arranged in ascending order. Save the serials in the \verb|"Score"| column. Assign same RankNo to records with same Rank order , subsequent No is skipped for the following record.
EOF
scp=<<'EOF'
more dat4.csv
mnumber a=Score e=same s=Sum%n S=10 i=dat4.csv o=rsl7.csv
more rsl7.csv
EOF
run(scp,title,comment)

############## Example 8
title="Start sequence from 10 with an interval of 5"
comment=<<'EOF'
Number the \verb|Sum| column sequentially from 10 at an interval of 5, where values of sum is arranged in ascending order. Save the serials in the \verb|“Score”| column. Assign the same number to records with the same Rank order.
EOF
scp=<<'EOF'
mnumber a=Score e=same s=Sum%n S=10 I=5 i=dat4.csv o=rsl8.csv
more rsl8.csv
EOF
run(scp,title,comment)
