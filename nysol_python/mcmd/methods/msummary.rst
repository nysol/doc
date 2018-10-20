msummary 1変数の統計量の計算
--------------------------------------

``f=`` パラメータで指定した集計項目で
``c=`` パラメータで指定した統計量の計算をする。\


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | キー項目名リスト(複数項目指定可)【 :ref:`集計キーブレイク処理<autoadd_keybreak>` 】
  | ここで指定された項目を単位として集計する。
  | 指定する場合は事前に指定する集計の単位となる項目順に並べ替えておく必要がある。

**f=** : 型=str , 必須

  | 集計項目名リスト(複数項目指定可)
  | ここで指定された項目の値が集計される。
  | ``x`` , ``nfn`` オプション使用時は、項目番号(0～)で指定。

**c=** : 型=str , 必須

  | 統計量リスト(複数項目指定可)
  | 出力する統計量をコンマで区切って指定する。
  | 統計量リスト:
  | ``sum/mean/count/ucount/devsq/var/uvar/sd/usd/cv/min/qtile1/median/qtile3/max/``
  | ``range/qrange/mode/skew/uskew/kurt/ukurt``

**a=** : 型=str , 任意(default=)

  | 新項目名を指定する。
  | ``f=`` パラメータで指定した項目名をデータとして出力する際の項目名(省略時はfld)を指定する。

**n=** : 型=bool , 任意(default=False)

  | NULL値が1つでも含まれていると結果もNULL値とする。



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
    '''customer,quantity,amount
    A,1,10
    A,2,20
    B,1,15
    B,3,10
    B,1,20
    ''')


**基本例**

``customer`` 項目を単位に ``quantity`` と ``amount`` 項目の中央値・平均値を求める。
統計量を求めた項目名は「変数」という項目に出力する。

  .. code-block:: python
    :linenos:

    nm.msummary(k="customer", f="quantity,amount", c="median:中央値,mean:平均値", a="変数", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,変数,中央値,平均値
    # A,quantity,1.5,1.5
    # A,amount,15,15
    # B,quantity,1,1.666666667
    # B,amount,15,15


関連メソッド
''''''''''''''''''''

* :doc:`mstats` : 求める統計量が1つのとき用いる。

