# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mbiclique'
db['title']='極大2部クリークの列挙'
db['related']=[
  ["mclique","一般グラフのクリーク列挙"]
]

############################### DOCUMENT
db['doc']='''
2部グラフデータを入力として、極大2部クリークを列挙する。

入力形式)

二部グラフの節点ペアを項目で表現したCSVデータ。

出力形式1) デフォルトの出力形式

二部クリークを構成する全節点を各部ごとにベクトル形式で出力する。
出力項目は、 ``節点項目名1,節点項目名2,size1,size2`` の4項目で、節点名1と節点名2は、
``ef=`` で指定された名称が利用される。
節点項目名1,節点項目名2に出力される値が節点名ベクトルである(一行が一つの二部クリークに対応)ことが異なる。
節点項目名1,節点項目名2には、各部を構成する節点名のベクトルが出力される。
size1,size2は2部クリークを構成する各部の節点数である。

出力形式2) ``edge`` オプションを指定した場合の出力形式

クリークIDと二部クリークを構成する全枝(節点ペア)を出力する。
出力項目は"id,節点項目名1,節点項目名2,size"の5項目である。
idはクリークの識別番号で、一つのクリークは同じid番号が振られる。id番号そのものに意味はない。
例えば各部のサイズが3,4であるような二部クリークは3*4=12行の枝データとして出力される。
出力形式1に比べてファイルサイズは大きくなる。
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
param['kwd']='o'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
出力ファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='l'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
2部クリークを構成する最小節点数(ここで指定したサイズより小さいクリークは列挙されない)を指定する。
カンマで区切って2つの値を指定すると、各部のサイズを制限できる。
1つ目の値はef=で指定した1つ目の部に対応し、2つ目の値は2つ目に指定した部に対応する。
'''
db['params'].append(param)

param={}
param['kwd']='u'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='制限なし'
param['text']='''
クリークを構成する最大節点数(ここで指定したサイズより大きいクリークは列挙されない)を指定する。
カンマで区切って2つの値を指定すると、各部のサイズを制限できる
'''
db['params'].append(param)

param={}
param['kwd']='edge'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
枝による出力(クリークIDと枝(節点ペア)で出力する)。
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
