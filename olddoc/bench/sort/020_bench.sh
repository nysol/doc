#!/bin/bash

export KG_VerboseLevel=1


# msort,msortf,xtsort,sort,sort_k1 全て実行する場合
function bench1 {
	logfile=log/bench1.log

	echo R msortf $1
	echo R msortf $1 &> xxlog1
	cat <indat/$1_msortf.csv >/dev/null
	(time msortf f=key i=indat/$1_msortf.csv o=/dev/null) &> xxlog2
	cat xxlog1 xxlog2 >>$logfile

	echo R xtsort $1
	echo R xtsort $1 &> xxlog1
	cat <indat/$1_xtsort.xt >/dev/null
	(time xtsort -k key -i indat/$1_xtsort.xt -o /dev/null) &> xxlog2
	cat xxlog1 xxlog2 >>$logfile

	echo R sort $1
	echo R sort $1 &> xxlog1
	cat <indat/$1_sort.txt >/dev/null
	(time sort -k1 indat/$1_sort.txt >/dev/null) &> xxlog2
	cat xxlog1 xxlog2 >>$logfile
}

#数値ソートの場合
function bench2 {
	logfile=log/bench2.log

	echo R msortf_n $1
	echo R msortf_n $1 &> xxlog1
	cat <indat/$1_msortf.csv >/dev/null
	(time msortf f=key%n i=indat/$1_msortf.csv o=/dev/null) &> xxlog2
	cat xxlog1 xxlog2 >>$logfile

	echo R xtsort_n $1
	echo R xtsort_n $1 &> xxlog1
	cat <indat/$1_xtsort.xt >/dev/null
	(time xtsort -k key%n -i indat/$1_xtsort.xt -o /dev/null) &> xxlog2
	cat xxlog1 xxlog2 >>$logfile

	echo R sort_n $1
	echo R sort_n $1 &> xxlog1
	cat <indat/$1_sort.txt >/dev/null
	(time sort -k1 -n indat/$1_sort.txt >/dev/null) &> xxlog2
	cat xxlog1 xxlog2 >>$logfile
}


#文字ソートの場合
function bench3 {
	logfile=log/bench3.log

	echo R msortf $1
	echo R msortf $1 &> xxlog1
	cat <indat/$1_msortf.csv >/dev/null
	(time msortf f=key i=indat/$1_msortf.csv o=/dev/null) &> xxlog2
	cat xxlog1 xxlog2 >>$logfile

	echo R xtsort $1
	echo R xtsort $1 &> xxlog1
	cat <indat/$1_xtsort.xt >/dev/null
	(time xtsort -k key -i indat/$1_xtsort.xt -o /dev/null) &> xxlog2
	cat xxlog1 xxlog2 >>$logfile
}

# 繰り返し回数
rcnt=10

# キーの種類数比較実験
function exp1 {
	rm log/bench1.log
	n=0
	while [ $n -lt $rcnt ]
	do
		bench1 100_2
		bench1 100_10
		bench1 100_100
		bench1 100_1000
		bench1 100_10000
		bench1 100_rand
		bench1 100_rand_asc
		bench1 100_rand_dec
		n=$(($n + 1))
	done
}

# 数値ソート実験
function exp2 {
	rm log/bench2.log
	n=0
	while [ $n -lt $rcnt ]
	do
		bench2 100_2
		bench2 100_10
		bench2 100_100
		bench2 100_1000
		bench2 100_10000
		bench2 100_rand
		bench2 100_rand_asc_n
		bench2 100_rand_dec_n
		n=$(($n + 1))
	done
}

# 件数による比較実験
function exp3 {
	rm log/bench3.log
	n=0
	while [ $n -lt $rcnt ]
	do
		bench3 100_rand
		bench3 200_rand
		bench3 300_rand
		bench3 400_rand
		bench3 500_rand
		bench3 600_rand
		bench3 700_rand
		bench3 800_rand
		bench3 900_rand
		bench3 1000_rand
		bench3 100_100
		bench3 200_100
		bench3 300_100
		bench3 400_100
		bench3 500_100
		bench3 600_100
		bench3 700_100
		bench3 800_100
		bench3 900_100
		bench3 1000_100
		n=$(($n + 1))
	done
}

exp1
exp2
exp3

