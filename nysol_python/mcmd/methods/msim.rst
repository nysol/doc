msim 二変数間の類似度の計算
--------------------------------

``f=`` パラメータで指定した項目の二変数間の類似度(距離)を
``c=`` パラメータで指定した類似度(距離)関数で計算し類似度行列として出力する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | ここで指定された項目(複数項目指定可)を単位として求める。

**f=** : 型=str , 必須

  | ここで指定された項目全ての二項目間の類似度を求める。

**c=** : 型=str , 必須

  | 類似度(距離)名リスト(複数項目指定可)
  | 次項に示した類似度(距離)名を指定する。
  | 項目名は以下のように，(:)コロンに続けて指定して変更可能。
  | コロンに続く名称を省略した場合は類似度(距離)関数名がそのまま項目名として利用される。
  | 例)  ``msim f=x,y,z c=pearson:ピアソン積率相関係数,euclid:ユークリッド距離,cosine:コサイン``
  | 類似度 ``=covar|ucovar|pearson|spearman|kendall|euclid|cosine|``
  | ~~ ``cityblock|hamming|chi|phi|jaccard|supportr|lift|confMax|``
  | ~~ ``confMin|yuleQ|yuleY|kappa|oddsRatio|convMax|convMin``

**a=** : 型=str , 任意(default=)

  | 2変数の名称を示す項目名を指定する。カンマで区切って2つ指定する。
  | 省略すると ``fld1,fld2`` が使われる。

**d=** : 型=bool , 任意(default=False)

  | 対角行列、上三角行列を出力する。
  | ``d`` オプションが指定されないと類似度行列の下三角行列のみ出力されるが、
  | ``d`` オプションを指定することにより対角行列及び上三角行列も出力される。

**n=** : 型=bool , 任意(default=False)

  | NULL値が1つでも含まれていると結果もNULL値とする。

**bufcount=** : 型=str , 任意(default=)

  | バッファのサイズ数を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`bufcount=<common_param_bufcount>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullkey=<common_param_assert_nullkey>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`x=<common_param_x>`
, :ref:`tmppath=<common_param_tmppath>`
, :ref:`precision=<common_param_precision>`


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''x,y,z
    14,0.17,-14
    11,0.2,-1
    32,0.15,-2
    13,0.33,-2
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''key,x,y,z
    A,14,0.17,-14
    A,11,0.2,-1
    A,32,0.15,-2
    B,13,0.33,-2
    B,10,0.8,-5
    B,15,0.45,-9
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''x,y,z
    1,1,0
    1,0,1
    1,0,1
    0,1,1
    ''')


**基本例**

``x、y、z`` 項目の2項目間の組み合わせについて
ピアソンの積率相関係数とコサインを計算する。

  .. code-block:: python
    :linenos:

    nm.msim(c="pearson,cosine", f="x,y,z", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # fld1,fld2,pearson,cosine
    # x,y,-0.5088704666,0.7860308044
    # x,z,0.1963041929,-0.5338153343
    # y,z,0.3311001423,-0.5524409416


**対角行列、上三角行列を出力**

``x、y、z`` 項目の2項目間の組み合わせについて
ピアソンの積率相関係数とコサインを計算する。(dオプションあり)

  .. code-block:: python
    :linenos:

    nm.msim(c="pearson,cosine", f="x,y,z", d=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # fld1,fld2,pearson,cosine
    # x,x,1,1
    # x,y,-0.5088704666,0.7860308044
    # x,z,0.1963041929,-0.5338153343
    # y,x,-0.5088704666,0.7860308044
    # y,y,1,1
    # y,z,0.3311001423,-0.5524409416
    # z,x,0.1963041929,-0.5338153343
    # z,y,0.3311001423,-0.5524409416
    # z,z,1,1


**キー単位での計算**

``key`` 項目を単位にして計算する。

  .. code-block:: python
    :linenos:

    nm.msim(k="key", c="pearson,cosine", f="x,y,z", i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # key%0,fld1,fld2,pearson,cosine
    # A,x,y,-0.8746392857,0.8472573627
    # A,x,z,0.3164384831,-0.521983618
    # A,y,z,0.1830936883,-0.6719258683
    # B,x,y,-0.7919009884,0.8782575583
    # B,x,z,-0.471446429,-0.9051543403
    # B,y,z,-0.1651896746,-0.8514129252


**類似度名の指定**

01値のデータに付いての計算。ハミング距離とphi係数を計算する。

  .. code-block:: python
    :linenos:

    nm.msim(c="hamming,phi", f="x,y,z", i="dat3.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # fld1,fld2,hamming,phi
    # x,y,0.75,-0.5773502692
    # x,z,0.5,-0.3333333333
    # y,z,0.75,-0.5773502692


**類似度名の変更**

01値のデータに付いての計算。ハミング距離とphi係数を計算し、
出力項目名を変更する。

  .. code-block:: python
    :linenos:

    nm.msim(c="hamming:ハミング距離,phi:ファイ係数", a="変数1,変数2", f="x,y,z", i="dat3.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # 変数1,変数2,ハミング距離,ファイ係数
    # x,y,0.75,-0.5773502692
    # x,z,0.5,-0.3333333333
    # y,z,0.75,-0.5773502692


関連メソッド
''''''''''''''''''''

* :doc:`mstats` : 1変量の統計量を計算するときはこちら。
* :doc:`mmvsim` : 移動窓を設定した類似度計算。

