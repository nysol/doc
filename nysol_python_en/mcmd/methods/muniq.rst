muniq レコードの単一化
----------------------------

値が重複した行を単一化する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 行を単一化する単位となる項目名リストを指定する。



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
    '''date,customer
    20081201,A
    20081202,A
    20081202,B
    20081202,B
    20081203,C
    ''')


**基本例**

``date`` 項目を単位に重複行を削除し単一にする。

  .. code-block:: python
    :linenos:

    nm.muniq(k="date", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # date%0,customer
    # 20081201,A
    # 20081202,B
    # 20081203,C


**複数の項目での重複行の削除**

``date`` と ``customer`` 項目を単位に重複行を削除し単一にする。

  .. code-block:: python
    :linenos:

    nm.muniq(k="date,customer", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # date%0,customer%1
    # 20081201,A
    # 20081202,A
    # 20081202,B
    # 20081203,C


関連メソッド
''''''''''''''''''''

* :doc:`mbest` : 同一キーの中で何番目の行を選択するかを指定したい場合は ``mbest`` コマンドを使う。

