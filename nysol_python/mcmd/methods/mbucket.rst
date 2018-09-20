mbucket 件数均等化バケット分割
--------------------------------------

``f=`` で指定した数値項目を ``n=`` で指定した数の区間に分割する。
区間の計算には2通りの方法があり、一つは、
各区間に属する件数ができるだけ均等になるような区間を計算する
(件数均等化バケット分割と呼ぶ)。
他方は、区間の範囲が均等になるような区間を計算する
(範囲均等化バケット分割と呼ぶ)。
``rng`` オプションを指定すると範囲均等分割となり、指定しなければ件数均等分割となる。
``f=`` に複数の項目を指定した場合は、それぞれの項目ごとにバケット分割を実行する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | ここで指定した項目(複数項目指定可)の値に基づいて分割をおこなう。
  | 分割対象の項目名:出力する項目名

**n=** : 型=str , 必須

  | 分割数
  | ``f=`` で指定した項目それぞれの分割数をカンマで区切って指定する。
  | ただし1つの数字を指定した場合は全ての項目の分割数として扱われる。

**F=** : 型=str , 任意(default=0)

  | 出力形式
  | バケットの名前を出力形式。
  | 0:バケット番号のみを表示する。
  | 1:バケットの範囲のみを表示する。
  | 2:バケット番号とバケット範囲の両方を表示する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | バケット分割を行う単位となる項目(複数項目指定可)名リスト。

**O=** : 型=str , 任意(default=)

  | バケット範囲出力データ
  | ``f=`` パラメータで指定した各項目の各バケットの数値範囲を出力するデータ。

**rng=** : 型=bool , 任意(default=False)

  | バケットの範囲均等指定
  | バケットの範囲が均等になるように分割する。

**r=** : 型=bool , 任意(default=False)

  | バケットの番号を逆順に出力する。

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
    '''id,x,y
    A,2,7
    B,6,7
    C,5,6
    D,7,5
    E,6,4
    F,1,3
    G,3,3
    H,4,2
    I,7,2
    J,2,1
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,x,y
    A,2,7
    A,6,7
    A,5,6
    B,7,5
    B,6,4
    B,1,3
    C,3,3
    C,4,2
    C,7,2
    C,2,1
    ''')


**基本例**

``x,y`` 項目それぞれで、件数ができるだけ均等になるように2分割する。
その際、各バケットの数値範囲を ``rng1.csv`` に出力する。

  .. code-block:: python
    :linenos:

    nm.mbucket(f="x:xb,y:yb", n="2", O="rng1.csv", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,x,y,xb,yb
    # A,2,7,1,2
    # B,6,7,2,2
    # C,5,6,2,2
    # D,7,5,2,2
    # E,6,4,2,2
    # F,1,3,1,1
    # G,3,3,1,1
    # H,4,2,1,1
    # I,7,2,2,1
    # J,2,1,1,1


**範囲均等化分割**

``rng=True`` オプションを指定すると範囲均等化分割となる。

  .. code-block:: python
    :linenos:

    nm.mbucket(f="x:xb,y:yb", n="2", rng=True, O="rng2.csv", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,x,y,xb,yb
    # A,2,7,1,2
    # B,6,7,2,2
    # C,5,6,2,2
    # D,7,5,2,2
    # E,6,4,2,2
    # F,1,3,1,1
    # G,3,3,1,1
    # H,4,2,2,1
    # I,7,2,2,1
    # J,2,1,1,1


**キー項目を指定した例**

id項目を集計キーとして、 ``x,y`` 項目それぞれを件数均等化バケット分割する。
``n=2,3`` と指定することで、 ``x`` 項目の分割数は2に、
``y`` 項目の分割数は3となる。
出力形式はバケット番号とバケット範囲の両方を表示する( ``F=2`` )。

  .. code-block:: python
    :linenos:

    nm.mbucket(k="id", f="x:xb,y:yb", n="2,3", F="2", i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id%0,x,y,xb,yb
    # A,2,7,1:_3.5,2:6.5_
    # A,6,7,2:3.5_,2:6.5_
    # A,5,6,2:3.5_,1:_6.5
    # B,7,5,2:3.5_,3:4.5_
    # B,6,4,2:3.5_,2:3.5_4.5
    # B,1,3,1:_3.5,1:_3.5
    # C,3,3,1:_3.5,3:2.5_
    # C,4,2,2:3.5_,2:1.5_2.5
    # C,7,2,2:3.5_,2:1.5_2.5
    # C,2,1,1:_3.5,1:_1.5


関連メソッド
''''''''''''''''''''

* :doc:`mmbucket` : 多次元のセルで件数均等化分割をする場合はこちらを使う。

