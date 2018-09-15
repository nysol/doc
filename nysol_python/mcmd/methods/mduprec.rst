mduprec レコードの複写
------------------------------

各レコードを複写する。
複写する行数は ``n=`` で固定値を与えるか、
もしくは ``f=`` で指定した項目の値により与える。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 任意(default=)

  | 複写行数をもつ項目名
  | ここで指定した項目の値の数分、その行を複写する。

**n=** : 型=str , 任意(default=)

  | 複写行数の指定
  | ここで指定した値の数分、行を複写する。



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
    '''store,val
    A,2
    B,
    C,5
    ''')


**基本例**

``quantity`` 項目の値の数分、データを複写し複数行のデータを生成する。
対象項目がNULL値の場合は複写しない。

  .. code-block:: python
    :linenos:

    nm.mduprec(f="val", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # store,val
    # A,2
    # A,2
    # C,5
    # C,5
    # C,5
    # C,5
    # C,5


**複写行数の指定**

データを2行づつ複写した( ``n=2`` )データを生成する。

  .. code-block:: python
    :linenos:

    nm.mduprec(n="2", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # store,val
    # A,2
    # A,2
    # B,
    # B,
    # C,5
    # C,5


関連メソッド
''''''''''''''''''''

* :doc:`mcount` : ``mduprec`` と逆の動きをする。
* :doc:`mwindow` : 一定数のレコードをずらしながら複写する。

