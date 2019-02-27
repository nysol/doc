mstats 一変数の統計量算出
--------------------------------

``f=`` パラメータで指定した数値項目について
``c=`` パラメータで指定した統計量の計算をする。
``k=`` を指定することで、キー単位で集計することができる。
``f=`` で指定した項目のNULL値は無視される。
ただし、全行がNULL値であればNULL値が出力される。
``(注)`` k=とf=パラメータで指定した項目以外については、どの行が出力されるか>は不定であることに注意してください。\


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | ここで指定された項目(複数項目指定可)を単位として集計する。

**f=** : 型=str , 必須

  | ここで指定された項目(複数項目指定可)の値が集計される。

**c=** : 型=str , 必須

  | 統計量(以下のリストから一つだけ指定可)
  | ``sum|mean|count|ucount|devsq|var|uvar|sd|usd|USD|cv|min|qtile1|``
  | ``median|qtile3|max|range|qrange|mode|skew|uskew|kurt|ukurt``

**n=** : 型=bool , 任意(default=False)

  | NULL値が1つでも含まれていると結果もNULL値とする。



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
    '''customer,quantity,amount
    A,1,10
    B,5,20
    B,2,10
    C,1,15
    C,3,10
    C,1,21
    ''')


**基本例**

``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の
各統計量合計値を計算する。

  .. code-block:: python
    :linenos:

    nm.mstats(k="customer", f="quantity,amount", c="sum", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,quantity,amount
    # A,1,10
    # B,7,30
    # C,5,46


**基本例2**

各統計量最大値を計算する。

  .. code-block:: python
    :linenos:

    nm.mstats(k="customer", f="quantity,amount", c="max", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer%0,quantity,amount
    # A,1,10
    # B,5,20
    # C,3,21


関連メソッド
''''''''''''''''''''

* :doc:`msim` : 2変量の統計量を求める。
* :doc:`mavg` : ``c=avg`` に特化したコマンド。
* :doc:`msum` : ``c=sum`` に特化したコマンド。
* :doc:`mcount` : ``c=count`` と異なり、集計キーの行数をカウントする。

