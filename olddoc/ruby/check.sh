#!/usr/bin/env bash

function rmDateTime {
	sed 's/ 20..-...-.. ..:..:..//' |
	sed 's/__KGTMP.* / /' |
	sed 's/__KGTMP.*$/ /' |
	sed 's/test\.rb:.*:in//'
}

errCnt=0
function doDiff {
	echo -n "checking $1 ... "

	if [ ! -e outdat/$1 ] ; then
		echo "no data found"
	else
		rmDateTime < answer/$1 >xxans
		rmDateTime < outdat/$1 >xxout
		diff -q xxans xxout > xxrsl
		if [ -s xxrsl ] ; then
			errCnt=$(($errCnt+1))
			echo NG
		else
			echo OK
		fi
	fi
}

#doDiff log19.txt
#exit

for fn in `ls answer` ; do
	doDiff $fn
done

echo "不一致の件数は $errCnt 件でした"
echo 'ただし，log37.txtは実行時依存のためNGで正常'

