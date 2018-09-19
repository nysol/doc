# ======================================
# コマンドマニュアル自動作成用基礎データ
# ======================================
db={}
db['name']='mtra2gc'
db['title']='トランザクションからの類似度グラフ生成'
db['related']=[
]

############################### DOCUMENT
db['doc']='''
2アイテムの共起情報によって類似度を定義し、ある閾値より高い類似度を持つアイテム間に枝を張ることで一般グラフを生成する。
内部的に2アイテムの共起情報の取得については、 :doc:`Takeのコアメソッドsspc <../methods0/sspc>` を用いている。

``no=`` で指定する節点データの出力形式は、 :numref:`mtra2gc.py_outNode` に示される通りである。
``node`` は ``item=`` で指定したアイテム項目、
``frequency`` は アイテムの出現頻度、 ``total`` は全トランザクション数、
そして、 ``support`` は 出現確率(出現頻度/全トランザクション数)を表す。

.. code-block:: bash
  :linenos:
  :caption: mtra2gcの節点出力ファイルの例
  :name: mtra2gc.py_outNode

  a,0.6,3,5
  b,0.8,4,5
  c,0.2,1,5
  d,0.8,4,5
  e,0.4,2,5
  f,0.8,4,5


``eo=`` で指定する辺データの出力形式は、 :numref:`mtra2gc.py_outEdge` に示される通りである。
``node1,node2`` は 辺を張る2つの節点、
``frequency`` は 辺(2つのアイテム)の共起頻度、 
``frequency1,frequency2`` は ``node1,node2`` の出現頻度、
``total`` は全トランザクション数、
そして、 ``support`` は 共起確率( ``frequency`` / ``total`` )
``confidence`` は確信度( ``frequency`` / ``frequency1`` )
``lift`` はリフト値( ( ``total`` * ``frequency`` ) / ( ``frequency1`` * ``frequency2`` ) を表す。
``jaccard`` と ``PMI`` は パラメータ ``sim=`` の説明を参照のこと。

.. code-block:: bash
  :linenos:
  :caption: mtra2gcの節点出力ファイルの例
  :name: mtra2gc.py_outNode

  node1%0,node2%1,frequency,frequency1,frequency2,total,support,confidence,lift,jaccard,PMI
  a,b,3,3,4,5,0.6,1,1.25,0.75,0.4368292054
  a,c,1,1,3,5,0.2,1,1.666666667,0.3333333333,0.3173938055
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
トランザクションデータファイルを指定する。
'''
db['params'].append(param)

param={}
param['kwd']='tid'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
トランザクションIDとなる項目名を指定する。
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
param['kwd']='no'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='節点データを出力しない'
param['text']='''
出力節点データファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='eo'
param['type']='str'
param['mand']=True
param['cond']=''
param['default']=''
param['text']='''
出力辺データファイル名を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='s'
param['type']='float(0.0-1.0)'
param['mand']=False
param['cond']=''
param['default']='0.01'
param['text']='''
枝を張る条件として、最小支持度(全トランザクション数に対する割合による指定)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='S'
param['type']='int'
param['mand']=False
param['cond']=''
param['default']='s=の値を用いる'
param['text']='''
枝を張る条件として、最小支持度(トランザクション数)を指定する。
'''
db['params'].append(param)

param={}
param['kwd']='sim'
param['type']='str'
param['mand']=False
param['cond']=''
param['default']='類似度による条件を用いない'
param['text']='''
アイテムa,bに枝を張る条件として用いる類似度を指定する。
省略した場合は、最小支持度の条件(s= or S=)でのみ枝を張ることになる。
指定できる類似度は以下の3つのいずれか一つ。
記号の意味は、 :math:`A (B)` : アイテム :math:`a (b)` を含むトランザクション集合、 :math:`T` : 全トランザクション集合。
J (jaccard): :math:`|A \cap B|/|A \cup B|`
P (normalized PMI): :math:`log(|A \cap B|*|T| / (|A|*|B|)) / log(|A \cap B|/|T|)`
 liftを-1〜+1に基準化したもの。
 -1:a(b)出現時b(a)出現なし、0:a,b独立、+1:a(b)出現時必ずb(a)出現
C (Confidence(A=>B)): :math:`|A \cap B|/|B|`
'''
db['params'].append(param)


param={}
param['kwd']='th'
param['type']='float'
param['mand']=True
param['cond']='sim=が指定された時'
param['default']=''
param['text']='''
sim=で指定された類似度について、ここで指定された値以上のアイテム間に枝を張る。
'''
db['params'].append(param)

param={}
param['kwd']='node_support'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
節点にもS=の条件を適用する。指定しなければ全てのアイテムを節点として出力する。
'''
db['params'].append(param)

param={}
param['kwd']='num'
param['type']='bool'
param['mand']=False
param['cond']=''
param['default']='False'
param['text']='''
アイテム項目が正の整数値である場合に指定可能で、処理が高速化される。
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
