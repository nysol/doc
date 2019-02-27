mpaste 参照ファイル項目の行番号マッチング結合
----------------------------------------------------

入力データと参照データを行番号でマッチングさせて結合する。
データ件数が異なる場合は、少い方のデータに合わせる。
``n`` や ``N`` オプションを指定することでマッチングできな行もNULL値で結合することが可能である。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 任意(default=)

  | 結合する参照データ上の項目名リスト(複数項目指定可)。
  | 省略するとキー項目を除いた全ての項目が結合される。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。
  | このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)

**n=** : 型=bool , 任意(default=False)

  | 入力データにあって参照データにない場合にNULL値を出力する。

**N=** : 型=bool , 任意(default=False)

  | 参照データにあって入力データにない場合にNULL値を出力する。



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
    '''id1
    1
    2
    3
    4
    ''')

    with open('ref1.csv','w') as f:
      f.write(
    '''id2
    a
    b
    c
    d
    ''')

    with open('ref2.csv','w') as f:
      f.write(
    '''id2
    a
    b
    ''')

    with open('ref3.csv','w') as f:
      f.write(
    '''id2,val
    a,R0
    b,R1
    c,R2
    d,R3
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mpaste(m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id1,id2
    # 1,a
    # 2,b
    # 3,c
    # 4,d


**行数が異なる例**

入力ファイルと参照ファイルで行数が異なる場合は、少いファイルの行数に合わせる。

  .. code-block:: python
    :linenos:

    nm.mpaste(m="ref2.csv", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id1,id2
    # 1,a
    # 2,b


**外部結合**

``n=True`` を指定すると、参照ファイルの行数が少なくても、対応しない入力ファイルの行もNULL値を結合して出力する。

  .. code-block:: python
    :linenos:

    nm.mpaste(m="ref2.csv", n=True, i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id1,id2
    # 1,a
    # 2,b
    # 3,
    # 4,


**結合項目を指定**


  .. code-block:: python
    :linenos:

    nm.mpaste(f="val", m="ref3.csv", i="dat1.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id1,val
    # 1,R0
    # 2,R1
    # 3,R2
    # 4,R3


関連メソッド
''''''''''''''''''''

* :doc:`mjoin` : 行番号でなく、キー項目で結合する。

