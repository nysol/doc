# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mdformat'
db['title']='日付時刻抽出'
db['related']=[

]

############################### DOCUMENT
db['doc']='''
他のシステムからエクスポートしたCSVデータでは、
日付時刻項目にスラッシュ記号やコロン記号が入っていることが多く、
また月日や時が1桁で格納されている場合もある
(例: ``2014/7/18 1:57`` )。
このような項目をそのままMCMDで扱おうとすると、
日付計算や並べ替え、範囲検索がうまくいかない。
``mdformat`` コマンドを使うことで、
``f=`` パラメータで指定した項目から、
``c=`` パラメータで指定したフォーマットに従って
年月日・時分秒を抽出し、MCMDで扱うことが可能な
:doc:`日付型や時刻型`
に変換することができる。

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
抽出対象となる項目名リスト(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
文字列のフォーマットを指定する。フォーマットの変換指定文字参照
'''
db['params'].append(param)

param={}
param['kwd']='A'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
このオプションにより、指定した項目を置き換えるのではなく、新たに項目が追加される。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullin,assert_nullout,nfn,nfno,x,tmppath,precision'
