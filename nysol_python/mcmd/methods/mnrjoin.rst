mnrjoin 参照ファイルの複数範囲条件による自然結合
--------------------------------------------------------

範囲により参照データの項目を結合(join)する。
``r=`` パラメータで指定した項目値が、 ``m=`` パラメータで指定した参照データの
``R=`` パラメータで指定した2項目の値の範囲条件(項目1以上項目2未満)に
マッチすれば ``f=`` パラメータの項目を結合する。
マッチする行が複数あれば、それらの行全てが出力され、ちょうど自然結合のような動きをする。
範囲比較される値は、デフォルトで文字列と見なされる。
数値として処理したい場合は ``r=`` パラメータの項目名のあとに\%nをつける。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 任意(default=全項目)

  | 結合する参照データ上の項目名リスト(複数項目指定可)を指定する。
  | 省略するとK=で指定された項目以外の項目を全て結合する。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。
  | このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)

**R=** : 型=str , 必須

  | 範囲項目名リスト(二項目限定)
  | 参照データ上の範囲項目名(start,end)を指定する。
  | 第一項目のNULL値は無限小，第二項目のNULL値は無限大として扱われる。

**rf=** : 型=str , 必須

  | 範囲比較される項目名[\%{n}]
  | 入力データ上の項目名を指定する。
  | 数値として処理したい場合は ``rf=`` パラメータの項目名のあとに\%nをつける。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 入力データ上の突き合わせる項目名リスト(複数項目指定可)
  | ここで指定した入力データの項目と ``K=`` パラメータで指定された参照データの項目が同じ行の項目結合が行われる。

**K=** : 型=str , 任意(default=k=と同一項目名)

  | 参照データ上の突き合わせる項目名リスト(複数項目指定可)
  | ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行の項目結合が行われる。
  | 参照データ上に ``k=`` パラメータで指定した入力データ上の項目と同名の項目が存在する場合は指定する必要はない。

**n=** : 型=bool , 任意(default=False)

  | 参照データにない入力データをNULL値として出力するフラグ。

**N=** : 型=bool , 任意(default=False)

  | 入力データにない参照データをNULL値として出力するフラグ。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullkey=<common_param_assert_nullkey>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
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
    '''date,price
    20080123,10
    20080123,20
    20080203,10
    20080203,35
    200804l0,50
    ''')

    with open('ref1.csv','w') as f:
      f.write(
    '''date,priceF,priceT,avg
    20080203,5,15,150
    20080203,40,50,200
    ''')


**基本例**

日付項目の値が ``20080203`` で、 ``amount`` 項目の値が ``5`` 以上 ``15`` 未満の入力データ行には ``avg=150`` を、
``40`` 以上 ``50`` 未満の行には ``avg=200`` を結合する。

  .. code-block:: python
    :linenos:

    nm.mnrjoin(k="date", f="avg", m="ref1.csv", R="priceF,priceT", rf="price%n", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # date%0,price,avg
    # 20080203,10,150


**未結合データ出力**

``n=True`` を指定することで、参照ファイルにマッチしない入力ファイルの行( ``avg=`` がNULL値の行)も出力し、
``N=True`` を指定することで、入力ファイルにマッチしない参照ファイルの行( ``price=`` がNULL値の行)も出力する。
いわゆる外部結合である。

  .. code-block:: python
    :linenos:

    nm.mnrjoin(k="date", f="avg", m="ref1.csv", R="priceF,priceT", rf="price%n", n=True, N=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # date%0,price,avg
    # 20080123,10,
    # 20080123,20,
    # 20080203,10,150
    # 20080203,35,
    # 20080203,,200
    # 200804l0,50,


関連メソッド
''''''''''''''''''''

* :doc:`mrjoin` : 参照データの結合キー( ``K=`` 項目)に重複がなければ ``mrjoin`` を使う。

