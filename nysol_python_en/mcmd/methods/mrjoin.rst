mrjoin 参照ファイルの範囲条件による結合
----------------------------------------------

範囲により参照データの項目を結合(join)する。
``r=`` パラメータで指定した項目値が、参照データ上にある範囲条件(項目値以上、次行の項目値未満)にマッチすれば ``f=`` パラメータで指定した項目値を結合する。
より複雑な範囲条件で結合したければ ``mnrjoin`` を使う。
範囲条件数が少なければ ``mchgnum`` の利用を考えるとよい。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 任意(default=)

  | 結合する参照データ上の項目名リスト(複数項目指定可)。
  | 省略すると ``K=`` で指定された項目以外の項目を全て結合する。

**m=** : 型=str , 任意(default=標準入力)

  | 参照データを指定する。
  | このパラメータが省略された時には標準入力が用いられる。( ``i=`` 指定ありの場合)

**rf=** : 型=str , 必須

  | 範囲比較される項目名
  | 入力データ上の項目名を指定する。
  | ここでここで指定した項目(複数項目指定可)で並べ替えられた後、結合が行われる。
  | %nが指定されると、数値範囲として解釈し、指定がなければ文字列範囲として解釈する。
  | ここで指定する項目にNULL値があってはならない。NULL値があった場合の動作は不定である。

**R=** : 型=str , 任意(default=)

  | 参照データ上の範囲項目名。
  | 省略時は ``r=`` パラメータと同名として扱われる。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 入力データ上の突き合わせる項目名リスト(複数項目指定可)
  | ここで指定した入力データの項目と ``K=`` パラメータで指定された

**K=** : 型=str , 任意(default=k=と同一項目名)

  | 参照データ上の突き合わせる項目名リスト(複数項目指定可)
  | ここで指定した参照データの項目と ``k=`` パラメータで指定された
  | 参照データ上に ``k=`` パラメータで指定した入力データ上の

**n=** : 型=bool , 任意(default=False)

  | 参照データにない入力データをNULL値として出力するフラグ。

**lo=** : 型=bool , 任意(default=False)

  | left open interval
  | ``R=``  パラメータで指定した範囲を左半開区間（より大きい～以下）と解釈する。



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
    '''price
    8
    15
    35
    50
    90
    200
    ''')

    with open('ref1.csv','w') as f:
      f.write(
    '''range,category
    10,low
    35,middle
    80,high
    100,
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''item,price
    A,10
    A,20
    B,10
    B,20
    ''')

    with open('ref2.csv','w') as f:
      f.write(
    '''item,price,category
    A,10,low
    A,15,high
    A,100,
    B,10,low
    B,35,high
    B,100,
    ''')


**基本例**

``price`` を範囲で
分類項目 ``low、middle、high`` を結合する。

  .. code-block:: python
    :linenos:

    nm.mrjoin(rf="price%n", m="ref1.csv", R="range", f="category", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # price%0n,category
    # 15,low
    # 35,middle
    # 50,middle
    # 90,high


**基本例2**


  .. code-block:: python
    :linenos:

    nm.mrjoin(lo=True, rf="price%n", m="ref1.csv", R="range", f="category", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # price%0n,category
    # 15,low
    # 35,low
    # 50,middle
    # 90,high


**基本例3**


  .. code-block:: python
    :linenos:

    nm.mrjoin(n=True, rf="price%n", m="ref1.csv", R="range", f="category", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # price%0n,category
    # 8,
    # 15,low
    # 35,middle
    # 50,middle
    # 90,high
    # 200,


**商品別に異なる範囲を設定して結合**


  .. code-block:: python
    :linenos:

    nm.mrjoin(k="item", rf="price%n", m="ref2.csv", f="category", i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # item%0,price%1n,category
    # A,10,low
    # A,20,high
    # B,10,low
    # B,20,low


関連メソッド
''''''''''''''''''''

* :doc:`mchgnum` : 数値範囲を指定して値を置換/追加する。
* :doc:`mjoin` : 数値範囲ではなく文字列一致による結合の場合はこのコマンドを使う。
* :doc:`mnrcommon` : 結合ではなく選択する場合はこのコマンドを使う。

