mbipolish 2部グラフの研磨
------------------------------------

2部グラフデータを入力として、密度の高い部分グラフの中でエッジが張られていないノードペアに枝を張る。
逆に、密度の低い部分グラフのエッジを削除する。
新たに張られる枝や刈られる枝の程度は、``sim=`` , ``th=`` と ``sim2=`` , ``th2=`` で与えた値によって変わる。


パラメータ
''''''''''''''''''''''

**ei=** : 型=str , 必須

  | エッジデータファイル名を指定する。

**ef=** : 型=str , 任意(default=node1,node2)

  | エッジデータ上の2つのノード項目名を指定する。

**eo=** : 型=str , 必須

  | データ研磨後のエッジデータファイル名を指定する。

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

**sim2=** : 型=str , 任意(default=sim=の値)

  | 指定できる値は ``sim=`` と同じ。

**th=** : 型=float , 必須

  | ``sim=`` で指定された類似度について、ここで指定された値以上の節点間に辺を張る。

**th2=** : 型=float , 任意(default=th=の値)

  | ``sim2=`` で指定された類似度について、ここで指定された値以上の節点間に辺を張る。

**sup=** : 型=int , 任意(default=0)

  | 左の部の次数がsup以上のノードを対象とする。省略すればsup=0。

**kn=** : 型=int , 任意(default=1)

  | kn=で指定された値以上の共起頻度を対象とする。

**kn2=** : 型=int , 任意(default=1)

  | kn2=で指定された値以上の次数を持つ右部を対象とする。

**iter=** : 型=int , 任意(default=30)

  | データ研磨の最大繰り返し数を指定する。

**O=** : 型=str , 任意(default=研磨過程を出力しない)

  | デバッグモード時、データ研磨過程のグラフを保存するディレクトリ名を指定する。

**log=** : 型=str , 任意(default=ログを出力しない)

  | パラメータの設定値や収束回数等をkey-value形式のCSVで保存するファイル名を指定する。

**T=** : 型=str , 任意(default=/tmp)

  | ワークディレクトリ名を指定する。



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('edge.csv','w') as f:
      f.write(
    '''node1,node2
    A,a
    A,b
    B,a
    B,b
    C,c
    C,d
    D,b
    D,e
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mbipolish(ei="edge.csv",ef="node1,node2", th=0.2, eo="output.csv").run()
    ### output.sv の内容


関連メソッド
''''''''''''''''''''

* :doc:`mpolishing` : 一般グラフの研磨

