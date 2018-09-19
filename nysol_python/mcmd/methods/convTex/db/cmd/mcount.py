# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mcount'
db['title']='行数カウント'
db['related']=[
  ["mstats","``c=count`` を指定することで、NULL値でないデータ件数をカウントできる。"]
]

############################### DOCUMENT
db['doc']='''
行数をカウントし、 ``a=`` パラメータで指定した項目名で出力する。
``k=`` を指定すると、集計キー毎の件数をカウントし、
``k=`` を指定しなければ、全行数がカウントされる。

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
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
新たに追加される項目の名前を指定する。
``nfn`` オプション使用時は、必須ではない。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
キー項目名リスト(複数項目指定可)
カウントの単位となる項目名リスト。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
