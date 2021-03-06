mavg 項目値の平均
----------------------

``f=`` で指定した項目の平均値を計算する。
``k=`` と ``f=`` で指定した項目以外については、どの行が出力されるか>は不定であることに注意されたい。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | ここで指定した項目(複数項目指定可)の値が集計される。
  | :(コロン）で新項目名を指定可能。例） ``f=amount:average``

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 集計の単位となる項目(複数項目指定可)名リストを指定する。

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
    A,1,5
    A,2,20
    B,1,15
    B,,10
    B,5,20
    ''')


**基本例**

``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の平均値を計算し、 ``qttTotal`` と ``amtTotal`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mavg(k="customer", f="quantity:qttTotal,amount:amtTotal", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,qttTotal,amtTotal
    # A,1.5,12.5
    # B,3,15


**NULL値がある場合の出力**

``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の平均値を計算し、 ``qttTotal`` と ``amtTotal`` という項目名で出力する。
``n=True`` オプションを指定することで、NULL値が含まれている場合は、結果もNULL値として出力する。

  .. code-block:: python
    :linenos:

    nm.mavg(k="customer", f="quantity:qttTotal,amount:amtTotal", n=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer%0,qttTotal,amtTotal
    # A,1.5,12.5
    # B,,15


**顧客項目を単位としない例**

``quantity`` と ``amount`` 項目の平均値を計算し、 ``qttTotal`` と ``amtTotal`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mavg(f="quantity:qttTotal,amount:amtTotal", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer,qttTotal,amtTotal
    # B,2.25,14


関連メソッド
''''''''''''''''''''

* :doc:`mhashavg` : 集計キーを事前に並べ替えなくてよい分高速である。
* :doc:`msum` : 合計バージョン。
* :doc:`mstats` : その他の多様な統計量を求めるのであればこれ。

