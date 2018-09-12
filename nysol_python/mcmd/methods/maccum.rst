maccum 累積計算
----------------------

``f=`` パラメータで指定した項目の累積を計算し、新しい項目として追加する。
``k=`` を指定することで、キー単位毎に累積計算が可能となる。

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
     - | ここで指定した項目(複数項目指定可)の値が累積される。
       | 項目の値がNULL値である場合は無視される。
       | :(コロン）で新項目名を指定する必要がある。例） ``f=数量:数量累計``
   * - | **s=str**
       | 必須
     - | ここで指定した項目(複数項目指定可)で並べ替えられた後、累積が計算される。
       | ``q=True`` オプションを指定しないとき、 ``s=`` パラメータは必須。
   * - | **k=str**
       | 任意
     - | 累積の単位となる項目名リスト(複数項目指定可)を指定する。


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
