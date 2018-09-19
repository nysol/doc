# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mfriends'
db['title']='グラフデータからの相互類似関係にある辺の選択'
db['related']=[
  ["mpal","トランザクションデータから相互類似関係にある2アイテム集合を選択する"]
]

############################### DOCUMENT
db['doc']='''
グラフ :math:`G=(V,E)` の任意の枝 :math:`(a,b)∈E` について条件
:math:`b \in A\ \mathrm{and}\ a \in B` を満たす枝を選択する。
ここで、 :math:`A(B)` は節点 :math:`a(b)` の隣接節点の内、
類似度が上位 :math:`r` 個の節点集合のこと。
:math:`r` は ``rank=`` で指定し、類似度(項目)は ``sim=`` で指定する。
結果は有向グラフとして出力される。
例えば節点 :math:`a,b` が相互類似関係にあれば、 a->b,b->a の両有向辺が出力される。
無向グラフで出力したければ、 ``udout`` オプションを指定する。
'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='ei'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
エッジデータファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='ef'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='node1,node2'
param['text']='''
エッジデータ上の2つのノード項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='ni'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='エッジファイル上のノードのみを対象にする'
param['text']='''
ノードデータファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='nf'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='node'
param['text']='''
ノードデータ上のノード項目名
'''
db['params'].append(param)

param={}
param['kwd']='eo'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
出力の辺データファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='no'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='ノードデータを出力しない'
param['text']='''
出力の節点データファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='rank'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='3'
param['text']='''
類似度上位何個までの隣接節点を対象とするかを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='sim'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
rank=で使う節点間類似度(枝の重み)項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='dir'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='b'
param['text']='''
出力する類似関係を以下の3つから選んで指定する。
``b`` : 双方向類似枝のみ出力する。
``m`` :片方向類似枝のみ出力する。
``x`` :双方向類似枝、片方向類似枝両方共出力する。
'''
db['params'].append(param)

param={}
param['kwd']='directed'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
有向グラフとみなして計算する。
'''
db['params'].append(param)

param={}
param['kwd']='udout'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
無向グラフとして出力する。両方向に枝がある場合(a->b,b->a)の枝はa-bとして出力される。
a->b,b->aで類似度が異なる場合は平均値が出力される。
'''
db['params'].append(param)

param={}
param['kwd']='T'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='/tmp'
param['text']='''
ワークディレクトリ名を指定する。
'''
db['params'].append(param)

db['comParams']=''
