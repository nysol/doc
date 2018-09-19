# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mshare'
db['title']='構成比の計算'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目の構成比を計算し、新しい項目として追加する。\\

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
ここで指定された項目（複数項目指定可）の値のシェアが計算される。
:(コロン）で新項目名を指定する必要がある。例）f=数量:数量シェア
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
シェア計算の単位となる項目名リスト（複数項目指定可）を指定する。
省略すると全行同じキーの値として処理される。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,x,tmppath,precision'
