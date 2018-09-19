mpolishing 一般グラフの研磨
--------------------------------------

一般グラフデータを入力として、密度の高い部分グラフの中でエッジが張られていないノードペアに枝を張る。
逆に、密度の低い部分グラフのエッジを削除する。
新たに張られる枝や刈られる枝の程度は、sim=とth=で与えた値によって変わる。


パラメータ
''''''''''''''''''''''

**ei=** : 型=str , 必須

  | エッジデータファイル名を指定する。

**ef=** : 型=str , 任意(default=node1,node2)

  | エッジデータ上の2つのノード項目名を指定する。

**ni=** : 型=str , 任意(default=エッジファイル上のノードのみを対象にする)

  | ノードデータファイル名を指定する。

**nf=** : 型=str , 任意(default=node)

  | ノードデータ上のノード項目名

**eo=** : 型=str , 必須

  | データ研磨後のエッジデータファイル名を指定する。

**no=** : 型=str , 任意(default=ノードデータを出力しない)

  | データ研磨後のノードデータファイル

**sim=** : 型=str , 任意(default=R)

  | ノードa,bに張られたエッジ集合を、それぞれA,Bとしたとき、ノードa,bに枝を張るために用いる類似度を指定する。
  | * i: inclusion
  | * I: both-inclusion
  | * S: :math:`|A \cap B| / max(|A|,|B|)`
  | * s: :math:`|A \cap B| / min(|A|,|B|)`
  | * T (intersection): find pairs having common [threshld] items
  | * R (resemblance): find pairs s.t. :math:`|A \cap B| / |A \cup B| >= [threshld]`
  | * P (PMI): find pairs s.t. log ( :math:`|A \cap B| * |all| / (|A|*|B|)) >= [threshld]`
  | * C (cosine distance): find pairs s.t. inner product of their normalized vectors >= [threshld]

**th=** : 型=float , 必須

  | sim=で指定された類似度について、ここで指定された値以上の節点間に枝を張る。

**sup=** : 型=int , 任意(default=0)

  | 類似度計算において、 :math:`|A∩B|>=sup` の条件を加える。

**indirect=** : 型=bool , 任意(default=False)

  | 上記類似度計算における隣接節点集合から直接の関係を除外する。
  | すなわち、 :math:`A=A-b, B=B-a` として類似度を計算する。

**iter=** : 型=int , 任意(default=30)

  | データ研磨の最大繰り返し数を指定する。

**log=** : 型=str , 任意(default=ログを出力しない)

  | パラメータの設定値や収束回数等をkey-value形式のCSVで保存するファイル名を指定する。

**T=** : 型=str , 任意(default=/tmp)

  | ワークディレクトリ名を指定する。

**O=** : 型=str , 任意(default=研磨過程を出力しない)

  | デバッグモード時、データ研磨過程のグラフを保存するディレクトリ名を指定する。



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('dat1.csv','w') as f:
      f.write(
    '''node1,node2
    a,b
    a,c
    a,e
    b,c
    b,e
    b,g
    c,d
    c,g
    d,e
    e,f
    ''')


**基本例**

類似度をresemblance(sim=R)とし、th=0.4で枝を張り直してグラフ研磨する。
``log1.csv`` を見ると、グラフ情報の表示が繰り返されておりそれが
5回目(dens4など)で終わっており、研磨回数は5回で収束していることがわかる。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    from nysol.take import graph as ng
    gi=ng.graph(edgeFile="dat1.csv",title1="node1",title2="node2")
    go=nt.mpolishing(gi=gi,sim="R",th=0.4,log="log.csv").run()
    e=go.edges().run()
    print(e)
    # [['a', 'b'], ['a', 'c'], ['a', 'e'], ['a', 'g'], ['b', 'c'], ['b', 'e'], ['b', 'g'], ['c', 'e'], ['c', 'g'], ['e', 'g']]
    n=go.nodes().run()
    print(n)
    # [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g']]
    ### log.csv の内容
    # key,value
    # iter,30
    # outDir,None
    # th,0.4
    # indirect,False
    # measure,R
    # minSupp,0
    # logFile,log.csv
    # outDir,None
    # time,0:00:00.245431
    # nSize0,7.0
    # eSize0,10
    # dens0,0.47619047619047616
    # nSize1,7.0
    # eSize1,11
    # dens1,0.5238095238095238
    # nSize2,6.0
    # eSize2,11
    # dens2,0.7333333333333333
    # nSize3,5.0
    # eSize3,10
    # dens3,1.0
    # nSize4,5.0
    # eSize4,10
    # dens4,1.0


**PMIによる研磨**

類似度をnormalized PMI(sim=P)とし、th=0.2で枝を張り直して得られた研磨グラフ。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    from nysol.take import graph as ng
    gi=ng.graph(edgeFile="dat1.csv",title1="node1",title2="node2")
    go=nt.mpolishing(gi=gi,sim="P",th=0.2).run()
    e=go.edges().run()
    print(e)
    # [['a', 'b'], ['b', 'c'], ['b', 'g'], ['c', 'g'], ['e', 'f']]
    ###  の内容


**intersectionで1回の研磨**

類似度をintersection(sim=T)とし、2件以上(th=2)で枝を張り直し
直接の接続を考慮に入れる例。研磨回数は1回のみ(iter=1)。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    from nysol.take import graph as ng
    gi=ng.graph(edgeFile="dat1.csv",title1="node1",title2="node2")
    go=nt.mpolishing(gi=gi,sim="T",th=2,iter=1).run()
    e=go.edges().run()
    print(e)
    # [['a', 'b'], ['a', 'c'], ['a', 'd'], ['a', 'e'], ['a', 'g'], ['b', 'c'], ['b', 'd'], ['b', 'e'], ['b', 'g'], ['c', 'd'], ['c', 'e'], ['c', 'g'], ['d', 'e'], ['e', 'f']]
    ### result.csv の内容


**直接の接続を考慮しない例**

``indirect`` オプションを指定することで、類似度の計算で直接の接続は無視される。
出力結果では、枝が全て消えるため、研磨後の枝データは出力されない。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    from nysol.take import graph as ng
    gi=ng.graph(edgeFile="dat1.csv",title1="node1",title2="node2")
    go=nt.mpolishing(gi=gi,sim="T",th=2,indirect=True).run()
    e=go.edges().run()
    print(e)
    # []
    ### result.csv の内容


関連メソッド
''''''''''''''''''''

* :doc:`mbipolish` : 2部グラフの研磨

