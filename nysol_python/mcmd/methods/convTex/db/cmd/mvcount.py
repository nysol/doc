# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mvcount'
db['title']='ベクトルサイズの計算'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
ベクトルのサイズ(ベクトルの要素数)を計算する。
典型的な例を :numref:`mvcount_input` 〜 :numref:`mvcount_out3` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mvcount_input

  no,items
  1,a b c
  2,a d
  3,b f e f
  4,




.. csv-table:: 基本例
  :header-rows: 1
  :name: mvcount_out1

  no,items,size
  1,a b c,3
  2,a d,2
  3,b f e f,4
  4,,0



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
要素数をカウントするベクトルの項目名( ``i=`` データ上)を指定する。
結果項目を ``:`` に続けて複数項目指定可能。
複数項目指定可能。
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

db['comParams']='i,o,delim,assert_diffSize,assert_nullin,nfn,nfno,x,tmppath,precision'
