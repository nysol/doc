mtrafld クロス表をトランザクション項目に変換
----------------------------------------------------

``f=`` で指定した項目値とその値のペアのアイテムを作成し、
それらのアイテムを連結し新しいベクトル項目(トランザクション項目とも呼ぶ)として出力する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**a=** : 型=str , 必須

  | トランザクション項目名を指定する。

**f=** : 型=str , 条件付き必須(``r`` オプション指定時必須)

  | 項目名リスト(複数項目指定可)
  | ここで指定された項目名と値とを連結したアイテムを作成し
  | トランザクション項目として出力される。
  | ``r`` オプションの指定がある時は
  | トランザクションデータから抜き出す項目名を指定する。
  | ``r`` オプションが指定されたとき，このパラメータは省略可能である。
  | 省略すると、全ての項目名と値ペアを処理対象とする。
  | ただし、 ``f=`` パラメータを省略すると標準入力(パイプ入力)は利用できない。

**delim=** : 型=str , 任意(default=)

  | トランザクション項目のアイテムを区切る文字を指定する(省略時はスペース)。

**delim2=** : 型=str , 任意(default=)

  | 項目名と値ペアとを区切る文字を指定する(省略時は=)。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | トランザクション項目をクロス表に変換する。

**valOnly=** : 型=bool , 任意(default=False)

  | このオプションが指定されると、アイテムとして「項目名=」は出力しない。



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
    '''customer,price,quantity
    A,198,1
    B,325,2
    C,200,3
    D,450,2
    E,100,1
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer,price,quantity
    A,198,1
    B,,2
    C,200,
    D,450,2
    E,,
    ''')


**基本例**

``price`` と ``quantity`` 項目を1つの文字列として連結し、
``transaction`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mtrafld(a="transaction", f="price,quantity", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,transaction
    # A,price=198 quantity=1
    # B,price=325 quantity=2
    # C,price=200 quantity=3
    # D,price=450 quantity=2
    # E,price=100 quantity=1


**基本例2**

出力された結果を ``r=True`` をつけて再実行し元に戻す。

  .. code-block:: python
    :linenos:

    nm.mtrafld(r=True, a="transaction", f="price,quantity", i="rsl1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer,price,quantity
    # A,198,1
    # B,325,2
    # C,200,3
    # D,450,2
    # E,100,1


**区切り文字の指定**

``price`` と数量 ``quantity`` 項目を\_(アンダーバー）で区切り1つの文字列として連結し、
項目名とデータは：（コロン）で区切り ``transaction`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mtrafld(a="transaction", f="price,quantity", delim="_", delim2=":", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer,transaction
    # A,price:198_quantity:1
    # B,price:325_quantity:2
    # C,price:200_quantity:3
    # D,price:450_quantity:2
    # E,price:100_quantity:1


**NULL値を含む場合**


  .. code-block:: python
    :linenos:

    nm.mtrafld(a="transaction", f="price,quantity", i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # customer,transaction
    # A,price=198 quantity=1
    # B,quantity=2
    # C,price=200
    # D,price=450 quantity=2
    # E,


**NULL値を含む場合2**

出力された結果を ``r=True`` をつけて再実行し元に戻す。

  .. code-block:: python
    :linenos:

    nm.mtrafld(r=True, a="transaction", f="price,quantity", i="rsl4.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # customer,price,quantity
    # A,198,1
    # B,,2
    # C,200,
    # D,450,2
    # E,,


**-valOnlyの指定**


  .. code-block:: python
    :linenos:

    nm.mtrafld(valOnly=True, f="price,quantity", a="transaction", i="dat2.csv", o="rsl6.csv").run()
    ### rsl6.csv の内容
    # customer,transaction
    # A,198 1
    # B,2
    # C,200
    # D,450 2
    # E,


関連メソッド
''''''''''''''''''''

* :doc:`mvsort` : トランザクションデータはベクトル型データを処理する一連の処理コマンド( ``mv`` から始まる)によって加工できる。
* :doc:`mcross` : トランザクションデータとしてではなく、個々のアイテムを独立した項目として出力し、その出現件数を出力する。
* :doc:`mtra` : 項目の値をアイテムとしてトランザクションデータを作成する。
* :doc:`mtraflg` : 項目名をアイテムとしてトランザクションデータを作成する。

