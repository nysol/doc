mnormalize 基準化
----------------------------

``f=`` パラメータで指定した項目を、 ``c=`` パラメータで指定した基準化の方法で基準化する。\


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**c=** : 型=str , 必須

  | 以下に示す基準化の方法のいずれかを指定する。
  | ``z``  : z得点 :  :math:`z_i=(x_i-m)/u`  ( :math:`x_i` :  :math:`i` 番目のデータ,  :math:`m`  :算術平均,  :math:`u`  :標準偏差)
  | ``Z``  : 偏差値 :  :math:`Z_i=50+10	imes z_i` 
  | ``range``  : 最小値を0,最大値を1に線形変換  :math:`r_i=(x_i-\min_x)/(\max_x-\min_x)`

**f=** : 型=str , 必須

  | ここで指定された項目が基準化される。
  | :(コロン）で新項目名を指定する必要がある。例） ``f=`` 数量:数量基準値

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | キー項目名リスト
  | ここで指定された項目を単位に基準化を行う。

**bufcount=** : 型=str , 任意(default=)

  | バッファのサイズ数を指定する。



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
    '''customer,quantity,amount
    A,1,10
    A,2,20
    B,1,15
    B,3,10
    B,1,20
    ''')


**基本例**

``customer`` を単位にして ``quantity`` と ``amount`` 項目を基準化（z得点）し、
``qttNorm`` と ``amtNorm`` という項目名で出力する。

  .. code-block:: python
    :linenos:

    nm.mnormalize(c="z", k="customer", f="quantity:qttNorm,amount:amtNorm", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # customer%0,quantity,amount,qttNorm,amtNorm
    # A,1,10,-0.7071067812,-0.7071067812
    # A,2,20,0.7071067812,0.7071067812
    # B,1,15,-0.5773502692,0
    # B,3,10,1.154700538,-1
    # B,1,20,-0.5773502692,1


**偏差値**


  .. code-block:: python
    :linenos:

    nm.mnormalize(c="Z", k="customer", f="quantity:qttNorm,amount:amtNorm", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # customer%0,quantity,amount,qttNorm,amtNorm
    # A,1,10,42.92893219,42.92893219
    # A,2,20,57.07106781,57.07106781
    # B,1,15,44.22649731,50
    # B,3,10,61.54700538,40
    # B,1,20,44.22649731,60


**0から1への線形変換**


  .. code-block:: python
    :linenos:

    nm.mnormalize(c="range", k="customer", f="quantity:qttNorm,amount:amtNorm", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # customer%0,quantity,amount,qttNorm,amtNorm
    # A,1,10,0,0
    # A,2,20,1,1
    # B,1,15,0,0.5
    # B,3,10,1,0
    # B,1,20,0,1


関連メソッド
''''''''''''''''''''



