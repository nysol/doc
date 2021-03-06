m2cross 1対Nのクロス集計
----------------------------------

1対Nのクロス集計を行う。
``s=`` を指定した場合には項目の値が項目名となるように横に展開され、
``f=`` で指定した項目がセルとして出力される。
``a=`` を指定した場合(2項目指定)には
指定した値が項目名となり、
１項目に ``f=`` で指定した項目名が、
２項目に ``f=`` で指定した項目値がそれぞれ縦展開される
``k=`` が指定されていた場合には、
指定した値が行idとなり、id単位で展開される。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**fixfld=** : 型=str , 任意(default=)

  | 横に展開する際、データがない場合に追加する項目名を指定する。

**f=** : 型=str , 必須

  | ここで指定された項目の値がセルの値として出力される。
  | a=を使用するときのみ複数項目指定可。

**s=** : 型=str , 任意(default=)

  | 列項目名に展開する項目を指定する。
  | ここで指定された項目の値が項目名として出力される。

**a=** : 型=str , 任意(default=)

  | ２項目指定する。
  | １項目目に ``f=`` で指定した項目名がデータとして展開される項目名を指定する。
  | ２項目目に ``f=`` で指定した項目値の項目名を指定する

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | キー項目名リスト
  | ここで指定した項目を単位に展開をおこなう。

**v=** : 型=str , 任意(default=)

  | NULL値置換文字列
  | NULL値があった場合、 ``v=`` パラメータで指定する置換文字列により、項目の値を置換する。



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
    '''item,date,quantity
    A,20081201,1
    A,20081202,2
    A,20081203,3
    B,20081201,4
    B,20081203,5
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''item,week,quantity
    A,Monday,1
    A,Tuesday,2
    A,Wednesday,3
    B,Thursday,4
    B,Friday,5
    ''')


**基本例**

``item`` 項目を単位に ``date`` 項目を横に展開し、
``quantity`` 項目を出力する。

  .. code-block:: python
    :linenos:

    nm.m2cross(k="item", f="quantity", s="date", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # item%0,20081201,20081202,20081203
    # A,1,2,3
    # B,4,,5


**元の入力データに戻す例**

例1の出力結果を元に戻すには、同じく ``m2cross`` を以下のよう用いればよい。

  .. code-block:: python
    :linenos:

    nm.m2cross(f="2008*", a="date,quantity", i="rsl1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # item%0,date,quantity
    # A,20081201,1
    # A,20081202,2
    # A,20081203,3
    # B,20081201,4
    # B,20081202,
    # B,20081203,5


**並びを逆順する例**

横に展開する項目名の並びを逆順にする。

  .. code-block:: python
    :linenos:

    nm.m2cross(k="item", f="quantity", s="date%r", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # item%0,20081203,20081202,20081201
    # A,3,2,1
    # B,5,,4


**データがない場合に項目を追加する例**

横に展開する際に、データがない場合に項目を追加する"

  .. code-block:: python
    :linenos:

    nm.m2cross(k="item", f="quantity", s="week", i="dat2.csv", fixfld="Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # item%0,Friday,Monday,Saturday,Sunday,Thursday,Tuesday,Wednesday
    # A,,1,,,,2,3
    # B,5,,,,4,,


関連メソッド
''''''''''''''''''''

* :doc:`mcross` : イメージは同じだが、 ``mcross`` はN対Nクロス集計として出力する。\

