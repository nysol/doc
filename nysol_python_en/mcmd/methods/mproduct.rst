mproduct 参照ファイルの直積結合
----------------------------------------

入力データ1行に対して、 ``m=`` パラメータで指定した参照データの
``f=`` パラメータで指定した項目全行を結合する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 任意(default=全項目)

  | 結合する参照データ上の項目名リスト(複数項目指定可)。
  | 省略するとキー項目を除いた全ての項目が結合される。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。
  | このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)

**bufcount=** : 型=str , 任意(default=)

  | バッファのサイズ数を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`bufcount=<common_param_bufcount>`
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
    '''customer
    A
    B
    ''')

    with open('ref1.csv','w') as f:
      f.write(
    '''date
    20090101
    20090201
    20090301
    ''')


**基本例**

入力ファイルにある ``customer`` 項目に対して、
参照ファイルにある ``date`` 項目全行を結合する。

  .. code-block:: python
    :linenos:

    nm.mproduct(f="date", m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,date
    # A,20090101
    # A,20090201
    # A,20090301
    # B,20090101
    # B,20090201
    # B,20090301


関連メソッド
''''''''''''''''''''

* :doc:`mnjoin` : 結合キーを指定しての ``mproduct`` のような結合を行う。

