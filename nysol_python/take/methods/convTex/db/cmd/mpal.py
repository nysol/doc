# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mpal'
db['title']='相互類似関係にあるアイテムペア列挙'
db['related']=[
  ["mfriend","グラフデータから相互類似関係にあるアイテムペア(辺)を求める"]
]

############################### DOCUMENT
db['doc']='''
トランザクションデータから2アイテム相関ルールを求め、
ランクに基づいた類似関係にある相関ルールを選択する

入力ファイル形式:

* トランザクションIDとアイテムの２項目によるトランザクションデータ。

o=の出力形式:

* 辺ファイル: simType,simPriority,node1,node2,sim,dir,color
* 節点ファイル: node,support,frequency,total
'''

############################### PARAMETERS
db['params']=[]

param={}
param['kwd']='i'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
トランザクションデータファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='tid'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
トランザクションID項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='item'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
アイテム項目名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='ro'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='ファイル出力なし'
param['text']='''
出力ルールファイル名を指定する。
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
param['kwd']='s'
param['type']='float'
param['mand']=False
param['cond']='S= or s=を指定しなければならない'
param['default']='0.05'
param['text']='''
最小支持度(全トランザクション数に対する割合による指定)
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='int'
param['mand']=True
param['cond']='S= or s=を指定しなければならない'
param['default']=''
param['text']='''
最小支持度(件数による指定)
'''
db['params'].append(param)

param={}
param['kwd']='filter'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='相関ルール評価指数でのルール選択をしない'
param['text']='''
相関ルールの評価指標(省略可,複数指定可)
指定できる類似度は以下の3つ(括弧内は値域)。
J: Jaccard(0..1), P:normalized PMI(-1..0..1), C:Confidence(0..1)
'''
db['params'].append(param)

param={}
param['kwd']='lb'
param['type']='float'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
filter=で指定した相関ルール評価指標の下限値を指定する。
例1: sim=P lb=0.5 : normalized PMIが0.5以上1以下の相関ルールを列挙する
例2: sim=P,C lb=0.5,0.2 ub=,0.8 : 例1に加えて、confidenceが0.2以上0.8以下の相関ルールを列挙する
'''
db['params'].append(param)

param={}
param['kwd']='ub'
param['type']='float'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
filter=で指定した相関ルール評価指標の上限値を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='sim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='S'
param['text']='''
列挙された相関ルールを元にして枝を張る条件となる指標を指定する。
以下に示す4つの相関ルール評価指標が指定できる。
S:Support, J: Jaccard, P:normalized PMI, C:Confidence
'''
db['params'].append(param)

param={}
param['kwd']='rank'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='3'
param['text']='''
辺を張る条件で、類似枝の上位何個までを選択するかを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='dir'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']=''
param['text']='''
双方向類似関係(b)のみを出力するか、単方向類似関係(m)のみか、両方とも含める(x)かを指定する。
相関ルールa=>bの類似度をsim(a=>b)としたとき、
b:(bi-directional) sim(a=>b)およびsim(b=>a)がrank=で指定した順位内である相関ルールのみ選択される。
m:(mono-directional) 片方向の類似度のみが、指定された順位内である相関ルールが選択される。
x:(both) bとmの両方共含める。
以上の3つのパラメータは複数指定することが可能(3つまで)。
 例1: sim=S dir=b rank=3 :
  アイテムaからみてsupport(a=>b)が3位以内で、かつ
  アイテムbからみてsupport(b=>a)も3位以内であるような相関ルールを選択する
 例2: sim=S,C dir=b,m rank=3,1
  例1に加えて、アイテムaから見てconfidenc(a=>b)が3以内、もしくは
  アイテムbから見てconfidenc(b=>a)が3以内であれば、そのような相関ルールも選択する
'''
db['params'].append(param)

param={}
param['kwd']='prune'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
sim=等を複数指定した場合、マルチ枝を単一化する。
第1優先順位: 双方向>片方向
第2優先順位: パラメータ位置昇順
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
