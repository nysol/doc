mkeybreak キーブレイク箇所
------------------------------------------------------

``k=`` パラメータで指定した項目をキー項目について、先頭と終端に印を付ける。
先頭は ``top`` 項目に、終端は ``bot`` 項目に ``1`` を出力する。
先頭/終端でない行はNULL値を出力する。

パラメータ
''''''''''''''''''''''

  .. list-table::
    :header-rows: 1

    * - キーワード
      - 内容

    * - | **i=**
        |   任意
        |   デフォルト:標準入力
      - |   入力データを指定する。
    * - | **o=**
        |   任意
        |   デフォルト:標準出力
      - |   出力データを指定する。
    * - | **k=**
        |   必須
      - |   集計キーとなる項目名リスト（複数項目指定可）を指定する。
    * - | **s=**
        |   任意
        |   デフォルト:
      - |   ここで指定した項目(複数項目指定可)で並べ替えた後、先頭・終端に印を付ける。
    * - | **a=**
        |   任意
        |   デフォルト:top,bot
      - |   先頭と終端の印を出力する項目名を指定する。

共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullkey=<common_param_assert_nullkey>`
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
    '''id,k1,k2,val
    1,A,a,1
    2,A,b,2
    3,A,b,3
    4,B,a,4
    5,B,a,5
    ''')
    
**基本例**

``k1`` 項目で並べ替えた後、 ``k1`` キー項目の先頭( ``top`` 項目)と終端( ``bottom`` 項目)に印( ``1`` )をつける。


  .. code-block:: python
    :linenos:

    >>> nm.mkeybreak(k="k1", i="dat1.csv", o="rsl1.csv").run()
    # ## rsl1.csv の内容
    # id,k1%0,k2,val,top,bot
    # 1,A,a,1,1,
    # 2,A,b,2,,
    # 3,A,b,3,,1
    # 4,B,a,4,1,
    # 5,B,a,5,,1

**2項目キー**

``k1`` ・ ``k2`` 項目で並べ替えた後、 ``k1`` キー項目の先頭( ``top`` 項目)と終端( ``bottom`` 項目)に印( ``1`` )をつける。


  .. code-block:: python
    :linenos:

    >>> nm.mkeybreak(s="k1,k2", k="k1", i="dat1.csv", o="rsl2.csv").run()
    # ## rsl2.csv の内容
    # id,k1,k2,val,top,bot
    # 1,A,a,1,1,
    # 2,A,b,2,,
    # 3,A,b,3,,1
    # 4,B,a,4,1,
    # 5,B,a,5,,1



関連メソッド
''''''''''''

