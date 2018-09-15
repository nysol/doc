msum 項目値の合計
----------------------

``k=`` パラメータで指定した項目の値が同じ行について、
``f=`` パラメータで指定した集計項目の項目値を合計する。\
``(注)`` k=とf=パラメータで指定した項目以外については、どの行が出力されるかは不定であることに注意してください。\

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 集計の単位となる項目名リスト（複数項目指定可）を指定する。

**f=** : 型=str , 必須

  | ここで指定された項目（複数項目指定可）の値が集計される。NULL値は無視される。

**n=** : 型=bool , 任意(default=False)

  | ``f=`` で指定した項目にNULL値が入っていると計算結果もNULLとする。



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
, :ref:`tmpPath=<common_param_tmpPath>`
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
    B,1,15
    A,2,20
    B,3,10
    B,1,20
    ''')


**基本例**

``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の合計値を計算し、
``qttTotal`` と ``amtTotal`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.msum(k="customer", f="quantity:qttTotal,amount:amtTotal", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,qttTotal,amtTotal
    # A,3,30
    # B,5,45


関連メソッド
''''''''''''''''''''

* :doc:`mhashsum` : 集計キーを事前に並べ替えなくても計算できる。
* :doc:`mavg` : 平均バージョン。
* :doc:`mstats` : その他の多様な統計量を求めるのであればこれ。

