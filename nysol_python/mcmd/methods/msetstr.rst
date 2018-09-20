msetstr 文字列項目の追加
--------------------------------

指定した文字列を項目として全行に追加する。複数項目の追加も可能。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**v=** : 型=str , 必須

  | 追加する文字列リスト。
  | 値を何も指定しないとNULL値が追加される。

**a=** : 型=str , 必須

  | 追加する項目名。
  | ``v=`` で指定した文字列の個数と同数の項目名を指定しなければならない。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
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
    '''customer,date
    A,20081202
    A,20081204
    B,20081203
    ''')


**基本例**

日付計算で必要となる基準日を(2007年01月01日と定義した場合)すべての行に「 ``20070101`` 」という文字列を追加し「基準日」という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.msetstr(v="20070101", a="基準日", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,date,基準日
    # A,20081202,20070101
    # A,20081204,20070101
    # B,20081203,20070101


**複数項目を追加**


  .. code-block:: python
    :linenos:

    nm.msetstr(v="20070101,20070201", a="基準日1,基準日2", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer,date,基準日1,基準日2
    # A,20081202,20070101,20070201
    # A,20081204,20070101,20070201
    # B,20081203,20070101,20070201


**null値項目追加**


  .. code-block:: python
    :linenos:

    nm.msetstr(v="", a="追加項目", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer,date,追加項目
    # A,20081202,
    # A,20081204,
    # B,20081203,


関連メソッド
''''''''''''''''''''

* :doc:`mcal` : ``if`` 関数を使えば、行ごとに条件を判定して異なる固定文字列を追加できる。

