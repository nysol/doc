mcut 項目の選択
--------------------

指定した項目を選択する。
``r=True`` オプションを付けると、指定した項目を削除する。

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
     - | 抜き出す項目名
       | 項目名をコロンで区切ることで、出力項目名を変更することができる。
       | ex.  ``f=a:A,b:B``
   * - | **r=bool**
       | 任意
     - | 項目削除スイッチ
       | ``f=`` で指定した項目を削除し、それ以外の項目が抜き出される。
   * - | **nfni=bool**
       | 任意
     - | 入力データの１行目を項目名行とみなさない。よって項目番号で指定しなければならない。
       | 以下のように、新項目名を組み合わせて指定することで項目名行を追加出力することが可能となる。
       | 例）f=0:日付,2:店,3:数量


共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
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
    '''customer,quantity,amount
    A,1,10
    A,2,20
    B,1,15
    B,3,10
    B,1,20
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''A,1,10
    A,2,20
    B,1,15
    B,3,10
    B,1,20
    ''')


**基本例**

``customer`` と ``amount`` 項目を選択する。ただし、 ``amount`` 項目は ``sales`` と名前を変更して出力している。

  .. code-block:: python
    :linenos:

    nm.mcut(f="customer,amount:sales", i="dat1.csv", o="rsl1.csv").run()
