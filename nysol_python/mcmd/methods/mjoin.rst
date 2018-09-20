mjoin 参照ファイルの項目結合
----------------------------------

``k=`` パラメータで指定した入力データの項目値と参照データの項目値を比較し、
同じ値を持つ ``f=`` パラメータで指定した参照データの項目値を結合する。
参照データのキー項目は単一化されている必要がある。
参照データに同じキー項目の値が複数ある場合は、 :doc:`mnjoin <mnjoin>` を利用すればよい。
また、 ``f=`` を省略すると、参照データのキー項目以外全ての項目を結合する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 必須

  | ここで指定した入力データの項目と ``K=`` パラメータで指定された
  | 参照データの項目が同じ行の項目結合が行われる。
  | NULL値は，参照データの ``K=`` で指定した項目のどの値にもマッチしない値として扱われる。

**f=** : 型=str , 任意(default=全項目)

  | 結合する参照データ上の項目名リストを指定する。
  | 省略するとキー項目を除いた全ての項目が結合される。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。
  | このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)

**K=** : 型=str , 任意(default=k=と同一項目名)

  | 参照データ上の突き合わせる項目名リスト
  | ここで指定した参照データの項目と ``k=`` パラメータで指定された入力データの項目が同じ行の項目結合が行われる。
  | NULL値は，入力データの ``k=`` で指定した項目のどの値にもマッチしない値として扱われる。
  | 参照データ上に ``k=`` パラメータで指定した入力データ上の

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
    '''item,date,price
    A,20081201,100
    A,20081213,98
    B,20081002,400
    B,20081209,450
    C,20081201,100
    ''')

    with open('ref1.csv','w') as f:
      f.write(
    '''item,cost
    A,50
    B,300
    E,200
    ''')


**基本例**

入力ファイルにある ``item`` 項目と、
参照ファイルにある ``item`` 項目を比較し同じ値の場合、 ``cost`` 項目を結合する。

  .. code-block:: python
    :linenos:

    nm.mjoin(k="item", f="cost", m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # item%0,date,price,cost
    # A,20081201,100,50
    # A,20081213,98,50
    # B,20081002,400,300
    # B,20081209,450,300


**未結合データ出力**

入力ファイルにある ``item`` 項目と、
参照ファイルにある ``item`` 項目を比較し同じ値の場合、 ``cost`` 項目を結合する。
その際、参照データにない入力データと参照データにない範囲データをNULL値として出力する。

  .. code-block:: python
    :linenos:

    nm.mjoin(k="item", f="cost", m="ref1.csv", n=True, N=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # item%0,date,price,cost
    # A,20081201,100,50
    # A,20081213,98,50
    # B,20081002,400,300
    # B,20081209,450,300
    # C,20081201,100,
    # E,,,200


関連メソッド
''''''''''''''''''''

* :doc:`mnjoin` : 参照データのキーに重複がある場合は ``mnjoin`` を使う。
* :doc:`mpaste` : 行番号による結合を行う。
* :doc:`mcommon` : 結合でなく単に選択するだけなら ``mcommon`` を使えばよい。

