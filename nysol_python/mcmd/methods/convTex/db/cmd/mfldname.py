# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mfldname'
db['title']='項目名の変更'
db['related']=[
  ["mcut","``mfldname`` と同じことができるが、一部の項目名を変更するには少し面倒。また ``mfldname`` の方が少しだけ高速。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` で指定した項目名を変更する。又、 ``n=`` で項目名を新規設定する。

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
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目名のみを変更する。(現項目名:新項目名)
指定していない項目名は変更せずに元の項目名が出力される。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目名が新たに採用される。
データ項目数と同じ数の項目名を指定する必要がある。
'''
db['params'].append(param)

param={}
param['kwd']='nfni'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
入力データの１行目を項目名行とみなさない。このオプションが指定された場合は ``f=`` は利用できない。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,nfn,nfno,x,q,tmppath,precision'
