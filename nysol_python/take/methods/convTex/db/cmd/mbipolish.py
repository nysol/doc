# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mbipolish'
db['title']='2部グラフの研磨'
db['related']=[
  ["mpolishing","一般グラフの研磨"]
]

############################### DOCUMENT
db['doc']='''
2部グラフデータを入力として、密度の高い部分グラフの中でエッジが張られていないノードペアに枝を張る。
逆に、密度の低い部分グラフのエッジを削除する。
新たに張られる枝や刈られる枝の程度は、``sim=`` , ``th=`` と ``sim2=`` , ``th2=`` で与えた値によって変わる。
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
param['kwd']='sim2'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='sim=の値'
param['text']='''
指定できる値は ``sim=`` と同じ。
'''
db['params'].append(param)

param={}
param['kwd']='th'
param['type']='float'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
``sim=`` で指定された類似度について、ここで指定された値以上の節点間に辺を張る。
'''
db['params'].append(param)

param={}
param['kwd']='th2'
param['type']='float'
param['mand']=False
param['cond']=''
param['default']='th=の値'
param['text']='''
``sim2=`` で指定された類似度について、ここで指定された値以上の節点間に辺を張る。
'''
db['params'].append(param)

param={}
param['kwd']='sup'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='0'
param['text']='''
左の部の次数がsup以上のノードを対象とする。省略すればsup=0。
'''
db['params'].append(param)

param={}
param['kwd']='kn'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='1'
param['text']='''
kn=で指定された値以上の共起頻度を対象とする。
'''
db['params'].append(param)

param={}
param['kwd']='kn2'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='1'
param['text']='''
kn2=で指定された値以上の次数を持つ右部を対象とする。
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
param['kwd']='O'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='研磨過程を出力しない'
param['text']='''
デバッグモード時、データ研磨過程のグラフを保存するディレクトリ名を指定する。
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

db['comParams']=''
