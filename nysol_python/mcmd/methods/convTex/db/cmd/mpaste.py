# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mpaste'
db['title']='参照ファイル項目の行番号マッチング結合'
db['related']=[
  ["mjoin","行番号でなく、キー項目で結合する。"]
]

############################### DOCUMENT
db['doc']='''
入力データと参照データを行番号でマッチングさせて結合する。
データ件数が異なる場合は、少い方のデータに合わせる。
``n`` や ``N`` オプションを指定することでマッチングできな行もNULL値で結合することが可能である。
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
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
入力データにあって参照データにない場合にNULL値を出力する。
'''
db['params'].append(param)

param={}
param['kwd']='N'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
参照データにあって入力データにない場合にNULL値を出力する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
