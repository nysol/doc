mtraflg クロス表をトランザクション項目に変換
----------------------------------------------------

``f=`` パラメータで指定した項目値がNULL値かどうかをチェックし、
NULL値以外であれば，それらの項目名を1つのアイテムとして連結し
新しいベクトル項目(トランザクション項目とも呼ぶ)として出力する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**a=** : 型=str , 必須

  | トランザクション項目名を指定する。

**f=** : 型=str , 必須

  | ここで指定された項目値(複数項目指定可)をチェックし、トランザクションデータを作成する。
  | ( ``r`` オプションの指定がある時はトランザクションデータから項目名として抜き出す値のリスト)

**delim=** : 型=str , 任意(default=)

  | ここで指定した文字をトランザクション項目のアイテム間の区切りとする（省略時はスペース）。
  | 文字列の指定はできない。1バイト文字のみ指定可能。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | トランザクション型から縦型へデータを変換する。



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
    '''customer,egg,milk
    A,1,1
    B,,1
    C,1,
    D,1,1
    ''')


**基本例**

``egg`` と ``milk`` 項目の値がNULL値以外なら、それら項目名を要素としたベクトルを作成する。

  .. code-block:: python
    :linenos:

    nm.mtraflg(f="egg,milk", a="transaction", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer,transaction
    # A,egg milk
    # B,milk
    # C,egg
    # D,egg milk


**基本例2**

出力された結果を ``r=True`` をつけて再実行し元に戻す。

  .. code-block:: python
    :linenos:

    nm.mtraflg(r=True, f="egg,milk", a="transaction", i="rsl1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer,egg,milk
    # A,1,1
    # B,,1
    # C,1,
    # D,1,1


**区切り文字の指定**

区切り文字を-(ハイフン）で連結し、 ``transaction`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mtraflg(f="egg,milk", a="transaction", delim="-", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer,transaction
    # A,egg-milk
    # B,milk
    # C,egg
    # D,egg-milk


関連メソッド
''''''''''''''''''''

* :doc:`mvsort` : トランザクションデータはベクトル型データを処理する一連の処理コマンド( ``mv`` から始まる)によって加工できる。
* :doc:`mcross` : トランザクションデータとしてではなく、個々のアイテムを独立した項目として出力し、その出現件数を出力する。
* :doc:`mtra` : 項目の値をアイテムとしてトランザクションデータを作成する。
* :doc:`mtrafld` : 「項目名=値」の形式でトランザクションデータを作成する。

