# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mproduct'
db['title']='参照ファイルの直積結合'
db['related']=[
  ["mnjoin","結合キーを指定しての ``mproduct`` のような結合を行う。"]
]

############################### DOCUMENT
db['doc']='''
入力データ1行に対して、 ``m=`` パラメータで指定した参照データの
``f=`` パラメータで指定した項目全行を結合する。

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
param['default']='全項目'
param['text']='''
結合する参照データ上の項目名リスト(複数項目指定可)。
省略するとキー項目を除いた全ての項目が結合される。
'''
db['params'].append(param)

param={}
param['kwd']='m'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='標準入力'
param['text']='''
参照データを指定する。
このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)
'''
db['params'].append(param)

param={}
param['kwd']='bufcount'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
バッファのサイズ数を指定する。
'''
db['params'].append(param)

db['comParams']='i,o,bufcount,assert_diffSize,assert_nullin,nfn,nfno,x,tmppath,precision'
