
function mkmf {
cat <<EOF >xxcmdOrder
command,cmdOrder,strnum,text
msortf,1,1,msortf f=key
msortf_n,4,2,msortf f=key\\%n
sort,3,1,sort -k1
sort_n,6,2,sort -k1 -n
xtsort,2,1,xtsort -k key
xtsort_n,5,2,xtsort -k key\\%n
EOF

cat <<EOF >xxdsOrder
data_set,dsOrder,name1,name2
1000_100,30,,1000
1000_rand,18,,1000
100_10,02,10,
100_100,03,100,100
100_1000,04,1000,
100_10000,05,10000,
100_2,01,2,
100_rand,06,rand,100
100_rand_asc,07,asc,
100_rand_dec,08,dec,
200_100,22,,200
200_rand,10,,200
300_100,23,,300
300_rand,11,,300
400_100,24,,400
400_rand,12,,400
500_100,25,,500
500_rand,13,,500
600_100,26,,600
600_rand,14,,600
700_100,27,,700
700_rand,15,,700
800_100,28,,800
800_rand,16,,800
900_100,29,,900
900_rand,17,,900
EOF
}

function clean {

grep -v '^END' |
grep -v '^#END' |
grep -v '^$' |
tr '\t' ' ' |
sed 's/real *//' |
sed 's/user *//' |
sed 's/sys *//' |
sed 's/s$//' |
awk '{
	if($1=="R"){
		if(NR!=1){
			print par,sec[1],sec[2],sec[3],sec[2]+sec[3];
		}
		type=1;
		par=$0;
	}else{
		split($0,ar,"m");
		sec[type]=60*ar[1]+ar[2];
		type++;
	}
}END{
	print par,sec[1],sec[2],sec[3],sec[2]+sec[3];
}
' |
sed 's/asc_n/asc/' |
sed 's/dec_n/dec/' |
sed 's/^R //' |
awk 'BEGIN{print "command,data_set,real,user,sys,user_sys";}{printf("%s,%s,%s,%s,%s,%s\n",$1,$2,$3,$4,$5,$6);}'

}

clean <log/bench1.log >log/bench1.csv
clean <log/bench2.log >log/bench2.csv
clean <log/bench3.log >log/bench3.csv

mkmf

mcat   i=log/bench1.csv |
mcut   f=data_set,command,real  |
msortf f=data_set,command,real%n  |
mbest  k=data_set,command from=1 to=1 -r |
msortf f=data_set,command,real%rn  |
mbest  k=data_set,command from=1 to=1 -r |
mavg   k=data_set,command f=real |
mjoin  k=data_set m=xxdsOrder f=dsOrder,name1,name2 |
msortf f=command |
mjoin  k=command m=xxcmdOrder f=cmdOrder |
msortf f=data_set,command o=log/bench1_avg.csv

mcat   i=log/bench2.csv |
mcut   f=data_set,command,real  |
msortf f=data_set,command,real%n  |
mbest  k=data_set,command from=1 to=1 -r |
msortf f=data_set,command,real%rn  |
mbest  k=data_set,command from=1 to=1 -r |
mavg   k=data_set,command f=real |
mjoin  k=data_set m=xxdsOrder f=dsOrder,name1,name2 |
msortf f=command |
mjoin  k=command m=xxcmdOrder f=cmdOrder |
msortf f=data_set,command o=log/bench2_avg.csv

mcat   i=log/bench3.csv |
mcut   f=data_set,command,real  |
msortf f=data_set,command,real%n  |
mbest  k=data_set,command from=1 to=1 -r |
msortf f=data_set,command,real%rn  |
mbest  k=data_set,command from=1 to=1 -r |
mavg   k=data_set,command f=real |
mjoin  k=data_set m=xxdsOrder f=dsOrder,name1,name2 |
msortf f=command |
mjoin  k=command m=xxcmdOrder f=cmdOrder |
msortf f=data_set,command o=log/bench3_avg.csv


