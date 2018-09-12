mdelnull NULL値行の削除
------------------------------------

``f=`` パラメータで指定した項目について、NULL値が含まれる行を削除(撰択)する。\

パラメータ
''''''''''''''''''''''

  .. list-table::
   :header-rows: 1

   * - キーワード
     - 内容
   * - | **i=str**
       | 任意
     - | 入力データを指定する。
   * - | **o=str**
       | 任意
     - | 出力データを指定する。
   * - | **f=str**
       | 必須
     - | NULL値の検索対象となる項目名（複数項目指定可）を指定する。
   * - | **k=str**
       | 任意
     - | 削除(撰択)する単位となるキー項目名（複数項目指定可）を指定する。
   * - | **u=str**
       | 任意
     - | 不一致データ出力データを指定する。
   * - | **bufcount=str**
       | 任意
     - | バッファのサイズ数を指定する。
   * - | **F=bool**
       | 任意
     - | 項目間AND条件
       | ``f=`` パラメータで複数項目を指定した場合、その全ての値がNULL値の行を削除(撰択)する。
   * - | **r=bool**
       | 任意
     - | 条件反転
       | 削除ではなく選択する。
   * - | **R=bool**
       | 任意
     - | レコード間AND条件
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
