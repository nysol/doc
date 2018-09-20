# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mavg'
db['title']='項目値の平均'
db['related']=[
  ["mhashavg","集計キーを事前に並べ替えなくてよい分高速である。"],
  ["msum","合計バージョン。"],
  ["mstats","その他の多様な統計量を求めるのであればこれ。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` で指定した項目の平均値を計算する。
``k=`` と ``f=`` で指定した項目以外については、どの行が出力されるか>は不定であることに注意されたい。
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
ここで指定した項目(複数項目指定可)の値が集計される。
:(コロン）で新項目名を指定可能。例） ``f=amount:average``
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
集計の単位となる項目(複数項目指定可)名リストを指定する。
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

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
