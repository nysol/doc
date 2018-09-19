# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mmvsim'
db['title']='移動窓の類似度計算'
db['related']=[
  ["msim","移動窓を設定せずに類似度計算を行う。"],
  ["mwindow","動窓のデータを作成するので、そのデータを使えば ``mmvstats`` で計算できない統計量も計算可能。"],
  ["mmvavg","移動平均に限定した計算を行う。"]
]

############################### DOCUMENT
db['doc']='''
移動窓を設定し、各種類似度(2変量の統計量)を計算する。
:doc:`msim` コマンドの移動窓バージョンとして考えればよい。
``msim`` との違いは、指定できる類似度は一つだけで、また類似度計算の対象項目は2つのみである。

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
param['cond']=' ``q=True`` の指定がない場合'
param['default']=''
param['text']='''
ここで指定した項目(複数項目指定可)で並べ替えられた後、各種類似度が計算される。
``q=True`` オプションを指定しないとき、 ``s=`` パラメータは必須。
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
類似度(以下のリストから一つだけ)指定する。
``covar|ucovar|pearson|spearman|kendall|euclid|``
``cosine|cityblock|hamming|chi|phi|jaccard|support|lift``
詳細な定義は :doc:`msim` コマンドを参照のこと。
'''
db['params'].append(param)

param={}
param['kwd']='skip'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='\verb|skip=(t=の値-1)|'
param['text']='''
出力を抑制する最初の行数を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
計算結果の出力として追加される項目の名前を指定する。
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
