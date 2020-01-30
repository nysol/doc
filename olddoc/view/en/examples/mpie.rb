#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
Age,Population
10,310504
20,552339
30,259034.5555
40,0450818
50,1231572
60,1215966
70,641667
EOF
)}

File.open("dat2.csv","w"){|fpw| fpw.write(
<<'EOF'
Pref,Age,Population
Nara,10,310504
Nara,20,552339
Nara,30,259034
Nara,40,450818
Nara,50,1231572
Nara,60,1215966
Nara,70,641667
Hokkaido,10,310504
Hokkaido,20,252339
Hokkaido,30,859034
Hokkaido,40,150818
Hokkaido,50,9231572
Hokkaido,60,4215966
Hokkaido,70,341667
EOF
)}

File.open("dat3.csv","w"){|fpw| fpw.write(
<<'EOF'
Gender,Age,ThemePark,Number
Male,30,Disney,100
Male,30,UFJ,59
Male,30,Umeyashiki,180
Male,40,Disney,200
Male,40,UFJ,3
Male,40,Umeyashiki,10
Male,50,Disney,110
Male,50,UFJ,40
Female,30,Umeyashiki,100
Female,30,Disney,80
Female,30,UFJ,200
Female,40,Disney,90
Female,40,UFJ,80
Female,40,Umeyashiki,120
Female,50,Disney,99
Female,50,UFJ,80
Female,50,Umeyashiki,110
EOF
)}


##############  Example 1
title="Draw a pie chart"
comment=<<'EOF'
Using the data \verb|dat1.csv|, set \verb|Age| as the unit of composition, draw a one dimensional pie chart  showing the population.
The output of the pie chart can be viewed in the web browser. Note that in the pie chart, when you place the mouse cursor over the bar chart, details of the unit of composition is shown in a pop-up box. The graph can also be moved by dragging the mouse, and the size of the graph can be scaled by scrolling the mouse.
EOF
scp=<<'EOF'
more dat1.csv
mpie.rb i=dat1.csv v=Population f=Age o=result1.html
head result1.html
EOF
run(scp,title,comment)

##############  Example 2
title="Draw a one dimensional pie chart"
comment=<<'EOF'
Using the data \verb|dat2.csv|, set \verb|Age| as the unit of composition, draw the pie chart showing the population by age. Specify \verb|Pref| at \verb|k=| parameter, which is designated on the x-axis as a one-dimensional pie chart. Specify the title of the graph at \verb|title=| parameter.
EOF
scp=<<'EOF'
more dat2.csv
mpie.rb i=dat2.csv k=Pref v=Population f=Age o=result2.html title='Population of Nara and Hokkaido by Age Group'
head result2.html
EOF
run(scp,title,comment)

##############  Example 3
title="Draw a two dimensional pie chart"
comment=<<'EOF'
Using the data \verb|dat3.csv|, set \verb|ThemePark| as the unit of composition, draw the pie chart showing the theme parks by \verb|Number| field, and specify the radius at 100 at the \verb|pr=| parameter. Specify \verb|Gender| and \verb|Age| at \verb|k=| parameter, which designates Gender on the x-axis, and Age on y-axis.
EOF
scp=<<'EOF'
more dat3.csv
mpie.rb i=dat3.csv k=Gender,Age v=Number f=ThemePark o=result3.html
head result3.html
EOF
run(scp,title,comment)

