#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Product,Amount
apple,100
milk,350
orange,100
pineapplejuice,500
wine,1000
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Product,Amount
A,apple,100
A,milk,350
B,orange,100
B,orange,100
B,pineapple,500
B,wine,1000
C,apple,100
C,orange,100
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
Product,Amount
fruit:柿,100
fruit:桃,250
fruit:葡萄,300
fruit:梨,450
fruit:苺,500
EOF
)}

File.open("dat4.csv","w"){|fpw| fpw.write(
<<'EOF'
Customer,Product,Amount,Gender,Date,PreviousDate
A,apple,100,1,2013/01/04,2013/01/01
A,milk,350,1,2013/04/04,2011/05/06
B,orange,100,2,2012/11/11,2011/12/12
B,orange,100,2,2013/05/30,2012/11/11
B,pineapple,500,2,2013/04/15,2013/04/01
B,wine,1000,2,2012/12/24,2011/12/24
C,apple,100,2,2013/02/14,NULL
C,orange,100,2,2013/02/14,2013/01/31
D,orange,100,2,2011/10/28,NULL
EOF
)}

############## Example 1
title="Basic example"
comment=<<'EOF'
Select records matching \verb|apple| and \verb|orange| in the Product field , print matching results to \verb|rsl1.csv| file. Unmatched records such as \verb|pineapplejuice| will be saved to other.csv file using the parameter \verb|u=oth1.csv|.
EOF
scp=<<'EOF'
more dat1.csv
mselstr f=Product v=apple,orange u=oth1.csv i=dat1.csv o=rsl1.csv
more rsl1.csv
more oth1.csv
EOF
run(scp,title,comment)

############## Example 2
title="Remove records"
comment=<<'EOF'
Contrary to example 1, remove records matching keywords \verb|apple| and \verb|orange| using the \verb|-r| option, the output is saved to \verb|rsl2.csv| file.
EOF
scp=<<'EOF'
mselstr f=Product  v=apple,orange -r i=dat1.csv o=rsl2.csv
more rsl2.csv
EOF
run(scp,title,comment)


############## Example 3
title="Select based on the key unit"
comment=<<'EOF'
Select all records of customer who have purchased oranges by specifying \verb|Customer| at the \verb|k=| parameter. Save unmatched records to \verb|oth2.csv|.
EOF
scp=<<'EOF'
more dat2.csv
mselstr k=Customer f=Product v=orange u=oth2.csv i=dat2.csv o=rsl3.csv
more rsl3.csv
more oth2.csv
EOF
run(scp,title,comment)

############## Example 4
title="Partial match"
comment=<<'EOF'
Select records where the \verb|Product| field contain the keyword \verb|apple|, and save the output to a file named  \verb|rsl4.csv|. Records with partial match such as \verb|pine(apple)juice| will also be saved in the output file \verb|rsl4.csv|.
EOF
scp=<<'EOF'
mselstr f=Product v=apple -sub i=dat1.csv o=rsl4.csv
more rsl4.csv
EOF
run(scp,title,comment)

############## Example 5
title="Wide character substring match"
comment=<<'EOF'
Select records where the \verb|Product| field contains wide characters  "柿", "桃", and "葡萄".

Matching maybe based on single byte character if the query string includes wide character, the query string maybe interpreted as multibyte character for matching. Therefore, it is necessary indicate wide character in the query string with \verb|-W| option.
EOF
scp=<<'EOF'
more dat3.csv
mselstr f=Product v=柿,桃,葡萄 -sub -W i=dat3.csv o=rsl5.csv
more rsl5.csv
EOF
run(scp,title,comment)

############## Example 6
title="Select product(s) with consecutive purchases in 2013."
comment=<<'EOF'
Use the \verb|-F| option to select transactions where the date of purchase and the previous date of purchase for the product both took place in 2013.  Save the query results to an output file \verb|rsl6.csv|. Save unmatched records to \verb|oth3.csv|.

EOF
scp=<<'EOF'
more dat4.csv
mselstr f=Date,PreviousDate -F -sub v=2013 u=oth3.csv i=dat4.csv o=rsl6.csv
more rsl6.csv
more oth3.csv
EOF
run(scp,title,comment)

############## Example 7
title="Extract all transactions of customers who have consecutive purchases in 2013"
comment=<<'EOF'
Use \verb|k=| parameter to select all transactions of customers who have purchased a product with date of purchase and date of previous purchase both took place in 2013. Save unmatched records to a file \verb|oth4.csv|.
EOF
scp=<<'EOF'
mselstr k=Customer f=Date,PreviousDate -F -sub v=2013 u=oth4.csv i=dat4.csv o=rsl7.csv
more rsl7.csv
more oth4.csv
EOF
run(scp,title,comment)

############## Example 8
title="Select new customer(s) who purchased in 2013"
comment=<<'EOF'
Use the \verb|-R| option to select all transactions of new customer(s) who made their first purchase in 2013, where date of previous purchase is NULL.
Write the query results to an output file ¥verb|rsl8.csv|, and save unmatched records to \verb|oth5.csv|. 

EOF
scp=<<'EOF'
mselstr k=Customer f=Date,PreviousDate -F -R -sub v=2013,NULL u=oth5.csv i=dat4.csv o=rsl8.csv
more rsl8.csv
more oth5.csv
EOF
run(scp,title,comment)
