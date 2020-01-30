


# キーの種類数別コマンド別文字列ソート速度比較
# log/bench1.csv
# command,data_set,real,user,sys,user_sys
# msortf,100_2,0.011,0.003,0.006,0.009
# xtsort,100_2,0.005,0.001,0.002,0.003
function run_key {
	msortf f=dsOrder,cmdOrder i=log/bench1_avg.csv |
	mcross k=name1 s=command f=real |
	mcut   f=name1:data_set,msortf,xtsort o=csv/key.csv

	mcut f=data_set,msortf,xtsort -nfno i=csv/key.csv |
	sed 's/,/ /g' >xxgp

	# gnuplotによるbarchart描画
	gnuplot -p << "EOF"
	set terminal postscript
	set output 'figure/key.eps'

	set style fill solid border lc rgb "black"
	set boxwidth 1
	#set xtics rotate
	#set style histogram clustered #ヒストグラム
	##set xtics rotate
	set yrange[0:]
	plot "xxgp" using ($0*3+0):2:xtic(1) with boxes lc rgb "gray" title "msortf",\
	     "xxgp" using ($0*3+1):3         with boxes lc rgb "white" title "xtsort"

	set terminal postscript eps
	set output "figure/key.eps"
	replot
EOF
}

# キーの種類数別コマンド別数値ソート速度比較
# log/bench2.csv
# command,data_set,real,user,sys,user_sys
#command,data_set,real,user,sys,user_sys
#msortf_n,100_2,1.412,1.121,0.216,1.337
#xtsort_n,100_2,2.715,1.981,0.295,2.276
function run_num {
	msortf f=dsOrder,cmdOrder i=log/bench2_avg.csv |
	mcross k=name1 s=command f=real |
	mcut   f=name1:data_set,msortf_n,xtsort_n o=csv/num.csv

	mcut f=data_set,msortf_n,xtsort_n -nfno i=csv/num.csv |
	sed 's/,/ /g' >xxgp

	# gnuplotによるbarchart描画
	gnuplot -p << "EOF"
	set terminal postscript
	set output 'figure/num.eps'

	set style fill solid border lc rgb "black"
	set boxwidth 1
	#set xtics rotate
	#set style histogram clustered #ヒストグラム
	##set xtics rotate
	set yrange[0:]
	plot "xxgp" using ($0*3+0):2:xtic(1) with boxes lc rgb "gray" title "msortf",\
	     "xxgp" using ($0*3+1):3         with boxes lc rgb "white" title "xtsort"

	set terminal postscript eps
	set output "figure/num.eps"
	replot
EOF
}

# データ件数別コマンド別文字列ソート速度比較(キーは乱数)
# log/bench3.csv
# command,data_set,real,user,sys,user_sys
# msortf,100_rand,1.565,1.975,0.23,2.205
# xtsort,100_rand,1.267,0.962,0.121,1.083
function run_line_rand {
	mselstr f=data_set v=_rand -sub i=log/bench3_avg.csv |
	msortf  f=dsOrder,cmdOrder |
	mcross  k=name2 s=command f=real |
	mcut    f=name2:data_set,msortf,xtsort o=csv/line_rand.csv

	mcut f=data_set,msortf,xtsort -nfno i=csv/line_rand.csv |
	sed 's/,/ /g' >xxgp

	# gnuplotによるlinechart描画
	gnuplot -p << "EOF"
	set terminal postscript
	set output 'figure/line_rand.eps'

	#set xtics rotate
	set yrange[0:]
	plot "xxgp" using 2:xtic(1) with lines lc rgb "blue"  title "msortf",\
	     "xxgp" using 3         with lines lc rgb "red"   title "xtsort"

	set terminal postscript eps
	set output "figure/line_rand.eps"
	replot
EOF
}

# データ件数別コマンド別文字列ソート速度比較(キーは乱数)
# log/bench3.csv
# command,data_set,real,user,sys,user_sys
# msortf,100_rand,1.565,1.975,0.23,2.205
# xtsort,100_rand,1.267,0.962,0.121,1.083
function run_line_100 {
	mselstr f=data_set v=_100 -sub i=log/bench3_avg.csv |
	msortf  f=dsOrder,cmdOrder |
	mcross k=name2 s=command f=real |
	mcut   f=name2:data_set,msortf,xtsort o=csv/line_100.csv

	mcut f=data_set,msortf,xtsort -nfno i=csv/line_100.csv |
	sed 's/,/ /g' >xxgp

	# gnuplotによるlinechart描画
	gnuplot -p << "EOF"
	set terminal postscript
	set output 'figure/line_100.eps'

	#set xtics rotate
	set yrange[0:]
	plot "xxgp" using 2:xtic(1) with lines lc rgb "blue"  title "msortf",\
	     "xxgp" using 3         with lines lc rgb "red"   title "xtsort"

	set terminal postscript eps
	set output "figure/line_100.eps"
	replot
EOF
}

rm -rf figure
mkdir -p figure
rm -rf csv
mkdir -p csv

run_key
run_num
run_line_rand
run_line_100

