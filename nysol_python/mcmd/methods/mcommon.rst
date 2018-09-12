mcommon 参照ファイルによる行選択
----------------------------------------

``k=`` パラメータで指定した入力データの項目値と ``m=`` パラメータで指定した参照データの項目値を比較し、同じ値を持つ入力データの行を選択する。

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
   * - | **k=str**
       | 必須
     - | 入力データ上の突き合わせる項目名リスト(複数項目指定可)
       | ここで指定した入力データの項目と ``K=`` パラメータで指定された参照データの項目が同じ行が選択される。
       | 同じ値が複数行連続していてもよい。
   * - | **m=str**
       | 任意
     - | 参照データを指定する。
       | またこのパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)
   * - | **K=str**
       | 任意
     - | 参照データ上の突き合わせる項目名リスト(複数項目指定可)
       | ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行が選択される。
       | 参照データ上に ``k=`` パラメータで指定した入力データ上の項目と同名の項目が存在する場合は指定する必要はない。
       | 同じ値が複数行連続していてもよい。
   * - | **u=str**
       | 任意
     - | 指定の条件に一致しない行を出力するデータ。
   * - | **r=bool**
       | 任意
     - | 条件反転
       | ``k=`` パラメータで指定した入力データの項目値と
       | ``m=`` パラメータで指定した参照データの項目値を比較し、
       | 同じ値を持たない入力データの行を選択する。


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

    nm.mcommon(k="customer", m="ref1.csv", u="oth.csv", i="dat1.csv", o="rsl1.csv").run()
