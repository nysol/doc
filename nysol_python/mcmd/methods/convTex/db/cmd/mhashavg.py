# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mhashavg'
db['title']='ハッシュ法による項目値の平均'
db['related']=[
  ["mavg","同じ機能をもつコマンドだが、内部的にキー項目の並べ替えを行う。"],
  ["mhashsum","同じくハッシュ法を用いた合計計算。"]
]

############################### DOCUMENT
db['doc']='''
hash法を使って ``k=`` パラメータで指定した項目を単位にして、 ``f=`` パラメータで指定した項目値の平均を計算する。
:doc:`mavg` との違いは、キー項目の並べ変えが必要ないため、その分処理速度が速い。
ただし、キーのサイズ(キー項目のとる値の種類数)が多い場合は処理速度が遅くなる。
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
ここで指定された項目(複数項目指定可)の平均が計算される。
:(コロン）で新項目名を指定可能。例） ``f=`` 数量:数量平均
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
ここで指定された項目をキーとして集計する(複数項目指定可)。
'''
db['params'].append(param)

param={}
param['kwd']='hs'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='199999'
param['text']='''
ハッシュサイズ
ハッシュサイズを指定する。
詳細に関しては「 :doc:`mhashsum` 」の節を参照のこと。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
NULL値が1つでも含まれていると結果もNULL値とする。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
