# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mcut'
db['title']='項目の選択'
db['related']=[
  ["mfldname","項目名を変更したいだけの場合は ``mfldname`` を使う。"]
]

############################### DOCUMENT
db['doc']='''
指定した項目を選択する。
``r`` オプションを付けると、指定した項目を削除する。
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
抜き出す項目名
項目名をコロンで区切ることで、出力項目名を変更することができる。
ex.  ``f=a:A,b:B``
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
項目削除スイッチ
``f=`` で指定した項目を削除し、それ以外の項目が抜き出される。
'''
db['params'].append(param)

param={}
param['kwd']='nfni'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
入力データの１行目を項目名行とみなさない。よって項目番号で指定しなければならない。
以下のように、新項目名を組み合わせて指定することで項目名行を追加出力することが可能となる。
例）f=0:日付,2:店,3:数量
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,nfn,nfno,x,tmppath,precision'
