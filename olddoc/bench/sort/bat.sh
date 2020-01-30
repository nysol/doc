#!/bin/bash

#./010_mkdat.sh 1   # 動作確認用に引数1で試す。本番は以下、引数10000で実行
#./010_mkdat.sh 10000  

#./020_bench.sh
./030_clean.sh
./040_mkchart.sh
./050_mktable.rb
