mmbucket 多次元均等化バケット分割
------------------------------------------

``f=`` で指定した複数の数値項目を次元とした件数均等化バケット分割を行う。
例えば、 ``f=a,b,c`` そして ``n=5`` と指定すると、
:doc:`mbucket` コマンドと同様に、項目 ``a,b,c`` それぞれを5つの区間に分割するが、
``mmbucket`` では、項目 ``a,b,c`` の3次元空間における各バケット(バケット数は :math:`5^3=125` 個になる)に
属する件数ができるだけ均等になるような区間を計算する

パラメータ
''''''''''''''''''''''

  .. list-table::
   :header-rows: 1

   * - キーワード
     - 内容
   * - | **i=str**
       | 任意
     - | 入力データを指定する。
   * - | **o=str**
       | 任意
     - | 出力データを指定する。
   * - | **f=str**
       | 必須
     - | ここで指定した項目(複数項目指定可)の値を分割する。
       | 複数指定すれば、その数の次元に基づく均等化バケット分割を行う。
       | 1項目のみ指定すれば ``mbucket`` と同じ結果になる。
       | ``x,-nfn=True`` オプション使用時は、項目番号(0〜)で指定可能。
   * - | **n=str**
       | 必須
     - | ``f=`` で指定した項目数と同じ個数分指定する。
       | ただし1つの数字を指定した場合、 ``f=`` で指定した全ての項目に、同じ分割数が適用される。
   * - | **F=str**
       | 任意
     - | 出力形式を指定する。
       | バケットの名前を出力形式。
       | 0:バケット番号のみを表示する。
       | 1:バケットの範囲のみを表示する。
       | 2:バケット番号とバケット範囲の両方を表示する。
   * - | **k=str**
       | 任意
     - | バケット分割を行う単位となる項目名リスト(複数項目指定可)を指定する。
   * - | **O=str**
       | 任意
     - | ``f=`` パラメータで指定した各項目の各バケットの数値範囲を出力するデータを指定する。
   * - | **bufcount=str**
       | 任意
     - | バッファのサイズ数を指定する。
   * - | **ms=bool**
       | 任意
     - | 各項目を順次バケット分割していく時の開始項目を変えることで複数回のバケット分割をトライし、
       | よりよい解を求める。詳細は、以下の「アルゴリズムの概要」を参照のこと。
   * - | **r=bool**
       | 任意
     - | バケット番号を逆順に出力する。


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

``x、y`` 項目の件数ができるだけ多次元均等になるように2分割する。
その際、各バケットの数値範囲を ``rng.csv`` という名前のファイルに出力する。

  .. code-block:: python
    :linenos:

    nm.mmbucket(f="x:xb,y:yb", n="2,2", O="rng.csv", i="dat1.csv", o="rsl1.csv").run()
