mshare 構成比の計算
--------------------------

``f=`` パラメータで指定した項目の構成比を計算し、新しい項目として追加する。\


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | ここで指定された項目（複数項目指定可）の値のシェアが計算される。
  | :(コロン）で新項目名を指定する必要がある。例）f=数量:数量シェア

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | シェア計算の単位となる項目名リスト（複数項目指定可）を指定する。
  | 省略すると全行同じキーの値として処理される。



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
    '''customer,quantity,amount
    A,1,10
    A,2,20
    B,1,15
    B,3,10
    B,1,20
    ''')


**基本例**

``customer`` 項目を単位に ``quantity`` と ``amount`` 項目のシェアを計算し、
「数量シェア」と「金額シェア」という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mshare(k="customer", f="quantity:quantityシェア,amount:amountシェア", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,quantity,amount,quantityシェア,amountシェア
    # A,1,10,0.3333333333,0.3333333333
    # A,2,20,0.6666666667,0.6666666667
    # B,1,15,0.2,0.3333333333
    # B,3,10,0.6,0.2222222222
    # B,1,20,0.2,0.4444444444


関連メソッド
''''''''''''''''''''



