mchgnum 数値範囲による置換
----------------------------------

``f=`` パラメータで指定した項目について、 ``R=`` パラメータで指定する
数値範囲条件と ``v=`` パラメータで指定する置換文字列により、項目の値を置換する。

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
     - | ここで指定した項目(複数項目指定可)の数値を ``R=`` と ``v=`` パラメータで指定した
       | 数値範囲リストおよび置換文字列リストに従って置換する。
   * - | **R=str**
       | 必須
     - | 置換対象となる数値範囲を指定(複数項目指定可)する( ``1.1,2.5``  : 1.1以上2.5未満)。
       | 最小値、最大値として ``MIN,MAX`` を使うことができる( ``MIN,2.5``  : 2.5未満)。
   * - | **O=str**
       | 任意
     - | 範囲外文字列
       | ``R=`` パラメータで指定した数値範囲リストのいずれとも合致しない値を
       | 置換するときの文字列(指定がなければNULL値となる)を指定する。
   * - | **F=bool**
       | 任意
     - | 範囲外を項目の値として出力
       | ``R=`` パラメータで指定した数値範囲リストのいずれとも
       | 合致しない値は、その項目の値のまま出力する。
   * - | **v=str**
       | 任意
     - | ``R=`` パラメータで指定した数値範囲に対応する置換文字列を指定する。
       | ``R=`` で指定した値の個数より1つ少い個数でなければならない。
   * - | **A=bool**
       | 任意
     - | このオプションにより、指定した項目を置き換えるのではなく、新たに項目が追加される。
   * - | **r=bool**
       | 任意
     - | ``R=`` パラメータの範囲を'〜より大きく〜以下'として扱う。
       | 例えば、 ``1.1_2.5`` は「1.1より大きく2.5以下」として扱う。


共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
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
    '''customer,quantity
    A,5
    B,10
    C,15
    D,2
    E,50
    ''')


**基本例**

``quantity`` 項目の値が最小以上10未満を ``low`` 、
10以上20未満を ``middle`` 、20以上最大未満を ``high`` という文字列に置換する。

  .. code-block:: python
    :linenos:

    nm.mchgnum(f="quantity", R="MIN,10,20,MAX", v="low,middle,high", i="dat1.csv", o="rsl1.csv").run()
