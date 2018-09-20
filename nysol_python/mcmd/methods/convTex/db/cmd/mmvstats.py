# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mmvstats'
db['title']='移動窓の統計量の計算'
db['related']=[
  ["mmvavg","移動平均に限定した計算を行う。"],
  ["mwindow","動窓のデータを作成するので、そのデータを使えば ``mmvstats`` で計算できない統計量も計算可能。"],
  ["mmvsim","移動窓の類似度(2変量統計量)の計算を行う。"]
]

############################### DOCUMENT
db['doc']='''
移動窓を設定し、各種統計量(1変量)を計算する。
:doc:`mstats` コマンドの移動窓バージョンとして考えればよい。

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
param['kwd']='s'
param['type']='str'
param['mand']=False
param['cond']=' ``q`` オプションの指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、各種統計量が計算される。
``q`` オプションを指定しないとき、 ``s=`` パラメータは必須。
'''
db['params'].append(param)

param={}
param['kwd']='k'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='キーブレイク処理しない'
param['text']='''
ここで指定された項目(複数項目指定可)を単位として集計する。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
集計項目名リスト(複数項目指定可)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='t'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
期間数を1以上の整数で指定する。
'''
db['params'].append(param)

param={}
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
統計量(以下のリストから一つだけ指定可)
``sum|mean|devsq|var|uvar|sd|usd|cv|min|``
``|max|range|skew|uskew|kurt|ukurt``
詳細な定義は :doc:`mstats` コマンドを参照のこと。
'''
db['params'].append(param)

param={}
param['kwd']='skip'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
出力を抑制する最初の行数
'''
db['params'].append(param)

param={}
param['kwd']='n'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
期間内にNULL値が1つでも含まれていると結果もNULL値とする。
'''
db['params'].append(param)

db['comParams']='i,o,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,q,tmppath,precision'
