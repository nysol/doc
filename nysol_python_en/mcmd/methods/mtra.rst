mtra 縦型データをベクトル項目に変換
----------------------------------------

``f=`` パラメータで指定した項目値をアイテムとし、それらのアイテムを連結し新しいベクトル項目(トランザクション項目とも呼ぶ)として出力する。
アイテムの区切り文字は ``delim=`` パラメータで指定する。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | ここで指定した項目(複数項目指定可)の値がアイテムとして連結されトランザクション項目となる。
  | NULL値は無視される。

**s=** : 型=str , 任意(default=)

  | ここで指定した項目(複数項目指定可)で並べ替えられた後、変換が行われる。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 文字列パターンの単位となる項目名(複数項目指定可)リスト。
  | ``r`` オプションが指定された時は指定できない。

**delim=** : 型=str , 任意(default=)

  | ここで指定した文字を区切り文字とする（省略時はスペース）。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | トランザクション項目を縦型データに変換する。



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
    '''customer,item
    A,a
    A,b
    B,c
    B,d
    B,e
    ''')


**基本例**

``customer`` を単位に ``item`` をスペース区切りで結合し、
``transaction`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mtra(k="customer", f="item:transaction", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,transaction
    # A,a b
    # B,c d e


**アイテムの区切り文字を-(ハイフン）で実行**


  .. code-block:: python
    :linenos:

    nm.mtra(k="customer", f="item:transaction", delim="-", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer%0,transaction
    # A,a-b
    # B,c-d-e


**アイテムを降順に並べ替えてから変換**


  .. code-block:: python
    :linenos:

    nm.mtra(k="customer", s="item%r", f="item:transaction", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer%0,transaction
    # A,b a
    # B,e d c


関連メソッド
''''''''''''''''''''

* :doc:`mvsort` : トランザクションデータは、ベクトル型データを処理する一連の処理コマンド( ``mv`` から始まる)によって加工できる。
* :doc:`mcross` : トランザクションデータとしてではなく、個々のアイテムを独立した項目として出力し、その出現件数を出力する。
* :doc:`mtrafld` : 「項目名=値」の形式でトランザクションデータを作成する。
* :doc:`mtraflg` : 項目名をアイテムとしてトランザクションデータを作成する。

