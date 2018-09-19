# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msum'
db['title']='項目値の合計'
db['related']=[
  ["mhashsum","集計キーを事前に並べ替えなくても計算できる。"],
  ["mavg","平均バージョン。"],
  ["mstats","その他の多様な統計量を求めるのであればこれ。"]
]

############################### DOCUMENT
db['doc']='''
``k=`` パラメータで指定した項目の値が同じ行について、
``f=`` パラメータで指定した集計項目の項目値を合計する。\\
``(注)`` k=とf=パラメータで指定した項目以外については、どの行が出力されるかは不定であることに注意してください。\\

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
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
集計の単位となる項目名リスト（複数項目指定可）を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目（複数項目指定可）の値が集計される。NULL値は無視される。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
``f=`` で指定した項目にNULL値が入っていると計算結果もNULLとする。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmpPath,precision'
