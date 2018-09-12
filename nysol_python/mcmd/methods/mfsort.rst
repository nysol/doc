mfsort 項目ソート
------------------------

各行で ``f=`` で指定した複数項目の値を並べ替え(デフォルトでは文字列昇順)、その順序で出力する。
項目名の並びは変化しないことに注意する。

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
     - | ソート対象となる項目を複数指定する。単一の項目を指定してもよいが、結果は変わらない。
   * - | **n=bool**
       | 任意
     - | 数値順に並べる。
   * - | **r=bool**
       | 任意
     - | 逆順に並べる。


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
    '''id,v1,v2,v3
    1,b,a,c
    2,a,b,a
    3,b,,e
    ''')


**例1: 基本例**

各行において  ``v1,v2,v3``  の値を昇順にならべ、その順番で  ``v1,v2,v3``  項目として出力する。

  .. code-block:: python
    :linenos:

    nm.mfsort(f="v*", i="dat1.csv", o="rsl1.csv").run()
