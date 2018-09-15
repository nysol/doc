mdelnull NULL値行の削除
------------------------------------

``f=`` パラメータで指定した項目について、NULL値が含まれる行を削除(撰択)する。\

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | NULL値の検索対象となる項目名（複数項目指定可）を指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 削除(撰択)する単位となるキー項目名（複数項目指定可）を指定する。

**u=** : 型=str , 任意(default=出力しない)

  | 不一致データ出力データを指定する。

**bufcount=** : 型=str , 任意(default=)

  | バッファのサイズ数を指定する。

**F=** : 型=bool , 任意(default=False)

  | 項目間AND条件
  | ``f=`` パラメータで複数項目を指定した場合、その全ての値がNULL値の行を削除(撰択)する。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | 削除ではなく選択する。

**R=** : 型=bool , 任意(default=False)

  | レコード間AND条件
  | ``k=`` パラメータを指定した場合、その全ての行がNULL値の行を削除(撰択)する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`bufcount=<common_param_bufcount>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullkey=<common_param_assert_nullkey>`
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
    A,,20
    B,1,15
    B,3,
    C,1,20
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer,quantity,amount
    A,1,10
    A,,
    B,1,15
    B,3,
    C,1,20
    ''')


**基本例**

``quantity`` と ``amount`` 項目がNULL値の行を削除する。
NULL値の行は ``oth.csv`` に出力する。

  .. code-block:: python
    :linenos:

    nm.mdelnull(f="quantity,amount", u="oth.csv", i="dat1.csv", o="rsl1.csv").run()
    ### oth.csv の内容
    # customer,quantity,amount
    # A,,20
    # B,3,
    ### rsl1.csv の内容
    # customer,quantity,amount
    # A,1,10
    # B,1,15
    # C,1,20


**NULL値の行を選択**

``r=True`` を指定することで、削除ではなく選択することになる。

  .. code-block:: python
    :linenos:

    nm.mdelnull(f="quantity,amount", r=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer,quantity,amount
    # A,,20
    # B,3,


**キー項目でのNULL値の行の削除**

``k=`` を指定することで、集計キー単位で削除することになる。
以下では ``customer`` 項目を単位にして、 ``quantity`` と ``amount`` 項目にNULL値が一つでも含まれていれば削除する。

  .. code-block:: python
    :linenos:

    nm.mdelnull(k="customer", f="quantity,amount", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer%0,quantity,amount
    # C,1,20


**項目間AND条件の例**

``quantity`` と ``amount`` 項目の両方がNULL値の行を削除する。

  .. code-block:: python
    :linenos:

    nm.mdelnull(f="quantity,amount", F=True, i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # customer,quantity,amount
    # A,1,10
    # B,1,15
    # B,3,
    # C,1,20


**レコード間AND条件の例**

``customer`` 項目を単位にして、 ``quantity`` 項目が全てNULL値の行を削除する。

  .. code-block:: python
    :linenos:

    nm.mdelnull(k="customer", f="quantity", R=True, i="dat1.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # customer%0,quantity,amount
    # A,1,10
    # A,,20
    # B,1,15
    # B,3,
    # C,1,20


関連メソッド
''''''''''''''''''''

* :doc:`mnullto` : NULL値を含む行を削除するのではなく、NULL値を指定の文字列に変換する。

