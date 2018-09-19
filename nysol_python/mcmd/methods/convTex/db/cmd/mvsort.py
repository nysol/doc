# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvsort'
db['title']='ベクトル要素のソート'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
ベクトル型の項目をソートする。
ベクトル型の項目とは、 :numref:`mvsort_input` のitems項目のように、
スペースで区切られた複数の文字列を値として持つ項目である。
典型的な例を :numref:`mvsort_input` 〜 :numref:`mvsort_out3` に示す。
オプションに何も指定しなければ文字列昇順に並べられ( :numref:`mvsort_out1` )、
項目名の後ろに ``%`` に続けて ``n`` を付けることで数値順に並べられる( :numref:`mvsort_out2` )。
ただし、ベクトルにアルファベットや漢字が含まれる場合の動作は不定である。
また項目名の後ろに ``r`` を指定することで逆順に並べることもできる( :numref:`mvsort_out3` )。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvsort_input

  no,items
  1,2 1 13
  2,4 5 2 5
  3,112 14
  4,5 31




.. csv-table:: 基本的な利用:ベクトルの要素を文字列昇順に並べる
  :header-rows: 1
  :name: mvsort_out1

  no,items
  1,1 13 2
  2,2 4 5 5
  3,112 14
  4,31 5




.. csv-table:: 数値昇順で並べる
  :header-rows: 1
  :name: mvsort_out2

  no,items
  1,1 2 13
  2,2 4 5 5
  3,14 112
  4,5 31




.. csv-table:: 数値降順として並べる
  :header-rows: 1
  :name: mvsort_out3

  no,items
  1,13 2 1
  2,5 5 4 2
  3,112 14
  4,31 5



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
ソーティングするベクトル項目名を指定する。複数項目指定可能。
``%`` に続けて ``n`` を指定すれば数値ソートに、
``%`` に続けて ``r`` を指定すれば逆順ソートに、
また、 ``n`` と ``r`` の両方を指定すれば数値逆順ソートとなる。
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
