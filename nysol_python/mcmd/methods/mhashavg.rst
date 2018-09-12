mhashavg ハッシュ法による項目値の平均
----------------------------------------------

hash法を使って ``k=`` パラメータで指定した項目を単位にして、 ``f=`` パラメータで指定した項目値の平均を計算する。
:doc:`mavg` との違いは、キー項目の並べ変えが必要ないため、その分処理速度が速い。
ただし、キーのサイズ(キー項目のとる値の種類数)が多い場合は処理速度が遅くなる。

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
     - | ここで指定された項目(複数項目指定可)の平均が計算される。
       | :(コロン）で新項目名を指定可能。例） ``f=`` 数量:数量平均
   * - | **k=str**
       | 任意
     - | ここで指定された項目をキーとして集計する(複数項目指定可)。
   * - | **hs=str**
       | 任意
     - | ハッシュサイズ
       | ハッシュサイズを指定する。
       | 詳細に関しては :doc:`mhashsum` 参照
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
    A,1,
    B,,15
    A,2,20
    B,3,10
    B,1,20
    ''')


**基本例**

``customer`` 項目を単位にして、 ``quantity`` と ``amount`` 項目の平均を計算する。

  .. code-block:: python
    :linenos:

    nm.mhashavg(k="customer", f="quantity,amount", i="dat1.csv", o="rsl1.csv").run()
