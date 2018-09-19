# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='msim'
db['title']='二変数間の類似度の計算'
db['related']=[
  ["mstats","1変量の統計量を計算するときはこちら。"],
  ["mmvsim","移動窓を設定した類似度計算。"]
]

############################### DOCUMENT
db['doc']='''
``f=`` パラメータで指定した項目の二変数間の類似度(距離)を
``c=`` パラメータで指定した類似度(距離)関数で計算し類似度行列として出力する。

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
ここで指定された項目(複数項目指定可)を単位として求める。
'''
db['params'].append(param)

param={}
param['kwd']='f'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
ここで指定された項目全ての二項目間の類似度を求める。
'''
db['params'].append(param)

param={}
param['kwd']='c'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
類似度(距離)名リスト(複数項目指定可)
次項に示した類似度(距離)名を指定する。
項目名は以下のように，(:)コロンに続けて指定して変更可能。
コロンに続く名称を省略した場合は類似度(距離)関数名がそのまま項目名として利用される。
例)  ``msim f=x,y,z c=pearson:ピアソン積率相関係数,euclid:ユークリッド距離,cosine:コサイン``
類似度 ``=covar|ucovar|pearson|spearman|kendall|euclid|cosine|``
~~ ``cityblock|hamming|chi|phi|jaccard|supportr|lift|confMax|``
~~ ``confMin|yuleQ|yuleY|kappa|oddsRatio|convMax|convMin``
'''
db['params'].append(param)

param={}
param['kwd']='a'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
2変数の名称を示す項目名を指定する。カンマで区切って2つ指定する。
省略すると ``fld1,fld2`` が使われる。
'''
db['params'].append(param)

param={}
param['kwd']='d'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
対角行列、上三角行列を出力する。
``d=True`` オプションが指定されないと類似度行列の下三角行列のみ出力されるが、
``d=True`` オプションを指定することにより対角行列及び上三角行列も出力される。
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

db['comParams']='i,o,bufcount,assert_diffSize,assert_nullkey,assert_nullin,assert_nullout,nfn,nfno,x,x,tmppath,precision'
