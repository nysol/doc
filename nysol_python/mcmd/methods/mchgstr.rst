mchgstr 文字列の置換
----------------------------

``f=`` パラメータで指定した項目について、
``c=`` パラメータで指定した置換条件で文字列を置換する。

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
   * - | **c=str**
       | 必須
     - | 置換対象となる文字列と置換文字列を指定する。
   * - | **f=str**
       | 必須
     - | ここで指定した項目(複数項目指定可)の文字列を ``c=`` パラメータで指定した置換条件リストに従って置換する。
   * - | **O=str**
       | 任意
     - | ``c=`` パラメータで指定した置換条件リストのいずれとも合致しない値を
       | 置換するときの文字列(指定がなければNULL値となる)を指定する。
   * - | **A=bool**
       | 任意
     - | このオプションにより、指定した項目を置き換えるのではなく、
   * - | **F=bool**
       | 任意
     - | ``c=`` パラメータで指定した置換条件リストのいずれとも合致しない値は、
       | その項目の値のまま出力する。
   * - | **sub=bool**
       | 任意
     - | 検索を完全一致ではなく部分文字列マッチで比較する
       | すなわち、 ``f=`` パラメータで指定した項目の値に、
       | ``c=`` パラメータで指定した置換条件で文字列を置換する。
   * - | **W=bool**
       | 任意
     - | ``sub=True`` オプションが指定されているときにワイド文字として部分文字列マッチをおこなう。


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
    '''id,item
    1,01
    2,02
    3,03
    4,04
    5,05
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,item
    1,0111
    2,0121
    3,0231
    4,0241
    5,0151
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''id,city
    1,奈良市
    2,下市町
    3,十津川村
    4,五條市
    5,山添村
    ''')


**基本例**

``item`` の値が
``"01"`` を ``"A"`` に、
``"03"`` を ``"B"`` に、
``"04"`` を ``"C"`` に置換する。
その他はNULL値として出力する。

  .. code-block:: python
    :linenos:

    nm.mchgstr(f="item", c="01:A,03:B,05:C", i="dat1.csv", o="rsl1.csv").run()
