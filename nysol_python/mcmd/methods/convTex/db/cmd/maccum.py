# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='maccum'
db['title']='累積計算'
db['related']=[
  ["mshare","構成比を計算する。 ``maccum`` と組み合わせて累積相対度数が計算できる。"],
  ["mcal","前行の計算結果 ``#{}`` を利用することで累計計算ができる。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目の累積を計算し、新しい項目として追加する。
``k=`` を指定することで、キー単位毎に累積計算が可能となる。

'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
累積の単位となる項目名リスト(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=True
param['cond']=' ``q`` オプションの指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、累積が計算される。
``q`` オプションを指定しないとき、 ``s=`` パラメータは必須。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)の値が累積される。
項目の値がNULL値である場合は無視される。
:(コロン）で新項目名を指定する必要がある。例） ``f=数量:数量累計``
'''
db['params'].append(param)

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

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
