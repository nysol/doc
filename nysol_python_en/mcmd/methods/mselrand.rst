mselrand ランダムに行を選択
------------------------------------

``c=`` パラメータもしくは ``p=`` パラメータで指定した行数をランダムに選択する(非復元抽出)。
``k=`` を指定した場合、同一キーの行から指定の行数をランダムに選択し、
また同時に ``B`` オプションを指定すると、キー単位で選択する。
乱数の生成にはメルセンヌ・ツイスター法を利用している

* 原作者のページ: http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html
* boostライブラリ: http://www.boost.org/doc/libs/1_54_0/doc/html/boost_random.html


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**c=** : 型=str , 任意(default=)

  | 各キーの値毎に選択する行数を指定する。
  | ``p=`` パラメータを指定しない場合の指定は必ず指定する必要がある。

**p=** : 型=str , 任意(default=)

  | 各キーの値毎に選択する割合をパーセントで指定する。
  | ``c=`` パラメータを指定しない場合の指定は必ず指定する必要がある。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 指定する項目（複数項目指定可）の値が同じ行から、一定行数ランダムに選択する。

**S=** : 型=str , 任意(default=)

  | 同じ乱数の種は同じシーケンスの乱数をふる。
  | 指定しない場合は、時刻に応じた異なる乱数の種が利用される。
  | 指定可能な乱数の種(-2147483648〜2147483647)

**u=** : 型=str , 任意(default=出力しない)

  | 指定の条件に一致しない行を出力するデータを指定する。

**B=** : 型=bool , 任意(default=False)

  | キー単位選択



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
    '''customer,date,amount
    A,20081201,10
    A,20081207,20
    A,20081213,30
    B,20081002,40
    B,20081209,50
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer,date,amount
    A,20081201,10
    A,20081207,20
    A,20081213,30
    B,20081002,40
    B,20081209,50
    C,20081210,60
    D,20081201,70
    D,20081205,80
    D,20081209,90
    ''')


**基本例**

一人の顧客につきランダムに1行を選択する。

  .. code-block:: python
    :linenos:

    nm.mselrand(k="customer", c="1", S="1", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,date,amount
    # A,20081201,10
    # B,20081002,40


**ランダムに一定割合の行を選択**

一人の顧客につきランダムに50\%の行を選択する。
また、それ以外の不一致データは ``oth2.csvと`` いうファイルに出力する。

  .. code-block:: python
    :linenos:

    nm.mselrand(k="customer", p="50", S="1", u="oth2.csv", i="dat1.csv", o="rsl2.csv").run()
    ### oth2.csv の内容
    # customer%0,date,amount
    # A,20081207,20
    # A,20081213,30
    # B,20081209,50
    ### rsl2.csv の内容
    # customer%0,date,amount
    # A,20081201,10
    # B,20081002,40


**キー単位の選択**

以下の例は、顧客 ``A,B,C,D`` の4人からランダムに2人を選ぶ。
顧客 ``D`` が選ばれると、顧客 ``D`` の行は全て出力される。

  .. code-block:: python
    :linenos:

    nm.mselrand(k="customer", c="2", S="1", B=True, i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer%0,date,amount
    # C,20081210,60
    # D,20081201,70
    # D,20081205,80
    # D,20081209,90


関連メソッド
''''''''''''''''''''

* :doc:`msel` : 正規乱数も使える。
* :doc:`mrand` : ランダム選択でなく、乱数項目を付け加える。

