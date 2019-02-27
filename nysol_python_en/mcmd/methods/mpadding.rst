mpadding (行補完) コマンド
--------------------------------------

``k=`` パラメータで指定した項目をキーとして、
``f=`` パラメータで指定した項目の値が連続するようにレコードを作成する。
``v=`` パラメータを指定した場合は、
``k=`` , ``f=`` で指定した以外の項目値を指定した文字列でパディングし、
``n`` オプション指定時は、nullでパディングする。
ただし、 ``v=`` と ``n`` オプション共に指定がなければ直前の項目値でパディングする。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | ここで指定された項目をキーとする。

**f=** : 型=str , 必須

  | 連続パディング対象項目名
  | ここで指定された項目の値が連続するようにレコードをパディングする。
  | 数字としてパディングするときは、no\%nのように\%nを指定する。
  | 日付としてパディングするときは\%d、時刻としてパディングするときは\%tを指定する。
  | 降順でパディングしたいときはno\%d\%rのようにrを追加する。

**v=** : 型=str , 任意(default=)

  | パディング用文字列指定
  | k=,f=で指定した以外の項目値を指定した文字列で出力する。

**S=** : 型=str , 任意(default=)

  | 開始値
  | f=で指定した項目の値の開始値を指定する。

**E=** : 型=str , 任意(default=)

  | 終了値
  | f=で指定した項目の値の終了値を指定する。

**n=** : 型=bool , 任意(default=False)

  | パディングにnull値指定
  | k=,f=で指定した以外の項目値をnullで出力する。



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
, :ref:`x=<common_param_x>`
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
    '''no
    3
    6
    8
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''date,dummy
    20130929,a
    20131002,b
    20131004,c
    ''')


**基本例**

``no`` 項目が整数(\%n)として連続するようにレコードをパディングする。
``1`` とverb|4|の間に ``2,3`` を、 ``4`` と ``2`` の間に ``3`` が挿入されている。

  .. code-block:: python
    :linenos:

    nm.mpadding(f="no%n", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # no%0n
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8


**開始値、終了値の指定**

行間のパディングだけでなく、先頭行/終端行の前後もパディングする。
前後の範囲は ``S=,E=`` で指定する。

  .. code-block:: python
    :linenos:

    nm.mpadding(f="no%n", S="1", E="10", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # no%0n
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10


**日付パディング**

``date`` 項目が日付(\%d)として連続するようにレコードをパディングする。
``k=,f=`` で指定した以外の項目は、直前の行の項目値でパディングする。

  .. code-block:: python
    :linenos:

    nm.mpadding(f="date%d", i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # date%0,dummy
    # 20130929,a
    # 20130930,a
    # 20131001,a
    # 20131002,b
    # 20131003,b
    # 20131004,c


**パディング用文字列指定**

``v=`` にてパディング文字列を指定することもできる。

  .. code-block:: python
    :linenos:

    nm.mpadding(f="date%d", v="padding", i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # date%0,dummy
    # 20130929,a
    # 20130930,padding
    # 20131001,padding
    # 20131002,b
    # 20131003,padding
    # 20131004,c


**パディングにNULL値を指定**

``n=True`` を指定してNULL値でパディングすることも可能。

  .. code-block:: python
    :linenos:

    nm.mpadding(f="date%d", n=True, i="dat2.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # date%0,dummy
    # 20130929,a
    # 20130930,
    # 20131001,
    # 20131002,b
    # 20131003,
    # 20131004,c


関連メソッド
''''''''''''''''''''



