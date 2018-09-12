mavg 項目値の平均
----------------------

``f=`` パラメータで指定した項目の平均値を計算する。
``(注)`` k=とf=パラメータで指定した項目以外については、どの行が出力されるか>は不定であることに注意してください。\

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
     - | ここで指定した項目(複数項目指定可)の値が集計される。
       | :(コロン）で新項目名を指定可能。例） ``f=`` 数量:数量平均
   * - | **k=str**
       | 任意
     - | 集計の単位となる項目(複数項目指定可)名リストを指定する。
   * - | **n=bool**
       | 任意
     - | NULL値が1つでも含まれていると結果もNULL値とする。


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
