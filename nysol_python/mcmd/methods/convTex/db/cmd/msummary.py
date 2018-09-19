# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msummary'
db['title']='1変数の統計量の計算'
db['related']=[
  ["mstats","求める統計量が1つのとき用いる。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した集計項目で
``c=`` パラメータで指定した統計量の計算をする。\\

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
キー項目名リスト(複数項目指定可)【 :doc:`集計キーブレイク処理` 】
ここで指定された項目を単位として集計する。
指定する場合は事前に指定する集計の単位となる項目順に並べ替えておく必要がある。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
集計項目名リスト(複数項目指定可)
ここで指定された項目の値が集計される。
``x=True`` , ``nfn=True`` オプション使用時は、項目番号(0～)で指定。
'''
db['params'].append(param)

param={}
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
統計量リスト(複数項目指定可)
出力する統計量をコンマで区切って指定する。
統計量リスト:
``sum/mean/count/ucount/devsq/var/uvar/sd/usd/cv/min/qtile1/median/qtile3/max/``
``range/qrange/mode/skew/uskew/kurt/ukurt``
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
新項目名を指定する。
``f=`` パラメータで指定した項目名をデータとして出力する際の項目名(省略時はfld)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
NULL値が1つでも含まれていると結果もNULL値とする。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
