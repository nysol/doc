# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='muniq'
db['title']='レコードの単一化'
db['related']=[
  ["mbest","同一キーの中で何番目の行を選択するかを指定したい場合は ``mbest`` コマンドを使う。"]
]

############################### DOCUMENT
db['doc']='''
値が重複した行を単一化する。

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
行を単一化する単位となる項目名リストを指定する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
