mchgnum 数値範囲による置換
---------------------------------------------------

``f=`` パラメータで指定した項目について、 ``R=`` パラメータで指定する
数値範囲条件と ``v=`` パラメータで指定する置換文字列により、項目の値を置換する。

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
    * - | **f=**
        |   必須
      - |   ここで指定した項目(複数項目指定可)の数値を ``R=`` と ``v=`` パラメータで指定した
        |   数値範囲リストおよび置換文字列リストに従って置換する。
    * - | **R=**
        |   必須
      - |   置換対象となる数値範囲を指定(複数項目指定可)する( ``1.1,2.5``  : 1.1以上2.5未満)。
        |   最小値、最大値として ``MIN,MAX`` を使うことができる( ``MIN,2.5``  : 2.5未満)。
    * - | **O=**
        |   任意
        |   デフォルト:null値
      - |   範囲外文字列
        |   ``R=`` パラメータで指定した数値範囲リストのいずれとも合致しない値を
        |   置換するときの文字列(指定がなければNULL値となる)を指定する。
    * - | **F=True|False**
        |   任意
        |   デフォルト:False
      - |   範囲外を項目の値として出力
        |   ``R=`` パラメータで指定した数値範囲リストのいずれとも
        |   合致しない値は、その項目の値のまま出力する。
    * - | **v=**
        |   任意
        |   デフォルト:
      - |   ``R=`` パラメータで指定した数値範囲に対応する置換文字列を指定する。
        |   ``R=`` で指定した値の個数より1つ少い個数でなければならない。
    * - | **A=True|False**
        |   任意
        |   デフォルト:False
      - |   このオプションにより、指定した項目を置き換えるのではなく、新たに項目が追加される。
    * - | **r=True|False**
        |   任意
        |   デフォルト:False
      - |   ``R=`` パラメータの範囲を'〜より大きく〜以下'として扱う。
        |   例えば、 ``1.1_2.5`` は「1.1より大きく2.5以下」として扱う。

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

rsl1.csv
rsl2.csv
rsl3.csv
rsl4.csv
rsl5.csv
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

    >>> nm.mchgnum(f="quantity", R="MIN,10,20,MAX", v="low,middle,high", i="dat1.csv", o="rsl1.csv").run()
    # ## rsl1.csv の内容
    # customer,quantity
    # A,low
    # B,middle
    # C,middle
    # D,low
    # E,high

**パラメータ範囲にイコールをつける例**

``quantity`` 項目の値が最小より多く10以下を ``low`` 、
10より多く20以下を ``middle`` 、20より多く最大以下を ``high`` という文字列に置換する。


  .. code-block:: python
    :linenos:

    >>> nm.mchgnum(f="quantity", R="MIN,10,20,MAX", v="low,middle,high", r=True, i="dat1.csv", o="rsl2.csv").run()
    # ## rsl2.csv の内容
    # customer,quantity
    # A,low
    # B,low
    # C,middle
    # D,low
    # E,high

**数値範囲リストに合致しない値を置換**

``quantity`` 項目の値が10以上20未満を ``low`` 、
20以上30未満を ``middle`` 、30以上最大未満を ``high`` 、
数量が10より小さい値は ``out of range`` という文字列に置換する。


  .. code-block:: python
    :linenos:

    >>> nm.mchgnum(f="quantity", R="10,20,30,MAX", v="low,middle,high", O="out of range", i="dat1.csv", o="rsl3.csv").run()
    # ## rsl3.csv の内容
    # customer,quantity
    # A,out of range
    # B,low
    # C,low
    # D,out of range
    # E,high

**新たな項目の追加**

``quantity`` 項目の値が最小以上10未満を ``low`` 、
10以上20未満を ``middle`` 、20以上最大未満を ``high`` という文字列に置換し
``evaluate`` という項目名で出力する。


  .. code-block:: python
    :linenos:

    >>> nm.mchgnum(f="quantity:evaluate", R="MIN,10,20,MAX", v="low,middle,high", A=True, i="dat1.csv", o="rsl4.csv").run()
    # ## rsl4.csv の内容
    # customer,quantity,evaluate
    # A,5,low
    # B,10,middle
    # C,15,middle
    # D,2,low
    # E,50,high

**範囲外を項目の値として出力**

``quantity`` 項目の値が10以上20未満を ``low`` 、20以上30未満を ``middle`` 、
30以上最大未満を ``high`` 、数量が10より小さい値は置換しないでそのまま出力する。


  .. code-block:: python
    :linenos:

    >>> nm.mchgnum(f="quantity", R="10,20,30,MAX", v="low,middle,high", F=True, i="dat1.csv", o="rsl5.csv").run()
    # ## rsl5.csv の内容
    # customer,quantity
    # A,5
    # B,low
    # C,low
    # D,2
    # E,high



関連メソッド
''''''''''''

- :doc:`mchgstr` 
- :doc:`msed` 
