mtra2gc トランザクションからの類似度グラフ生成
------------------------------------------------------

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
  :name: mtra2gc.py_outEdge

  node1%0,node2%1,frequency,frequency1,frequency2,total,support,confidence,lift,jaccard,PMI
  a,b,3,3,4,5,0.6,1,1.25,0.75,0.4368292054
  a,c,1,1,3,5,0.2,1,1.666666667,0.3333333333,0.3173938055


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 必須

  | トランザクションデータファイルを指定する。

**tid=** : 型=str , 必須

  | トランザクションIDとなる項目名を指定する。

**item=** : 型=str , 必須

  | アイテム項目名を指定する。

**no=** : 型=str , 任意(default=節点データを出力しない)

  | 出力節点データファイル名を指定する。

**eo=** : 型=str , 必須

  | 出力辺データファイル名を指定する。

**s=** : 型=float(0.0-1.0) , 任意(default=0.01)

  | 枝を張る条件として、最小支持度(全トランザクション数に対する割合による指定)を指定する。

**S=** : 型=int , 任意(default=s=の値を用いる)

  | 枝を張る条件として、最小支持度(トランザクション数)を指定する。

**sim=** : 型=str , 任意(default=類似度による条件を用いない)

  | アイテムa,bに枝を張る条件として用いる類似度を指定する。
  | 省略した場合は、最小支持度の条件(s= or S=)でのみ枝を張ることになる。
  | 指定できる類似度は以下の3つのいずれか一つ。
  | 記号の意味は、 :math:`A (B)` : アイテム :math:`a (b)` を含むトランザクション集合、 :math:`T` : 全トランザクション集合。
  | J (jaccard): :math:`|A \cap B|/|A \cup B|`
  | P (normalized PMI): :math:`log(|A \cap B|*|T| / (|A|*|B|)) / log(|A \cap B|/|T|)`
  |  liftを-1〜+1に基準化したもの。
  |  -1:a(b)出現時b(a)出現なし、0:a,b独立、+1:a(b)出現時必ずb(a)出現
  | C (Confidence(A=>B)): :math:`|A \cap B|/|B|`

**th=** : 型=float , 条件付き必須(sim=が指定された時)

  | sim=で指定された類似度について、ここで指定された値以上のアイテム間に枝を張る。

**node_support=** : 型=bool , 任意(default=False)

  | 節点にもS=の条件を適用する。指定しなければ全てのアイテムを節点として出力する。

**num=** : 型=bool , 任意(default=False)

  | アイテム項目が正の整数値である場合に指定可能で、処理が高速化される。

**T=** : 型=str , 任意(default=/tmp)

  | ワークディレクトリを指定する。



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('tra.csv','w') as f:
      f.write(
    '''id,item
    1,a
    1,b
    1,c
    1,f
    2,d
    2,e
    2,f
    3,a
    3,b
    3,d
    3,f
    4,b
    4,d
    4,f
    5,a
    5,b
    5,d
    5,e
    ''')


**基本例**

共起頻度が2以上( ``S=2`` )、確信度が0.7以上 (``sim="C"`` , ``th=0.7`` )を満たす2アイテム集合を
グラフデータ(節点データファイル: ``node.csv`` , 辺データファイル: ``edge.csv`` )として列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mtra2gc(i="tra.csv", tid="id", item="item", S=2, sim="C", th=0.7, no="node.csv", eo="edge.csv").run()
    ### node.csv の内容
    # node%0,support,frequency,total
    # a,0.6,3,5
    # b,0.8,4,5
    # c,0.2,1,5
    # d,0.8,4,5
    # e,0.4,2,5
    # f,0.8,4,5
    ### edge.csv の内容
    # node1%0,node2%1,frequency,frequency1,frequency2,total,support,confidence,lift,jaccard,PMI
    # a,b,3,3,4,5,0.6,1,1.25,0.75,0.4368292054
    # b,a,3,4,3,5,0.6,0.75,1.25,0.75,0.4368292054
    # b,d,3,4,4,5,0.6,0.75,0.9375,0.6,-0.1263415893
    # b,f,3,4,4,5,0.6,0.75,0.9375,0.6,-0.1263415893
    # d,b,3,4,4,5,0.6,0.75,0.9375,0.6,-0.1263415893
    # d,f,3,4,4,5,0.6,0.75,0.9375,0.6,-0.1263415893
    # e,d,2,2,4,5,0.4,1,1.25,0.5,0.2435292026
    # f,b,3,4,4,5,0.6,0.75,0.9375,0.6,-0.1263415893
    # f,d,3,4,4,5,0.6,0.75,0.9375,0.6,-0.1263415893


関連メソッド
''''''''''''''''''''



