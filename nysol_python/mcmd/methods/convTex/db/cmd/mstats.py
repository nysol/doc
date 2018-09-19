# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mstats'
db['title']='一変数の統計量算出'
db['related']=[
  ["msim","2変量の統計量を求める。"],
  ["mavg","``c=avg`` に特化したコマンド。"],
  ["msum","``c=sum`` に特化したコマンド。"],
  ["mcount","``c=count`` と異なり、集計キーの行数をカウントする。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した数値項目について
``c=`` パラメータで指定した統計量の計算をする。
``k=`` を指定することで、キー単位で集計することができる。
``f=`` で指定した項目のNULL値は無視される。
ただし、全行がNULL値であればNULL値が出力される。
``(注)`` k=とf=パラメータで指定した項目以外については、どの行が出力されるか>は不定であることに注意してください。\\

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
ここで指定された項目(複数項目指定可)を単位として集計する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目(複数項目指定可)の値が集計される。
'''
db['params'].append(param)

param={}
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
統計量(以下のリストから一つだけ指定可)
``sum|mean|count|ucount|devsq|var|uvar|sd|usd|USD|cv|min|qtile1|``
``median|qtile3|max|range|qrange|mode|skew|uskew|kurt|ukurt``
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
