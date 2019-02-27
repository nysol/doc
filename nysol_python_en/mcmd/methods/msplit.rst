msplit 区切り文字による項目分割
--------------------------------------

区切り文字によって項目を分割する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | 区切り文字で分割するデータの項目名を指定する

**a=** : 型=str , 必須

  | 新項目を指定する
  | ここで指定した項目名分分割される。足りない分はNULLとなる

**delim=** : 型=str , 任意(default=)

  | 新しい区切り文字を指定する。デフォルト値は半角スペース。

**r=** : 型=bool , 任意(default=False)

  | ``f=`` で指定した項目を取り除く



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
    '''id,data
    A,1 10 2
    A,2 20 3
    B,1 15 5
    B,3 10 4
    B,1 20 6
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,data
    A,1 10 2
    A,2 20 3
    B,1 15 5
    B,3 4
    B,1
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''id,data
    A,1_10_3
    A,2_20_5
    B,1_15_6
    B,3_10_7
    B,1_20_8
    ''')


**基本例**

半角スペースで分割

  .. code-block:: python
    :linenos:

    nm.msplit(f="data", a="d1,d2,d3", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,data,d1,d2,d3
    # A,1 10 2,1,10,2
    # A,2 20 3,2,20,3
    # B,1 15 5,1,15,5
    # B,3 10 4,3,10,4
    # B,1 20 6,1,20,6


**-r利用**

``r=True`` を指定することで、 ``f=`` で項目を削除できる。

  .. code-block:: python
    :linenos:

    nm.msplit(f="data", a="d1,d2,d3", r=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,d1,d2,d3
    # A,1,10,2
    # A,2,20,3
    # B,1,15,5
    # B,3,10,4
    # B,1,20,6


**分割数不一致**

``a=`` で指定した項目数よりも分割できる項目数が少ない場合は、NULLが追加され、
多い場合、先頭から指定した分割数まで出力する

  .. code-block:: python
    :linenos:

    nm.msplit(f="data", a="d1,d2", i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,data,d1,d2
    # A,1 10 2,1,10
    # A,2 20 3,2,20
    # B,1 15 5,1,15
    # B,3 4,3,4
    # B,1,1,


**delim指定**

``delim=`` を使用して半角スペース以外の文字で分割する

  .. code-block:: python
    :linenos:

    nm.msplit(f="data", a="d1,d2,d3", delim="_", i="dat3.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,data,d1,d2,d3
    # A,1_10_3,1,10,3
    # A,2_20_5,2,20,5
    # B,1_15_6,1,15,6
    # B,3_10_7,3,10,7
    # B,1_20_8,1,20,8


関連メソッド
''''''''''''''''''''



