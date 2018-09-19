# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mcommon'
db['title']='参照ファイルによる行選択'
db['related']=[
  ["mselstr","参照データの結合キーの種類数が少なければこのコマンドでも対応できる。"],
  ["mnrcommon","参照データの結合キーがユニークでなければこちらを使う。"],
  ["mjoin","選択だけでなく、項目を結合したい場合はこのコマンド。"]
]

############################### DOCUMENT
db['doc']='''
``k=`` パラメータで指定した入力データの項目値と ``m=`` パラメータで指定した参照データの項目値を比較し、同じ値を持つ入力データの行を選択する。

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
param['mand']=True
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
入力データ上の突き合わせる項目名リスト(複数項目指定可)
ここで指定した入力データの項目と ``K=`` パラメータで指定された参照データの項目が同じ行が選択される。
同じ値が複数行連続していてもよい。
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
またこのパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)
'''
db['params'].append(param)

param={}
param['kwd']='K'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='k=と同一項目名'
param['text']='''
参照データ上の突き合わせる項目名リスト(複数項目指定可)
ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行が選択される。
参照データ上に ``k=`` パラメータで指定した入力データ上の項目と同名の項目が存在する場合は指定する必要はない。
同じ値が複数行連続していてもよい。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='出力しない'
param['text']='''
指定の条件に一致しない行を出力するデータ。
'''
db['params'].append(param)

param={}
param['kwd']='r'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
条件反転
``k=`` パラメータで指定した入力データの項目値と
``m=`` パラメータで指定した参照データの項目値を比較し、
同じ値を持たない入力データの行を選択する。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,nfn,nfno,x,q,tmppath,precision'
