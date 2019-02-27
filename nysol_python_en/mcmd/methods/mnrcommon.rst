mnrcommon 参照ファイルの複数範囲条件による行撰択
----------------------------------------------------------

参照データの範囲条件にマッチする入力データの行を選択する。
``k=`` パラメータで指定した入力データの項目値と ``K=`` パラメータで指定した参照データの項目値が同じ行について、
``r=`` でパラメータで指定した項目値が ``R=`` パラメータで指定した2項目の値の範囲条件(項目1以上項目2未満)にマッチすれば選択する。
数値として処理したい場合は ``r=`` パラメータの項目名のあとに ``%n`` をつけること。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 入力データ上の突き合わせる項目名リスト(複数項目指定可)を指定する。
  | ここで指定した入力データの項目と ``K=`` パラメータで指定された参照データの項目が同じ行の項目結合が行われる。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。
  | このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)

**R=** : 型=str , 必須

  | 参照データ上の範囲項目名(start,end)を指定する。
  | 第一項目のNULL値は無限小，第二項目のNULL値は無限大として扱われる。

**fr=** : 型=str , 必須

  | 範囲比較される入力データ上の項目名を指定する。
  | ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行が選択される。
  | 数値として処理したい場合は ``r=`` パラメータの項目名のあとに\%nをつける。

**K=** : 型=str , 任意(default=k=と同一項目名)

  | 参照データ上の突き合わせる項目名リスト(複数項目指定可)
  | ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行の項目結合が行われる。
  | 参照データ上に ``k=`` パラメータで指定した入力データ上の項目と同名の項目が存在する場合は指定する必要はない。

**u=** : 型=str , 任意(default=出力しない)

  | 指定の条件に一致しない行を出力するデータ。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | ``R=`` パラメータで指定した行番号以外の行を選択する。



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
    '''date,amount
    20080123,10
    20080203,10
    20080203,20
    20080203,45
    200804l0,50
    ''')

    with open('ref1.csv','w') as f:
      f.write(
    '''date,amountF,amountT
    20080203,5,15
    20080203,40,50
    ''')


**基本例**

日付項目の値が ``20080203`` で、 ``amount`` 項目の値が ``5`` 以上 ``15`` 未満の行、および ``40`` 以上 ``50`` 未満の行を選択する。

  .. code-block:: python
    :linenos:

    nm.mnrcommon(k="date", m="ref1.csv", R="amountF,amountT", rf="amount%n", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # date%0,amount
    # 20080203,10
    # 20080203,45


**条件反転**

``r=True`` を付けると選択条件は反転する。

  .. code-block:: python
    :linenos:

    nm.mnrcommon(k="date", m="ref1.csv", R="amountF,amountT", rf="amount%n", r=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # date%0,amount
    # 20080123,10
    # 20080203,20
    # 200804l0,50


関連メソッド
''''''''''''''''''''

* :doc:`mcommon` : 範囲でなく文字列マッチで選択したい場合はこのコマンドを使う。
* :doc:`mnrjoin` : 選択ではなく参照データの項目を結合する。

