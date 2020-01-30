#!/bin/bash

# $1: 件数の単位　通常は10000を指定する．テスト実行の時は1を指定すると短時間で実行可能となる．

#データを作成する
# $1:行数
# $2:keyの種類
function mkdata_sub {
	no=$(($1*$unit))
	#echo mnewrand min=10000000 max=$((9999999+$2)) -int S=1 a=key l=$no

	# msortf用データ
	mnewrand min=10000000 max=$((9999999+$2)) -int S=1 a=key l=$no |
	mcal c='randi(100,299,2)'  a=fld1 |
	mcal c='randi(100,299,3)'  a=fld2 |
	mcal c='randi(100,299,4)'  a=fld3 |
	mcal c='randi(100,299,5)'  a=fld4 |
	mcal c='randi(-100,-1,6)'  a=fldn  o=indat/$3_msortf.csv

	# msort用データ
	#cp indat/$3_msortf.csv indat/$3_msort.csv
	# xtsort用データ
	csv2xt -F -i indat/$3_msortf.csv -o indat/$3_xtsort.xt
	# sort用データ
	xt2txt -i indat/$3_xtsort.xt -o indat/$3_sort.txt
	#cp indat/$3_sort.txt indat/$3_sort.txt
}


# ソート済みデータの作成
function mksortdata {

	# msortf 文字列昇順降順
	msortf f=key   i=indat/$1_msortf.csv o=indat/$1_asc_msortf.csv
	msortf f=key%r i=indat/$1_msortf.csv o=indat/$1_dec_msortf.csv

	# xtsortf 文字列昇順降順
	xtsort -k key   -i indat/$1_xtsort.xt -o indat/$1_asc_xtsort.xt
	xtsort -k key%r -i indat/$1_xtsort.xt -o indat/$1_dec_xtsort.xt

	# sort 文字列昇順降順
	#xt2txt -i indat/$1_xtsort.xt | sort    > indat/$1_asc_sort.txt
	#xt2txt -i indat/$1_xtsort.xt | sort -r > indat/$1_dec_sort.txt

	# sort 文字列昇順降順
	xt2txt -i indat/$1_xtsort.xt | sort -k1    > indat/$1_asc_sort.txt
	xt2txt -i indat/$1_xtsort.xt | sort -k1 -r > indat/$1_dec_sort.txt

	# msort 文字列昇順降順
	#msort    i=indat/$1_msort.csv o=indat/$1_asc_msort.csv

	echo 'key,fld1,fld2,fld3,fld4,fldn' >xxhead
	#cat xxhead indat/$1_dec_sort.txt >indat/$1_dec_msort.csv
	
	# msortf 数値昇順降順
	msortf f=key%n  i=indat/$1_msortf.csv o=indat/$1_asc_n_msortf.csv
	msortf f=key%nr i=indat/$1_msortf.csv o=indat/$1_dec_n_msortf.csv

	# xtsort 数値昇順降順
	xtsort -k key%n  -i indat/$1_xtsort.xt -o indat/$1_asc_n_xtsort.xt
	xtsort -k key%nr -i indat/$1_xtsort.xt -o indat/$1_dec_n_xtsort.xt

	# sort 数値昇順降順
	sort -k1 -n    <indat/$1_sort.txt > indat/$1_asc_n_sort.txt
	sort -k1 -r -n <indat/$1_sort.txt > indat/$1_dec_n_sort.txt

}

# 行数単位
unit=$1

mkdir -p indat

# キーの種類数比較用のデータ作成
mkdata_sub 100 2        100_2
mkdata_sub 100 10       100_10
mkdata_sub 100 100      100_100
mkdata_sub 100 1000     100_1000
mkdata_sub 100 10000    100_10000
mkdata_sub 100 90000000 100_rand

# 数値ソーティング用データの作成
mksortdata 100_rand

# データ件数比較用のデータ作成(rand)
#mkdata_sub 1000 90000000 100_rand
mkdata_sub 200  90000000 200_rand
mkdata_sub 300  90000000 300_rand
mkdata_sub 400  90000000 400_rand
mkdata_sub 500  90000000 500_rand
mkdata_sub 600  90000000 600_rand
mkdata_sub 700  90000000 700_rand
mkdata_sub 800  90000000 800_rand
mkdata_sub 900  90000000 900_rand
mkdata_sub 1000 90000000 1000_rand

# データ件数比較用のデータ作成(100)
#mkdata_sub 1000  100 100_100
mkdata_sub 200  100 200_100
mkdata_sub 300  100 300_100
mkdata_sub 400  100 400_100
mkdata_sub 500  100 500_100
mkdata_sub 600  100 600_100
mkdata_sub 700  100 700_100
mkdata_sub 800  100 800_100
mkdata_sub 900  100 900_100
mkdata_sub 1000 100 1000_100

