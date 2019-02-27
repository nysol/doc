mnjoin 参照ファイル項目の自然結合
----------------------------------------

``k=`` パラメータで指定した入力データの項目値と参照データの項目値を比較し、
同じ値の場合 ``m=`` パラメータで指定した参照データにある
``f=`` パラメータで指定した項目値を自然結合する。
``mjoin`` コマンドとの違いは、参照データ上のキー項目に重複があってもよい点である。
あるキー値について、入力データ上に :math:`n` 件、参照データ上に :math:`m` 件のレコードがあった場合、
:math:`n	imes m` 件のレコードが出力されることになる。
また、 ``f=`` を省略すると、参照データのキー項目以外全ての項目を結合する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 必須

  | 入力データ上の突き合わせる項目名リストを指定する。
  | ここで指定した入力データの項目と ``K=`` パラメータで指定された
  | 参照データの項目が同じ行の項目結合が行われる。

**f=** : 型=str , 任意(default=全項目)

  | 結合する参照データ上の項目名リストを指定する。
  | 省略するとキー項目を除いた全ての項目が結合される。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。
  | このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)

**K=** : 型=str , 任意(default=k=と同一項目名)

  | 参照データ上の突き合わせる項目名リスト
  | ここで指定した参照データの項目と ``k=`` パラメータで指定された
  | 参照データ上に ``k=`` パラメータで指定した入力データ上の

**bufcount=** : 型=str , 任意(default=)

  | バッファのサイズ数を指定する。

**n=** : 型=bool , 任意(default=False)

  | 参照データにない入力データをNULL値として出力するフラグ。

**N=** : 型=bool , 任意(default=False)

  | 入力データにない参照データをNULL値として出力するフラグ。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`bufcount=<common_param_bufcount>`
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
    A,70
    B,300
    E,200
    ''')

    with open('ref2.csv','w') as f:
      f.write(
    '''item,cost
    A,50
    B,300
    E,200
    ''')


**基本例**

入力ファイルにある ``item`` 項目と、
参照ファイルにある ``item`` 項目を比較し同じ値の場合、 ``cost`` 項目を結合する。
入力ファイル、参照ファイル共に ``item=A`` が2行あり、結果、出力ファイルには2$	imes$2=4行の ``item=A`` が出力されている。

  .. code-block:: python
    :linenos:

    nm.mnjoin(k="item", f="cost", m="ref1.csv", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # item%0,date,price,cost
    # A,20081201,100,50
    # A,20081201,100,70
    # A,20081213,98,50
    # A,20081213,98,70
    # B,20081002,400,300
    # B,20081209,450,300


**未結合データ出力**

``n=True`` を指定することで、参照ファイルにマッチしない入力ファイルの行( ``item="C"`` の行)も出力し、
``N=True`` を指定することで、入力ファイルにマッチしない参照ファイルの行( ``item="E"`` の行)も出力する。

  .. code-block:: python
    :linenos:

    nm.mnjoin(k="item", f="cost", m="ref2.csv", n=True, N=True, i="dat1.csv", o="rsl2.csv").run()
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

* :doc:`mjoin` : 参照データのキーが単一化されているのであれば ``mjoin`` を使うと若干高速。
* :doc:`mproduct` : 結合キー関係なく全行の組み合せで結合する。1行だけからなる参照データを入力データ全行に結合する目的で利用することが多い。

