mcross クロス集計
------------------------

クロス集計を行う。
``s=`` で指定した項目の値が項目名となるように横に展開され、
``k=`` で指定した値が行idとなり、
``f=`` で指定した項目がセルとして出力される。

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
     - | ここで指定された項目の値がセルの値として出力される。
       | 複数項目指定すると、複数行に展開される。
       | それら複数行を識別するための項目として ``fld`` 項目が出力され、
       | ``f=`` で指定した項目名が値として出力される。
       | この ``fld`` という項目名を変更したい場合は ``a=`` パラメータを使う。
   * - | **s=str**
       | 必須
     - | 列項目名に展開する項目を指定する。
       | ここで指定された項目の値が項目名として出力される。
   * - | **a=str**
       | 任意
     - | ``f=`` で指定した項目名がデータとして展開される項目名を指定する。
       | 省略した場合は ``fld`` という項目名で出力される。
   * - | **k=str**
       | 任意
     - | キー項目名リスト
       | ここで指定した項目を単位に横展開をおこなう。
   * - | **v=str**
       | 任意
     - | NULL値置換文字列
       | NULL値があった場合、 ``v=`` パラメータで指定する置換文字列により、項目の値を置換する。


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
    '''item,date,quantity,price
    A,20081201,1,10
    A,20081202,2,20
    A,20081203,3,30
    B,20081201,4,40
    B,20081203,5,50
    ''')


**基本例**

``item`` 項目を単位に ``date`` 項目を横に展開し、
``quantity`` 項目を出力する。

  .. code-block:: python
    :linenos:

    nm.mcross(k="item", f="quantity", s="date", i="dat1.csv", o="rsl1.csv").run()
