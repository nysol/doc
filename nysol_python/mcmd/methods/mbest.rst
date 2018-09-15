mbest 指定行の選択
------------------------

指定した行番号の行を選択する。
行番号は0から始まることに注意する(項目名行は除いて、データ本体の先頭行が0行目)。
行番号は ``from=`` と ``to=`` (もしくは ``size=`` )で指定する。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**s=** : 型=str , 条件付き必須( ``q=True`` の指定がない場合)

  | ここで指定した項目(複数項目指定可)で並べ替えられた後、指定した行が選択される。
  | ``q=True`` オプションを指定しないとき、 ``s=`` パラメータは必須。

**from=** : 型=str , 任意(default=0)

  | 選択する開始行番号(0以上の整数)

**to=** : 型=str , 任意(default=0)

  | 選択する終了行番号(0以上の整数)
  | 「 ``from=`` の値」 :math:`\le` 「 ``to=`` の値」でなければならない。

**size=** : 型=str , 任意(default=1)

  | 選択する行数
  | ``to=`` と ``size=`` の両方を同時に指定することはできない。

**R=** : 型=str , 任意(default=)

  | 行番号範囲リスト(複数項目指定可)【必須】*以前のバージョンで使用されていた範囲指定の方法
  | ここで指定した行番号の行が選択される。
  | \_(アンダーバー)で範囲指定できる。
  | 範囲指定の際にはMIN(開始行以降),MAX(最終行まで)を使用できる。
  | ※One Point：事前に目的とする行選択が行いやすいように並べ替えておくとよい。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 指定列の項目(複数項目指定可)が同じ値の行ごとに、 ``from=`` , ``to=`` , ``size=`` で指定した行番号の行を選択する。
  | ``x=True`` , ``nfn=True`` オプション使用時は、項目番号(0〜)で指定可能。

**u=** : 型=str , 任意(default=出力しない)

  | 不一致データ出力データ
  | 指定の条件に一致しない行を出力するデータ。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | ``from=,to=(size=)`` パラメータで指定した行番号以外の行を選択する。



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
    '''customer,quantity,amount
    A,20,5200
    B,18,4000
    C,15,3500
    D,10,2000
    E,3,800
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer,date,amount
    A,20081201,10
    A,20081207,20
    A,20081213,30
    B,20081002,40
    B,20081209,50
    ''')


**基本例**

この例では、 ``quantity`` と ``amount`` 項目値の大きい順（降順）に並べ替えている。
``from=`` , ``to=`` , ``size=`` を指定しなければ先頭行(0行目)のみ選択する

  .. code-block:: python
    :linenos:

    nm.mbest(s="quantity%nr,amount%nr", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,quantity%0nr,amount%1nr
    # A,20,5200


**基本例2**

``customer`` で並べ替えた後、先頭行(0行目)から3行選択する

  .. code-block:: python
    :linenos:

    nm.mbest(s="customer", fr="0", size="3", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer%0,quantity,amount
    # A,20,5200
    # B,18,4000
    # C,15,3500


**基本例3**

並べ替えを行わず(もとのレコード順序を維持したまま)、0行目から1行目まで選択する

  .. code-block:: python
    :linenos:

    nm.mbest(q=True, fr="0", to="1", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer,quantity,amount
    # A,20,5200
    # B,18,4000


**条件反転**

顧客の初回来店日以外の行を選択する。
初回来店日は ``fvd.csv`` というファイルに出力する。

  .. code-block:: python
    :linenos:

    nm.mbest(s="customer,date", k="customer", r=True, u="fvd.csv", i="dat2.csv", o="rsl4.csv").run()
    ### fvd.csv の内容
    # customer,date,amount
    # A,20081201,10
    # B,20081002,40
    ### rsl4.csv の内容
    # customer,date,amount
    # A,20081207,20
    # A,20081213,30
    # B,20081209,50


関連メソッド
''''''''''''''''''''

* :doc:`msel` : ``line()`` 関数を使えば、同じようなことができる。
* :doc:`muniq` : 単純にキー項目を単一化したいだけならこれ。
* :doc:`mselnum` : 数値範囲によって行選択ができる。

