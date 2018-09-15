mchgstr 文字列の置換
----------------------------

``f=`` パラメータで指定した項目について、
``c=`` パラメータで指定した置換条件で文字列を置換する。

パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**c=** : 型=str , 必須

  | 置換対象となる文字列と置換文字列を指定する。

**f=** : 型=str , 必須

  | ここで指定した項目(複数項目指定可)の文字列を ``c=`` パラメータで指定した置換条件リストに従って置換する。

**O=** : 型=str , 任意(default=null値)

  | ``c=`` パラメータで指定した置換条件リストのいずれとも合致しない値を
  | 置換するときの文字列(指定がなければNULL値となる)を指定する。

**A=** : 型=bool , 任意(default=False)

  | このオプションにより、指定した項目を置き換えるのではなく、

**F=** : 型=bool , 任意(default=False)

  | ``c=`` パラメータで指定した置換条件リストのいずれとも合致しない値は、
  | その項目の値のまま出力する。

**sub=** : 型=bool , 任意(default=False)

  | 検索を完全一致ではなく部分文字列マッチで比較する
  | すなわち、 ``f=`` パラメータで指定した項目の値に、
  | ``c=`` パラメータで指定した置換条件で文字列を置換する。

**W=** : 型=bool , 任意(default=False)

  | ``sub=True`` オプションが指定されているときにワイド文字として部分文字列マッチをおこなう。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
, :ref:`assert_nullout=<common_param_assert_nullout>`
, :ref:`nfn=<common_param_nfn>`
, :ref:`nfno=<common_param_nfno>`
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
    '''id,item
    1,01
    2,02
    3,03
    4,04
    5,05
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,item
    1,0111
    2,0121
    3,0231
    4,0241
    5,0151
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''id,city
    1,奈良市
    2,下市町
    3,十津川村
    4,五條市
    5,山添村
    ''')


**基本例**

``item`` の値が
``"01"`` を ``"A"`` に、
``"03"`` を ``"B"`` に、
``"04"`` を ``"C"`` に置換する。
その他はNULL値として出力する。

  .. code-block:: python
    :linenos:

    nm.mchgstr(f="item", c="01:A,03:B,05:C", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,item
    # 1,A
    # 2,
    # 3,B
    # 4,
    # 5,C


**条件に合致しない値を置換する文字列の指定**

``O=`` パラメータを指定することで、
置換条件に合致しない場合は ``"out of range"`` という文字列に置換して出力する。

  .. code-block:: python
    :linenos:

    nm.mchgstr(f="item", c="01:A,03:B,05:C", O="out of range", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,item
    # 1,A
    # 2,out of range
    # 3,B
    # 4,out of range
    # 5,C


**新しい項目として出力**

``A=True`` オプションを付けることで、新しい項目( ``item info`` )として出力する。

  .. code-block:: python
    :linenos:

    nm.mchgstr(f="item:item info", c="01:A,03:B,05:C", O="out of range", A=True, i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,item,item info
    # 1,01,A
    # 2,02,out of range
    # 3,03,B
    # 4,04,out of range
    # 5,05,C


**条件外を項目の値として出力**

``F=True`` オプションを付けることで、
置換条件に合致しない場合は、元の値をそのまま出力する。

  .. code-block:: python
    :linenos:

    nm.mchgstr(f="item", c="01:A,03:B,05:C", F=True, i="dat1.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,item
    # 1,A
    # 2,02
    # 3,B
    # 4,04
    # 5,C


**条件を部分文字列マッチで置換**

``sub=True`` オプションをつけることで、部分文字列の置換となる。
以下の例では、 ``item`` 項目に文字列 ``"01"`` が含まれていれば、それを ``"A"`` に置換する。

  .. code-block:: python
    :linenos:

    nm.mchgstr(f="item", c="01:A", sub=True, i="dat2.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # id,item
    # 1,A11
    # 2,A21
    # 3,
    # 4,
    # 5,A51


**ワイド文字での部分文字列マッチ**

ワイド文字の部分文字列置換をする場合は ``W=True`` オプションを用いる。
ただし、UTF-8エンコーディングを用いているのであれば ``W=True`` をつけなくても正しく動作する。
詳しくは「\hyperref[sect:multibyte]{マルチバイト文字}」の節を参照されたい。

  .. code-block:: python
    :linenos:

    nm.mchgstr(f="city", c="市:01,町:02,村:02", sub=True, W=True, i="dat3.csv", o="rsl6.csv").run()
    ### rsl6.csv の内容
    # id,city
    # 1,奈良01
    # 2,下0102
    # 3,十津川02
    # 4,五條01
    # 5,山添02


関連メソッド
''''''''''''''''''''

* :doc:`mchgnum` : 数値範囲による置換ならばこちら。
* :doc:`msed` : 正規表現による置換が可能。

