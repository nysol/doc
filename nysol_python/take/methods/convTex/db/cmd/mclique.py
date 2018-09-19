# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mclique'
db['title']='クリークの列挙'
db['related']=[
  ["mbiclique","2部クリーク列挙"]
]

############################### DOCUMENT
db['doc']='''
一般グラフデータから極大クリークを列挙する。

**入力形式**: 一般グラフを節点ペアで表現した形式。他のいかなる節点とも接続のない節点は、サイズが1の自明なクリークであるため、入力対象外とする。

**出力形式**: クリークIDと接点を出力する。出力項目は ``id,node,size`` の3項目である。sizeはクリークを構成する節点数である。
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
辺データファイルを指定する。
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
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
節点データファイルを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='nf'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='node'
param['text']='''
節点データ上の節点項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='o'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']='標準出力'
param['text']='''
出力ファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
クリークを構成する最小節点数(ここで指定したサイズより小さいクリークは列挙されない)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
クリークを構成する最大節点数(ここで指定したサイズより大きいクリークは列挙されない)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='all'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
極大クリークだけでなく、全クリークを列挙する。
'''
db['params'].append(param)

param={}
param['kwd']='T'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='/tmp'
param['text']='''
ワークディレクトリを指定する。
'''
db['params'].append(param)

db['comParams']=''
