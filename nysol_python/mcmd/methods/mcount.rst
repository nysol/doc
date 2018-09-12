mcount 行数カウント
--------------------------

行数をカウントし、 ``a=`` パラメータで指定した項目名で出力する。
``k=`` を指定すると、集計キー毎の件数をカウントし、
``k=`` を指定しなければ、全行数がカウントされる。

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
   * - | **a=str**
       | 必須
     - | 新たに追加される項目の名前を指定する。
       | ``nfn`` オプション使用時は、必須ではない。
   * - | **k=str**
       | 任意
     - | キー項目名リスト(複数項目指定可)
       | カウントの単位となる項目名リスト。


共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
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
    '''date
    20090109
    20090109
    20090110
    20090109
    20090110
    ''')


**基本例**

``date`` 項目を単位に行数をカウントし、 ``count`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mcount(k="date", a="count", i="dat1.csv", o="rsl1.csv").run()
