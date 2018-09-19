# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mslide'
db['title']='行ずらし'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
指定した項目の値を指定した行数ずらして出力する。
例えば、日別の株価データにおいて収益率(当日の株価/前日の株価)を計算するなど
レコード間の演算を行いたい場合に利用する。
典型的な例を :numref:`mslide_input` 〜 :numref:`mslide_out3` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mslide_input

  date,val
  4/6,1
  4/7,2
  4/8,3
  4/9,4




.. csv-table:: f=val:nextVal
  :header-rows: 1
  :name: mslide_out1

  date,val,nextVal
  4/6,1,2
  4/7,2,3
  4/8,3,4




.. csv-table:: f=val:nextVal -r
  :header-rows: 1
  :name: mslide_out2

  date,val,nextVal
  4/7,2,1
  4/8,3,2
  4/9,4,3




.. csv-table:: f=val t=2
  :header-rows: 1
  :name: mslide_out3

  date,val,val1,val2
  4/6,1,2,3
  4/7,2,3,4


:numref:`mslide_input` に示される入力データは日別の集計値が4日分示されており、
スーパーの売上推移や株価推移と考えればよい。
この入力データについて、
日々の増加率(ここでは簡単のために「増加率=翌日の値/当日の値」とする)
を計算することを考える。
入力データに示される日付4/6〜4/9について、
それぞれの日の値(val)を１行上にずらし、
新しい項目(newVal)として出力した結果が :numref:`mslide_out1` に示されている。
この出力結果に対してmcalコマンドでnextVal/valを計算すれば増加率が求められる。
ちなみに、4/9の行が消えているのは、4/9の行の次の行が存在しないからである。
存在しない時も-nオプションを指定することでNULL値を出力することができる。
:numref:`mslide_out1` は、下の行の値を上にずらしたが、-rオプションを指定することで、
逆に(上の行の値を下に)ずらすことも可能である( :numref:`mslide_out2` )。
さらに、t=を指定することで、スライドの回数を指定することもできる。
t=2で実行した結果を :numref:`mslide_out3` に示している。
これは " ``mslide f=val:val1 | mslide f=val1:val2`` "のように、
mslideを複数回実行するのと同じ効果がある。
なお、 ``t=`` を指定した場合、新たに出力される項目名は、
``f=`` で指定した項目名に、1から始まる連番が付与されたものとなる。
また ``t=`` と ``l=True`` を併用することで、最後にずらした結果のみを出力することも可能である。
mslideの機能はmwindowによく似ている。
mslideはレコード間の演算を項目演算として実現し、
一方で、mwindowはレコード間演算を行集計として実現している。
よって、mslideした後の演算はmcalやmselが主役となり、
一方でmwindowしたのちはmsumやmavgなどのデータ集約のコマンドが主役となる。

'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='i'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準入力'
param['text']='''
入力データを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='o'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準出力'
param['text']='''
出力データを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ずらす対象となる項目名を指定する。複数項目指定可能。
``t=`` を指定しないときは、コロンに続いて窓キーの項目名を指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q=True`` の指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、行をずらす。
``q=True`` オプションを指定しないとき、 ``s=`` パラメータは必須。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
ここで指定された項目の値を単位に処理する。
'''
db['params'].append(param)

param={}
param['kwd']='t'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ずらす回数を指定する。省略すれば ``t=1`` が設定される。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
逆方向に(上の値を下に)ずらす。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
次(前)の行がなくてもNULL値を出力する。
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
最後にずらした結果のみを出力する。
'''
db['params'].append(param)

db['comParams']='assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
