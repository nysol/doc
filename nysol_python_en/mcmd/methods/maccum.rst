maccum 累積計算
----------------------

``f=`` パラメータで指定した項目の累積を計算し、新しい項目として追加する。
``k=`` を指定することで、キー単位毎に累積計算が可能となる。


パラメータ
''''''''''''''''''''''

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 累積の単位となる項目名リスト(複数項目指定可)を指定する。

**s=** : 型=str , 条件付き必須( ``q`` オプションの指定がない場合)

  | ここで指定した項目(複数項目指定可)で並べ替えられた後、累積が計算される。
  | ``q`` オプションを指定しないとき、 ``s=`` パラメータは必須。

**f=** : 型=str , 必須

  | ここで指定した項目(複数項目指定可)の値が累積される。
  | 項目の値がNULL値である場合は無視される。
  | :(コロン）で新項目名を指定する必要がある。例） ``f=数量:数量累計``

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。



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
    A,2,20
    B,1,15
    B,3,10
    B,1,20
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer,quantity,amount
    A,1,10
    A,,20
    B,1,15
    B,3,
    B,1,20
    ''')


**基本例**

``quantity`` と ``amount`` 項目の累積値を計算し、 ``qttAccum`` と ``amtAccum`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.maccum(s="customer", f="quantity:qttAccum,amount:amtAccum", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,quantity,amount,qttAccum,amtAccum
    # A,1,10,1,10
    # A,2,20,3,30
    # B,1,15,4,45
    # B,3,10,7,55
    # B,1,20,8,75


**キー項目を指定する例**

``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の累積値を計算し、 ``qttAccum`` と ``amtAccum`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.maccum(k="customer", s="customer", f="quantity:qttAccum,amount:amtAccum", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer,quantity,amount,qttAccum,amtAccum
    # A,1,10,1,10
    # A,2,20,3,30
    # B,1,15,1,15
    # B,3,10,4,25
    # B,1,20,5,45


**NULL値を含む累計**

``quantity`` と ``amount`` 項目の累積値を計算し、 ``qttAccum`` と ``amtAccum`` という項目名で出力する。
NULLは無視される。結果もNULLが出力される。

  .. code-block:: python
    :linenos:

    nm.maccum(s="customer", f="quantity:qttAccum,amount:amtAccum", i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer%0,quantity,amount,qttAccum,amtAccum
    # A,1,10,1,10
    # A,,20,,30
    # B,1,15,2,45
    # B,3,,5,
    # B,1,20,6,65


関連メソッド
''''''''''''''''''''

* :doc:`mshare` : 構成比を計算する。 ``maccum`` と組み合わせて累積相対度数が計算できる。
* :doc:`mcal` : 前行の計算結果 ``#{}`` を利用することで累計計算ができる。

