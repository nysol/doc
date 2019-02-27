mbiclique 極大2部クリークの列挙
------------------------------------------

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


パラメータ
''''''''''''''''''''''

**ei=** : 型=str , 必須

  | 辺データファイルを指定する。

**ef=** : 型=str , 任意(default=node1,node2)

  | エッジデータ上の2つのノード項目名を指定する。

**o=** : 型=str , 必須

  | 出力ファイル名を指定する。

**l=** : 型=str , 任意(default=制限なし)

  | 2部クリークを構成する最小節点数(ここで指定したサイズより小さいクリークは列挙されない)を指定する。
  | カンマで区切って2つの値を指定すると、各部のサイズを制限できる。
  | 1つ目の値はef=で指定した1つ目の部に対応し、2つ目の値は2つ目に指定した部に対応する。

**u=** : 型=str , 任意(default=制限なし)

  | クリークを構成する最大節点数(ここで指定したサイズより大きいクリークは列挙されない)を指定する。
  | カンマで区切って2つの値を指定すると、各部のサイズを制限できる

**edge=** : 型=bool , 任意(default=False)

  | 枝による出力(クリークIDと枝(節点ペア)で出力する)。

**T=** : 型=str , 任意(default=/tmp)

  | ワークディレクトリを指定する。



利用例
''''''''''''

**入力データの準備**

  .. code-block:: python
    :linenos:

    with open('dat.csv','w') as f:
      f.write(
    '''node1,node2
    a,A
    a,B
    a,C
    b,A
    b,B
    b,D
    c,A
    c,D
    d,B
    d,C
    d,D
    ''')


**基本例**

2部グラフデータ ``dat.csv`` から極大2部クリークを列挙し ``result.csv`` に出力する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mbiclique(ei="dat.csv", ef="node1,node2", o="result.csv").run()
    ### result.csv の内容
    # node1%0,node2%1,size1,size2
    # a,A B C,1,3
    # a b,A B,2,2
    # a b c,A,3,1
    # a b d,B,3,1
    # a d,B C,2,2
    # b,A B D,1,3
    # b c,A D,2,2
    # b c d,D,3,1
    # b d,B D,2,2
    # d,B C D,1,3


**サイズを制限する例**

項目 ``node1,node2`` 共にサイズが2の極大二部クリークを列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mbiclique(ei="dat.csv", ef="node1,node2", l="2,2",u="2,2", o="result.csv").run()
    ### result.csv の内容
    # node1%0,node2%1,size1,size2
    # a b,A B,2,2
    # a d,B C,2,2
    # b c,A D,2,2
    # b d,B D,2,2


**エッジ形式での出力**

``edge=True`` によって、出力形式がエッジ形式(ノードペア)になる。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mbiclique(ei="dat.csv", ef="node1,node2", l="2,2",u="2,2", edge=True, o="result.csv").run()
    ### result.csv の内容
    # id%0,node1,node2,size1,size2
    # 0,a,A,2,2
    # 0,a,B,2,2
    # 0,b,A,2,2
    # 0,b,B,2,2
    # 1,b,A,2,2
    # 1,b,D,2,2
    # 1,c,A,2,2
    # 1,c,D,2,2
    # 2,b,B,2,2
    # 2,b,D,2,2
    # 2,d,B,2,2
    # 2,d,D,2,2
    # 3,a,B,2,2
    # 3,a,C,2,2
    # 3,d,B,2,2
    # 3,d,C,2,2


**部分的にサイズを制限する例**

項目 ``node1`` のサイズの下限を1に(デフォルトの下限が1なので実際には意味がないが指定例として)、
項目 ``node2`` のサイズの上限を3に制限した極大二部クリークを列挙する。
``u=` パラメータの1番目の値がnullになっているのは、項目 ``node1`` の上限を設定しないためである。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mbiclique(ei="dat.csv", ef="node1,node2", l="1,",u=",3", o="result.csv").run()
    ### result.csv の内容
    # node1%0,node2%1,size1,size2
    # a,A B C,1,3
    # a b,A B,2,2
    # a b c,A,3,1
    # a b d,B,3,1
    # a d,B C,2,2
    # b,A B D,1,3
    # b c,A D,2,2
    # b c d,D,3,1
    # b d,B D,2,2
    # d,B C D,1,3


関連メソッド
''''''''''''''''''''

* :doc:`mclique` : 一般グラフのクリーク列挙

