# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mkeybreak'
db['title']='キーブレイク箇所'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
``k=`` パラメータで指定した項目をキー項目について、先頭と終端に印を付ける。
先頭は ``top`` 項目に、終端は ``bot`` 項目に ``1`` を出力する。
先頭/終端でない行はNULL値を出力する。

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
param['mand']=True
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
集計キーとなる項目名リスト（複数項目指定可）を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q=True`` の指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えた後、先頭・終端に印を付ける。
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='top,bot'
param['text']='''
先頭と終端の印を出力する項目名を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullout,nfn,nfno,x,q,tmppath,precision'
