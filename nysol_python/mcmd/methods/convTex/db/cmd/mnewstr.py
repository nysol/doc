# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mnewstr'
db['title']='固定文字列データの新規生成'
db['related']=[
  ["mnewnumber","連番を生成する。"],
  ["mnewrand","乱数を生成する。"]
]

############################### DOCUMENT
db['doc']='''
``v=`` パラメータで指定した文字列データを新規作成し、 ``a=`` パラメータで指定した項目名で出力する。
一度に複数の項目を生成することも可能。

'''

############################### PARAMETERS
db['params']=[]

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
新規に作成するデータの項目名を指定する。
複数の項目を生成する場合は、項目名をカンマで区切る。
``nfn`` もしくは ``nfno`` オプション指定時は指定の必要はない。
'''
db['params'].append(param)

param={}
param['kwd']='v'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
新しく作成する文字列を指定する。
複数の項目を生成する場合は、値をカンマで区切る。 ``a=`` で指定した個数と同数でなければならない。
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='10'
param['text']='''
新規作成する乱数データの行数を指定する。
'''
db['params'].append(param)

db['comParams']='o,nfn,nfno,x,tmppath,precision'
