mmvstats 移動窓の統計量の計算
--------------------------------------

移動窓を設定し、各種統計量(1変量)を計算する。
:doc:`mstats` コマンドの移動窓バージョンとして考えればよい。

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
   * - | **s=str**
       | 任意
     - | ここで指定した項目(複数項目指定可)で並べ替えられた後、各種統計量が計算される。
       | erb|-q|オプションを指定しないとき、erb|s=|パラメータは必須。
   * - | **k=str**
       | 任意
     - | ここで指定された項目(複数項目指定可)を単位として集計する。
   * - | **f=str**
       | 必須
     - | 集計項目名リスト(複数項目指定可)を指定する。
   * - | **t=str**
       | 任意
     - | 期間数を1以上の整数で指定する。
   * - | **c=str**
       | 必須
     - | 統計量(以下のリストから一つだけ指定可)
       | ``sum|mean|devsq|var|uvar|sd|usd|cv|min|``
       | ``|max|range|skew|uskew|kurt|ukurt``
       | 詳細な定義は :doc:`mstats` コマンドを参照のこと。
   * - | **skip=str**
       | 任意
     - | 出力を抑制する最初の行数
   * - | **n=bool**
       | 任意
     - | 期間内にNULL値が1つでも含まれていると結果もNULL値とする。


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
    '''id,value
    1,5
    2,1
    3,3
    4,4
    5,4
    6,6
    7,1
    8,4
    9,7
    ''')


**基本例**

移動窓の合計を計算する。
最初の行は期数に満たないため出力されない。

  .. code-block:: python
    :linenos:

    nm.mmvstats(s="id", f="value", t="2", c="sum", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id%0,value
    # 2,6
    # 3,4
    # 4,7
    # 5,8
    # 6,10
    # 7,7
    # 8,5
    # 9,11


