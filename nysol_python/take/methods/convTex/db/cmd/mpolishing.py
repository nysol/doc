# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mpolishing'
db['title']='一般グラフの研磨'
db['related']=[
  ["mbipolish","2部グラフの研磨"]
]

############################### DOCUMENT
db['doc']='''
一般グラフデータを入力として、密度の高い部分グラフの中でエッジが張られていないノードペアに枝を張る。
逆に、密度の低い部分グラフのエッジを削除する。
新たに張られる枝や刈られる枝の程度は、sim=とth=で与えた値によって変わる。
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
データ研磨後のエッジデータファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='no'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='ノードデータを出力しない'
param['text']='''
データ研磨後のノードデータファイル
'''
db['params'].append(param)

param={}
param['kwd']='sim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='R'
param['text']='''
ノードa,bに張られたエッジ集合を、それぞれA,Bとしたとき、ノードa,bに枝を張るために用いる類似度を指定する。
* i: inclusion
* I: both-inclusion
* S: :math:`|A \cap B| / max(|A|,|B|)`
* s: :math:`|A \cap B| / min(|A|,|B|)`
* T (intersection): find pairs having common [threshld] items
* R (resemblance): find pairs s.t. :math:`|A \cap B| / |A \cup B| >= [threshld]`
* P (PMI): find pairs s.t. log ( :math:`|A \cap B| * |all| / (|A|*|B|)) >= [threshld]`
* C (cosine distance): find pairs s.t. inner product of their normalized vectors >= [threshld]
'''
db['params'].append(param)

param={}
param['kwd']='th'
param['type']='float'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
sim=で指定された類似度について、ここで指定された値以上の節点間に枝を張る。
'''
db['params'].append(param)

param={}
param['kwd']='sup'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
類似度計算において、 :math:`|A∩B|>=sup` の条件を加える。
'''
db['params'].append(param)

param={}
param['kwd']='indirect'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
上記類似度計算における隣接節点集合から直接の関係を除外する。
すなわち、 :math:`A=A-b, B=B-a` として類似度を計算する。
'''
db['params'].append(param)

param={}
param['kwd']='iter'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='30'
param['text']='''
データ研磨の最大繰り返し数を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='log'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='ログを出力しない'
param['text']='''
パラメータの設定値や収束回数等をkey-value形式のCSVで保存するファイル名を指定する。
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

param={}
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='研磨過程を出力しない'
param['text']='''
デバッグモード時、データ研磨過程のグラフを保存するディレクトリ名を指定する。
'''
db['params'].append(param)

db['comParams']=''
