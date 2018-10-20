mnumber 連番
--------------------

数字連番もしくはアルファベット連番(A,B,...,Z,AA,AB,...,AZ,BA,BB,...,ZZ,AAA,AAB,...)ををふり、 ``a=`` パラメータで指定した項目名で出力する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**a=** : 型=str , 必須

  | 新たに追加される項目の名前を指定する。【但し、-nfn,-nfnoオプション指定時は必要なし】

**e=** : 型=str , 任意(default=)

  | 同Rankの処理方法
  | 同一キー同一ソート項目値への処理方法を指定する。
  | 指定しない場合は、デフォルトは ``e=seq`` である。
  | ``seq:`` 同Rankの場合は各行に連番を振るが、その順序は不定である。
  | ``same:`` 同Rankの場合は同じNoもしくはアルファベットを付け加える。
  | ``skip:`` 同Rankの場合は同じNoを振り、
  | 次のNoはスキップするようにNoもしくはアルファベット連番を付け加える。
  | (注意) ``e={same/skip}`` を指定する場合は、 ``s=`` パラメータを同時に指定しなければならない。

**I=** : 型=str , 任意(default=)

  | 連番の間隔を指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 連番もしくは連文字をふる単位となる項目名リスト(複数項目指定可)を指定する。【 :ref:`集計キーブレイク処理<autoadd_keybreak>` 】
  | (注意）指定する場合は事前に ``k=`` パラメータで指定する連番、
  | もしくは連文字をふる単位となる項目順に並べ替えておく必要がある。

**s=** : 型=str , 任意(default=)

  | ここで指定した項目(複数項目指定可)で並べ替えられた後、連番が追加される。
  | ``B`` オプション指定時以外は必須。

**S=** : 型=str , 任意(default=)

  | 開始No
  | 連番の開始Noを指定する。
  | 大文字のアルファベットが指定された場合はアルファベット連番となる。
  | ただし、アルファベット連番の場合、間隔( ``I=`` )に負の値は指定できない。

**B=** : 型=bool , 任意(default=False)

  | キー毎に連番もしくはアルファベット連番をふる。
  | あるキー内では全行同じNoもしくはアルファベットがふられる。



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
    '''Customer,Val,Sum
    A,29,300
    B,35,250
    C,15,200
    D,23,150
    E,10,100
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''Date
    20090101
    20090101
    20090102
    20090103
    20090103
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''Customer,Val,Sum
    A,3,300
    B,1,250
    C,2,250
    D,1,150
    E,1,100
    ''')

    with open('dat4.csv','w') as f:
      f.write(
    '''Customer,Val,Sum
    A,1,100
    B,1,150
    C,1,250
    D,2,250
    E,3,300
    ''')


**数字の連番**

Customer項目名順（昇順）に連番を振り「No」という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mnumber(s="Customer", a="No", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # Customer%0,Val,Sum,No
    # A,29,300,0
    # B,35,250,1
    # C,15,200,2
    # D,23,150,3
    # E,10,100,4


**Date項目順の連番**

Date項目順（昇順）に連番をふる。その際、同じDateには同じNoを振り「No」という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mnumber(k="Date", a="No", B=True, i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # Date%0,No
    # 20090101,0
    # 20090101,0
    # 20090102,1
    # 20090103,2
    # 20090103,2


**Sum項目順の連番(同Rankは同じアルファベットをふる)**

Sum項目の多い順（降順）にアルファベットのAから順に連文字を振り「Rank」という項目名で出力する。
また、同Rankの場合は同じアルファベット文字を振ることにする。

  .. code-block:: python
    :linenos:

    nm.mnumber(a="Rank", e="same", s="Sum%nr", S="A", i="dat3.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # Customer,Val,Sum%0nr,Rank
    # A,3,300,A
    # B,1,250,B
    # C,2,250,B
    # D,1,150,C
    # E,1,100,D


**Sum項目順の連番(同Rankは並び順でNoをふる)**

Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は並び順でNoを振ることにする。

  .. code-block:: python
    :linenos:

    nm.mnumber(a="Rank", e="seq", s="Sum%nr", i="dat3.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # Customer,Val,Sum%0nr,Rank
    # A,3,300,0
    # B,1,250,1
    # C,2,250,2
    # D,1,150,3
    # E,1,100,4


**Sum項目順の連番(同Rankは同じNoをふる)**

Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は同じNoを振ることにする。

  .. code-block:: python
    :linenos:

    nm.mnumber(a="Rank", e="same", s="Sum%nr", i="dat3.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # Customer,Val,Sum%0nr,Rank
    # A,3,300,0
    # B,1,250,1
    # C,2,250,1
    # D,1,150,2
    # E,1,100,3


**Sum項目順の連番(同Rankの場合は同じRankNoを振り、次のNoはスキップ)**

Sum項目の多い順（降順）に連番を振り「Rank」という項目名で出力する。
その際、同Rankの場合は同じRankNoを振り、次のNoはスキップするようにNoを振ることにする。

  .. code-block:: python
    :linenos:

    nm.mnumber(a="Rank", e="skip", s="Sum%nr", i="dat3.csv", o="rsl6.csv").run()
    ### rsl6.csv の内容
    # Customer,Val,Sum%0nr,Rank
    # A,3,300,0
    # B,1,250,1
    # C,2,250,1
    # D,1,150,3
    # E,1,100,4


**10から始まる連番**

Sum項目の小さい順（昇順）に10から始まる連番を振り「Score」という項目名で出力する。
その際、同Rankの場合は同じRankNoを振り、次のNoはスキップするようにNoを振ることにする。

  .. code-block:: python
    :linenos:

    nm.mnumber(a="Score", e="same", s="Sum%n", S="10", i="dat4.csv", o="rsl7.csv").run()
    ### rsl7.csv の内容
    # Customer,Val,Sum%0n,Score
    # A,1,100,10
    # B,1,150,11
    # C,1,250,12
    # D,2,250,12
    # E,3,300,13


**10から始まる5つ飛びの連番**

Sum項目の小さい順番（昇順）に10から始まる5つ飛びの連番を振り「Score」という項目名で出力する。
また、同Rankの場合は同じNoを振ることにする。

  .. code-block:: python
    :linenos:

    nm.mnumber(a="Score", e="same", s="Sum%n", S="10", I="5", i="dat4.csv", o="rsl8.csv").run()
    ### rsl8.csv の内容
    # Customer,Val,Sum%0n,Score
    # A,1,100,10
    # B,1,150,15
    # C,1,250,20
    # D,2,250,20
    # E,3,300,25


関連メソッド
''''''''''''''''''''

* :doc:`mnewnumber` : 新たに連番データを生成する場合に使う。
* :doc:`mbest` : 行番号による選択であれば、 ``mnumber`` を使わずともこのコマンドで。

