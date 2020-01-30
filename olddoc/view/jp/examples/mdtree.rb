#!/usr/bin/env ruby
# coding: utf-8
require "../../../scp/mkTex.rb"

File.open("dat1.csv","w"){|fpw| fpw.write(
<<'EOF'
性別,来店距離,購入パターン,入院歴
男,1.2,ABCAAA,あり
男,10.5,BCDADD,あり
男,0.5,AAAA,なし
男,2.0,BBCC,なし
男,3.1,DEDDA,あり
女,0.7,CCCAA,なし
女,1.5,DDDEEE,あり
女,2.6,BACD,あり
女,3.5,ABBB,あり
女,4.0,DDDD,あり
女,2.1,DEDE,なし
男,1.2,ABCAAA,あり
男,10.5,BCDADD,あり
男,0.5,AAAA,なし
男,2.0,BBCC,なし
男,3.1,DEDDA,あり
男,0.7,CCCAA,なし
男,1.5,DDDEEE,なし
男,2.6,BACD,あり
男,3.5,ABBB,あり
男,4.0,DDDD,あり
男,2.1,DEDE,なし
男,1.2,ABCAAA,あり
男,10.5,BCDADDA,あり
男,0.5,AAAAA,なし
男,2.0,BBCCA,なし
男,3.1,DEDDA,あり
男,0.7,CCCAA,なし
男,1.5,ADDDEEE,あり
男,2.6,BACD,あり
男,3.5,ABBB,あり
男,4.0,DDDD,あり
女,2.1,DEDE,なし
女,1.2,ABCAAA,あり
女,10.5,BCDADD,あり
女,0.5,AAAA,なし
女,2.0,BBCC,なし
女,3.1,DEDDA,あり
女,0.7,CCCAA,なし
女,1.5,DDDEEE,あり
女,2.6,BACD,あり
女,3.5,ABBB,あり
女,4.0,DDDD,あり
女,2.1,DEDE,なし
女,1.2,ABCAAA,あり
女,10.5,BCDADD,あり
女,0.5,AAAA,なし
女,2.0,BBCC,なし
女,3.1,DEDDA,あり
女,0.7,CCCAA,なし
女,1.5,DDDEEE,あり
女,2.6,BACD,あり
女,3.5,ABBB,あり
女,1.0,DDDD,あり
女,2.5,DEDE,なし
女,2.5,ABBB,あり
女,1.0,DDDD,あり
女,1.1,DEDE,なし
女,2.2,ABCAAA,あり
女,10.5,BCDADD,あり
女,1.5,AAAA,なし
女,2.6,BBCC,なし
女,3.3,DEDDA,あり
女,1.7,CCCAA,なし
女,1.5,DDDEEE,あり
女,2.6,BACD,あり
女,3.9,ABBB,あり
女,4.5,DDDD,あり
女,2.1,DEDE,なし
女,3.9,BABB,あり
男,4.5,BAA,なし
女,2.1,DEDE,なし
男,3.9,BABB,あり
女,3.9,BABB,あり
男,4.5,BAA,なし
女,2.1,DEDE,なし
男,3.9,BABB,あり
女,3.9,BABB,あり
男,4.5,BAA,なし
女,2.1,DEDE,なし
男,3.9,BABB,あり
EOF
)}

############## 例1
title="基本例"
comment=<<'EOF'
前節の解説で用いてる例。
EOF
scp=<<'EOF'
cat dat1.csv
mbonsai c=入院歴 n=来店距離 p=購入パターン d=性別 i=dat1.csv O=outdat
mdtree.rb i=outdat/model.pmml o=model1.html
mdtree.rb alpha=0.1 i=outdat/model.pmml o=model2.html
head model1.html
head model2.html
EOF
run(scp,title,comment)

