mmvavg 移動平均の算出
----------------------------

移動平均(moving average)を算出する。
移動平均としては、単純移動平均( :math:`SMA` )、線形荷重移動平均( :math:`WMA` )、指数平滑移動平均( :math:`EMA` )の３種類の移動平均が計算可能である。
ある時 :math:`t` における値を :math:`x_t` で表したとき、 :math:`m` 期の各種移動平均は式(ef{eq:sma},ef{eq:wma},ef{eq:ema})で定義される。
egin{eqnarray}
SMA_t=rac{1}{m} \sum_{i=0}^{m-1} x_{t-i}
\label{eq:sma}
\end{eqnarray}
egin{eqnarray}
WMA_t=\sum_{i=0}^{m-1} rac{m-i}{S} x_{t-i},\ \ S=\sum_{i=1}^m i
\label{eq:wma}
\end{eqnarray}
egin{eqnarray}
EMA_t=lpha x_t + (1-lpha)EMA_{t-1}
\label{eq:ema}
\end{eqnarray}


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**s=** : 型=str , 任意(default=)

  | ここで指定した項目(複数項目指定可)で並べ替えられた後、移動平均が計算される。
  | ``q`` オプションを指定しないとき、 ``s=`` パラメータは必須。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | ここで指定された項目(複数項目指定可)を単位として集計する。

**f=** : 型=str , 必須

  | 移動平均を求める項目名リスト(複数項目指定可)を指定する。

**t=** : 型=str , 任意(default=)

  | 期間数を1以上の整数で指定する。
  | ``exp`` オプション指定時に ``alpha=`` を指定すれば ``t=`` は指定できない。

**w=** : 型=bool , 任意(default=False)

  | 線形加重移動平均を求める。

**exp=** : 型=bool , 任意(default=False)

  | 指数平滑移動平均を求める。

**alpha=** : 型=str , 任意(default=)

  | ``exp`` オプションが指定された時の平滑化係数を実数値で与える。
  | 省略時は ``alpha=2/(t=の値+1)`` 。

**skip=** : 型=str , 任意(default=)

  | 出力を抑制する最初の行数。
  | デフォルト値:  ``skip=(t=の値-1)`` ,  ``exp`` オプションが指定された場合は ``skip=0``

**n=** : 型=bool , 任意(default=False)

  | 期間内にNULL値が1つでも含まれていると結果もNULL値とする。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullkey=<common_param_assert_nullkey>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
, :ref:`x=<common_param_x>`
, :ref:`q=<common_param_q>`
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
    '''id,value
    1,5
    2,1
    3,3
    4,4
    5,4
    6,6
    7,1
    8,4
    9,7
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,key,value
    1,a,5
    2,a,1
    3,a,3
    4,a,4
    5,a,4
    6,b,6
    7,b,1
    8,b,4
    9,b,7
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''key,value
    a,1
    a,2
    a,3
    a,4
    a,5
    b,6
    b,1
    b,4
    b,7
    ''')


**基本例**

最初の行は期数に満たないため出力されない。

  .. code-block:: python
    :linenos:

    nm.mmvavg(s="id", f="value", t="2", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id%0,value
    # 2,3
    # 3,2
    # 4,3.5
    # 5,4
    # 6,5
    # 7,3.5
    # 8,2.5
    # 9,5.5


**基本例2**

最初の行は期数に満たないため出力されない。

  .. code-block:: python
    :linenos:

    nm.mmvavg(s="id", f="value", t="2", w=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id%0,value
    # 2,2.333333333
    # 3,2.333333333
    # 4,3.666666667
    # 5,4
    # 6,5.333333333
    # 7,2.666666667
    # 8,3
    # 9,6


**基本例3**

指数平滑移動平均( ``exp=True`` )の場合は最初の行から出力される。

  .. code-block:: python
    :linenos:

    nm.mmvavg(s="id", f="value", t="2", exp=True, i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id%0,value
    # 1,5
    # 2,2.333333333
    # 3,2.777777778
    # 4,3.592592593
    # 5,3.864197531
    # 6,5.288065844
    # 7,2.429355281
    # 8,3.47645176
    # 9,5.82548392


**キーを指定する例**


  .. code-block:: python
    :linenos:

    nm.mmvavg(s="key,id", k="key", f="value", t="2", i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,key,value
    # 2,a,3
    # 3,a,2
    # 4,a,3.5
    # 5,a,4
    # 7,b,3.5
    # 8,b,2.5
    # 9,b,5.5


**指定した期に満たなくても出力する例**


  .. code-block:: python
    :linenos:

    nm.mmvavg(q=True, k="key", f="value", t="2", skip="0", i="dat3.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # key,value
    # a,1
    # a,1.5
    # a,2.5
    # a,3.5
    # a,4.5
    # b,6
    # b,3.5
    # b,2.5
    # b,5.5


関連メソッド
''''''''''''''''''''

* :doc:`mmvstats` : 平均だけでなく、各種統計量を指定可能。
* :doc:`mmvsim` : 2変量の統計量を計算する。
* :doc:`mwindow` : 動窓のデータを作成するので、そのデータを使えば ``mmvstats`` で計算できない統計量も計算可能。

