msed 正規表現による文字列置換
----------------------------------

``f=`` パラメータで指定した項目について、
``c=`` パラメータで指定した正規表現に一致する内容を
``v=`` パラメータ指定した文字列で置換する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | 置換対象となる項目名リスト(複数項目指定可)を指定する。

**c=** : 型=str , 必須

  | 置換したい文字列についての正規表現を指定する。
  | 正規表現の使用方法参照

**v=** : 型=str , 必須

  | ``c=`` パラメータで指定した正規表現にマッチした部分文字列が、
  | ここで指定した文字列に置換される。
  | マッチ結果を用いた置換も可能で、指定方法は以下の通り。
  | erb|$
  | ``$```  : 置換対象文字列の先頭から、マッチした文字列の直前までの文字列
  | ``$'``  : マッチした文字列の直後から、置換対象文字列の最後までの文字列
  | ``$N``  : N番目の部分マッチ文字列( ``N>=1`` )

**A=** : 型=bool , 任意(default=False)

  | このオプションにより、指定した項目を置き換えるのではなく、
  | 新たに項目が追加される。

**g=** : 型=bool , 任意(default=False)

  | 正規表現にマッチする全ての部分文字列を置換対象とする。

**W=** : 型=bool , 任意(default=False)

  | ワイド文字として正規表現による文字列置換を行う。



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
    '''customer,zipCode
    A,6230041
    B,6240053
    C,6330032
    D,6230087
    E,6530095
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''item,price
    fruit:apple,100
    fruit:peach,250
    fruit:pineapple,300
    fruit:orange,450
    fruit:grapefruit,500
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''str1
    abc
    abbc
    ac
    ''')


**基本例**

``zipCode`` 項目の値が00から始まる4桁文字列を ``####`` に置換する。

  .. code-block:: python
    :linenos:

    nm.msed(f="zipCode", c="00..", v="####", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,zipCode
    # A,623####
    # B,624####
    # C,633####
    # D,623####
    # E,653####


**項目名指定**

``zipCode`` の値が00から始まる4桁の数字を ``####`` に置換し、 ``zipCode4`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.msed(f="zipCode:zipCode4", c="00\d\d", v="####", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer,zipCode4
    # A,623####
    # B,624####
    # C,633####
    # D,623####
    # E,653####


**グローバル置換**

``zipCode`` の値が ``0`` を全て ``=True`` にグローバル置換する。

  .. code-block:: python
    :linenos:

    nm.msed(f="zipCode", c="0", v="-", g=True, i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer,zipCode
    # A,623--41
    # B,624--53
    # C,633--32
    # D,623--87
    # E,653--95


**部分置換**

``item`` の先頭の ``fruit`` を削除する。
先頭一致( ``^`` )を指定しているので、最後の行の ``grapefruit`` は削除されていないことに注意する。

  .. code-block:: python
    :linenos:

    nm.msed(f="item", c="^fruit", v="", g=True, i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # item,price
    # :apple,100
    # :peach,250
    # :pineapple,300
    # :orange,450
    # :grapefruit,500


**マッチ結果を用いた置換**

``v=`` の中で ``$&`` を用いれば、マッチした文字列(連続した ``b`` )に置き換わる。

  .. code-block:: python
    :linenos:

    nm.msed(f="str1", c="b+", v="#$&#", i="dat3.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # str1
    # a#b#c
    # a#bb#c
    # ac


**グローバルマッチとの組み合せ**

グローバルマッチにすると、個々のマッチ毎に ``v=`` の内容が評価される。

  .. code-block:: python
    :linenos:

    nm.msed(f="str1", c="b", v="#$&#", g=True, i="dat3.csv", o="rsl6.csv").run()
    ### rsl6.csv の内容
    # str1
    # a#b#c
    # a#b##b#c
    # ac


**プレフィックス置換**

``$``` にて、マッチした箇所の前の文字列(プレフィックス)に置換される。

  .. code-block:: python
    :linenos:

    nm.msed(f="str1", c="b", v="#$`#", i="dat3.csv", o="rsl7.csv").run()
    ### rsl7.csv の内容
    # str1
    # a#a#c
    # a#a#bc
    # ac


**サフィックス置換**

``$'`` にて、マッチした箇所の後の文字列(サフィックス)に置換される。

  .. code-block:: python
    :linenos:

    nm.msed(f="str1", c="b", v="#$'#", i="dat3.csv", o="rsl8.csv").run()
    ### rsl8.csv の内容
    # str1
    # a#c#c
    # a#bc#bc
    # ac


関連メソッド
''''''''''''''''''''

* :doc:`mchgstr` : 単純な文字列マッチによる置換であればこのコマンドを利用する。
* :doc:`mcal` : 正規表現を扱う関数がいくつか用意されている。

