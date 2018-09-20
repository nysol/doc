mrand 擬似乱数
--------------------

0.0から1.0の範囲の実数の擬似乱数、もしくは範囲指定による整数の擬似乱数を生成し、 ``a=`` パラメータで指定した項目名で出力する。
乱数の生成にはメルセンヌ・ツイスター法を利用している
(\href{http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html}{原作者のページ}
, \href{http://www.boost.org/doc/libs/1_54_0/doc/html/boost_random.html}{boostライブラリ})。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 指定したキー項目について、同じキー値には同じ乱数値が振られる。

**a=** : 型=str , 必須

  | 新たに追加される項目の名前を指定する。【但し、-nfn,-nfnoオプション指定時は必要なし】

**max=** : 型=str , 任意(default=INT\_MAX)

  | 乱数の最大値
  | 0〜 :math:`2^{32}` (約21億)の範囲の整数が指定可能
  | このパラメータを指定するときは ``int`` オプションも指定しなければならない。

**min=** : 型=str , 任意(default=0)

  | 整数乱数の最小値
  | 0〜 :math:`2^{32}` (約21億)の範囲の整数が指定可能
  | このパラメータを指定するときは ``int`` オプションも指定しなければならない。

**S=** : 型=str , 任意(default=現在時刻)

  | 乱数の種
  | 同じ乱数の種を指定すれば、同じ乱数系列となる。
  | ``S=`` を指定しなければ、時刻(ミリ(1/1000秒単位)に応じた異なる乱数の種が利用される。
  | 指定可能な乱数の種(-2147483648〜2147483647)

**int=** : 型=bool , 任意(default=False)

  | 整数乱数を生成



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
    '''customer
    A
    B
    C
    D
    E
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer
    A
    A
    A
    B
    B
    C
    D
    D
    D
    ''')


**基本例**

0.0から1.0の範囲の実数乱数を生成する。

  .. code-block:: python
    :linenos:

    nm.mrand(a="rand", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,rand
    # A,0.2326046587
    # B,0.8796894355
    # C,0.4733951823
    # D,0.1713104991
    # E,0.9858783041


**基本例2**

-intで整数乱数

  .. code-block:: python
    :linenos:

    nm.mrand(a="rand", int=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer,rand
    # A,1960666384
    # B,1548479388
    # C,303832552
    # D,221426400
    # E,1692666423


**最小値、最大値を決めた乱数の生成**

最小値が10、最大値が100の整数の乱数を生成し、 ``rand`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mrand(a="rand", int=True, min="10", max="100", S="1", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer,rand
    # A,47
    # B,100
    # C,75
    # D,94
    # E,10


**キー単位の乱数生成**

以下の例は、顧客 ``A,B,C,D`` の4人について同じ顧客には同じ乱数値を振る。

  .. code-block:: python
    :linenos:

    nm.mrand(k="customer", int=True, min="0", max="1", a="rand", i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # customer%0,rand
    # A,0
    # A,0
    # A,0
    # B,1
    # B,1
    # C,1
    # D,0
    # D,0
    # D,0


関連メソッド
''''''''''''''''''''

* :doc:`mselrand` : ランダムに行を選択する。
* :doc:`mnewrand` : 入力データなしに、乱数データを新たに生成する。

