mclique クリークの列挙
------------------------------

一般グラフデータから極大クリークを列挙する。

**入力形式**: 一般グラフを節点ペアで表現した形式。他のいかなる節点とも接続のない節点は、サイズが1の自明なクリークであるため、入力対象外とする。

**出力形式**: クリークIDと接点を出力する。出力項目は ``id,node,size`` の3項目である。sizeはクリークを構成する節点数である。


パラメータ
''''''''''''''''''''''

**ei=** : 型=str , 必須

  | 辺データファイルを指定する。

**ef=** : 型=str , 任意(default=node1,node2)

  | エッジデータ上の2つのノード項目名を指定する。

**ni=** : 型=str , 必須

  | 節点データファイルを指定する。

**nf=** : 型=str , 任意(default=node)

  | 節点データ上の節点項目名を指定する。

**o=** : 型=str , 必須

  | 出力ファイル名を指定する。

**l=** : 型=int , 任意(default=制限なし)

  | クリークを構成する最小節点数(ここで指定したサイズより小さいクリークは列挙されない)を指定する。

**u=** : 型=int , 任意(default=制限なし)

  | クリークを構成する最大節点数(ここで指定したサイズより大きいクリークは列挙されない)を指定する。

**all=** : 型=bool , 任意(default=False)

  | 極大クリークだけでなく、全クリークを列挙する。

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
    a,b
    a,c
    a,d
    a,e
    b,c
    b,d
    b,f
    c,d
    c,e
    d,e
    e,f
    ''')


**基本例**

グラフデータ ``dat.csv`` から極大クリークを列挙し ``result.csv`` に出力する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mclique(ei="dat.csv", ef="node1,node2", o="result.csv")
    ### result.csv の内容


**サイズの指定**

サイズが4以上の極大クリークのみ列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mclique(ei="dat.csv", ef="node1,node2", l=4, o="result.csv")
    ### result.csv の内容


**全クリーク列挙**

サイズが4以上の全クリークを列挙する。

  .. code-block:: python
    :linenos:

    import nysol.take as nt
    nt.mclique(ei="dat.csv", ef="node1,node2", l=3, u=3, all=True, o="result.csv")
    ### result.csv の内容


関連メソッド
''''''''''''''''''''

* :doc:`mbiclique` : クリーク列挙

