mcommon 参照ファイルによる行選択
------------------------------------------------------------

``k=`` パラメータで指定した入力データの項目値と ``m=`` パラメータで指定した参照データの項目値を比較し、同じ値を持つ入力データの行を選択する。

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
      - |   入力データ上の突き合わせる項目名リスト(複数項目指定可)
        |   ここで指定した入力データの項目と ``K=`` パラメータで指定された参照データの項目が同じ行が選択される。
        |   同じ値が複数行連続していてもよい。
    * - | **m=**
        |   任意
        |   デフォルト:標準入力
      - |   参照データを指定する。
        |   またこのパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)
    * - | **K=**
        |   任意
        |   デフォルト:k=と同一項目名
      - |   参照データ上の突き合わせる項目名リスト(複数項目指定可)
        |   ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行が選択される。
        |   参照データ上に ``k=`` パラメータで指定した入力データ上の項目と同名の項目が存在する場合は指定する必要はない。
        |   同じ値が複数行連続していてもよい。
    * - | **u=**
        |   任意
        |   デフォルト:出力しない
      - |   指定の条件に一致しない行を出力するデータ。
    * - | **r=True|False**
        |   任意
        |   デフォルト:False
      - |   条件反転
        |   ``k=`` パラメータで指定した入力データの項目値と
        |   ``m=`` パラメータで指定した参照データの項目値を比較し、
        |   同じ値を持たない入力データの行を選択する。

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
    '''customer,quantity
    A,1
    B,2
    C,1
    D,3
    E,1
    ''')
            
    with open('ref1.csv','w') as f:
      f.write(
    '''customer,gender
    A,female
    B,male
    E,female
    ''')
            
    with open('ref2.csv','w') as f:
      f.write(
    '''customerID,gender
    A,female
    B,male
    E,female
    ''')
            
    with open('dat3.csv','w') as f:
      f.write(
    '''customer,quantity
    A,1
    A,2
    A,3
    B,1
    D,1
    D,2
    ''')
            
    with open('ref3.csv','w') as f:
      f.write(
    '''customer
    A
    A
    D
    ''')
    
**基本例**

入力ファイルにある ``customer`` 項目と、参照ファイルにある ``customer`` 項目が同じ値を持つ入力ファイルの行を選択する。
それ以外のデータは ``oth.csv`` に出力する。


  .. code-block:: python
    :linenos:

    >>> nm.mcommon(k="customer", m="ref1.csv", u="oth.csv", i="dat1.csv", o="rsl1.csv").run()
    # ## oth.csv の内容
    # customer%0,quantity
    # C,1
    # D,3
    # ## rsl1.csv の内容
    # customer%0,quantity
    # A,1
    # B,2
    # E,1

**同じ値を持たない入力ファイルの行選択**

``r=True`` オプションを付けることで、条件が逆転し、参照ファイルにない ``customer`` を選択することになる。


  .. code-block:: python
    :linenos:

    >>> nm.mcommon(k="customer", m="ref1.csv", r=True, i="dat1.csv", o="rsl2.csv").run()
    # ## rsl2.csv の内容
    # customer%0,quantity
    # C,1
    # D,3

**結合キー項目名が異なる場合**

結合キーの項目名が異なる場合は、 ``K=`` で指定する。


  .. code-block:: python
    :linenos:

    >>> nm.mcommon(k="customer", K="customerID", i="dat1.csv", m="ref2.csv", o="rsl3.csv").run()
    # ## rsl3.csv の内容
    # customer%0,quantity
    # A,1
    # B,2
    # E,1

**キー項目に重複行がある場合の例**

参照ファイルと入力ファイルのキー項目に重複行があっても選択可能。


  .. code-block:: python
    :linenos:

    >>> nm.mcommon(k="customer", m="ref3.csv", r=True, i="dat3.csv", o="rsl4.csv").run()
    # ## rsl4.csv の内容
    # customer%0,quantity
    # B,1



関連メソッド
''''''''''''

- :doc:`mselstr` 
- :doc:`mnrcommon` 
- :doc:`mjoin` 
