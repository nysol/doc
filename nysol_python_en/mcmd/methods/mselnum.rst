mselnum 数値範囲による行選択
------------------------------------

``f=`` で指定した項目の値が、
``c=`` で指定した数値範囲にマッチする行を選択する。
以下に示すように多様な選択条件を指定することが可能である。
このコマンドで指定できないより複雑な条件(文字列マッチとの組み合せなど)
を設定するのであれば :doc:`msel` コマンドを利用すればよい。
OR条件、AND条件およびキー指定についての詳細は ``mselstr`` コマンドを参照されたい。

 *  開区間、閉区間、半開区間、無限区間の制定が可能である。
 *   ``c=`` に複数の範囲を指定すれば、いずれかの範囲にマッチすれば選択される(OR条件)。
 *   ``f`` =に複数項目を指定すれば、いずれかの項目の値がマッチすれば選択される(OR条件)。
 *   ``f=`` のOR条件をAND条件に変更することも可能( ``F`` オプション)。
 *   ``k=`` を指定することでキー単位で選択することが可能。
 *  キー単位選択の場合、複数レコードのAND条件を指定可能( ``R`` オプション)。

典型的な例を :numref:`mselnum_input` 〜 :numref:`mselnum_out3` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mselnum_input

  key,val
  a,1
  a,-3
  b,3
  b,6




.. csv-table:: val項目が1以上3以下の行を選択
  :header-rows: 1
  :name: mselnum_out1

  key,val
  a,1
  b,3




.. csv-table:: val項目が1以上3未満の行を選択
  :header-rows: 1
  :name: mselnum_out2

  key,val
  a,1




.. csv-table:: 5以上の行を選択
  :header-rows: 1
  :name: mselnum_out3

  key,val
  b,6




.. csv-table:: 1以下もしくは5以上の行を選択
  :header-rows: 1
  :name: mselnum_out4

  key,val
  a,1
  a,-3
  b,6




パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**f=** : 型=str , 必須

  | 検索対象となる項目名リスト(複数項目指定可)を指定する。

**c=** : 型=str , 必須

  | ``f=`` パラメータで指定した項目の値が、ここで指定した文字列リスト(複数範囲指定可)の1つにマッチすれば選択される。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 撰択する単位となるキー項目(複数項目指定可)を指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 指定の条件に一致する行を出力するデータを指定する。

**u=** : 型=str , 任意(default=出力しない)

  | 指定の条件に一致しない行を出力するデータを指定する。

**F=** : 型=bool , 任意(default=False)

  | ``f=`` パラメータで複数項目を指定した場合、その全ての値がマッチする行を撰択する。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | 選択ではなく削除する。

**R=** : 型=bool , 任意(default=False)

  | ``k=`` パラメータを指定した場合、その全ての行がマッチすれば行を撰択する。

**bufcount=** : 型=str , 任意(default=)

  | バッファのサイズ数を指定する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`bufcount=<common_param_bufcount>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullkey=<common_param_assert_nullkey>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
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
    '''id,val
    1,5.1
    2,5
    3,-2.0
    4,
    5,2.0
    ''')


**基本例**

``val`` 項目が2以上5以下の行、すなわち ``id=2,5`` の行を選択する。

  .. code-block:: python
    :linenos:

    nm.mselnum(f="val", c="[2,5]", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val
    # 2,5
    # 5,2.0


**片側範囲**

``val`` 項目が2以上の行、すなわち ``id=1,2,5`` の行を選択する。

  .. code-block:: python
    :linenos:

    nm.mselnum(f="val", c="[2,]", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,val
    # 1,5.1
    # 2,5
    # 5,2.0


関連メソッド
''''''''''''''''''''



