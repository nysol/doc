# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvuniq'
db['title']='ベクトル要素の単一化'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
ベクトル型の項目の要素を単一化する。
内部的にはtree構造を利用して単一化をしているので、
出力される要素の順序は文字列昇順に並び変わる。
一方で、 ``n=True`` オプションを指定すると、
ベクトルを系列として考え、
要素を先頭から順番に走査し、互いに隣接した要素のみを単一化し出力する。
典型的な例を :numref:`mvuniq_out1` , :numref:`mvuniq_out2` に示す。
:numref:`mvuniq_out1` では、全ての要素が単一化されているのが分かる。
一方で、 ``n=True`` オプションを指定して実行すると、
:numref:`mvuniq_out2` の３行目に見られるように、
互いに隣接する ``b`` のみが単一化される。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvuniq_input

  no,items
  1,b a a
  2,a a b b b
  3,a b b a
  4,a b c




.. csv-table:: 基本的な例
  :header-rows: 1
  :name: mvuniq_out1

  no,items
  1,a b
  2,a b
  3,a b
  4,a b c




.. csv-table:: ベクトルを系列と考え、互いに隣り合う同じ要素のみを単一化する例
  :header-rows: 1
  :name: mvuniq_out2

  no,items
  1,b a
  2,a b
  3,a b a
  4,a b c



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
param['kwd']='vf'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
単一化する対象項目名を指定する。複数項目指定可能。
結果の項目名を変更したいときは、:(コロン)に続けて新項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``vf=`` で:(コロン)に続けて指定した項目名で、新たな項目が追加される。
なお ``A=True`` オプションを指定した場合、 ``vf=`` パラメータで指定するすべての
項目に新項目名を指定しなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
ベクトルを系列と考え隣接する同一要素のみ単一化する
'''
db['params'].append(param)

param={}
param['kwd']='delim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ベクトル型データの区切り文字を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,delim,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
