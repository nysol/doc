# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msetstr'
db['title']='文字列項目の追加'
db['related']=[
  ["mcal","``if`` 関数を使えば、行ごとに条件を判定して異なる固定文字列を追加できる。"]
]

############################### DOCUMENT
db['doc']='''
指定した文字列を項目として全行に追加する。複数項目の追加も可能。

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
param['kwd']='v'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
追加する文字列リスト。
値を何も指定しないとNULL値が追加される。
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
追加する項目名。
``v=`` で指定した文字列の個数と同数の項目名を指定しなければならない。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,nfn,nfno,x,tmppath,precision'
