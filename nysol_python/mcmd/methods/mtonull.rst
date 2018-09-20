mtonull NULL値へ置換
--------------------------------

``f=`` パラメータで指定した項目を対象に、
``v=`` パラメータで指定した値にマッチした項目データをNULL値に置換する。
マッチの方法としては完全一致(デフォルト)と部分文字列マッチ( ``sub`` オプション)を選択できる。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 出力データを指定する。

**f=** : 型=str , 必須

  | 置換対象の項目名リスト(複数項目指定可)を指定する。

**v=** : 型=str , 必須

  | ``f=`` パラメータで指定した項目の値が、ここで指定した文字列リスト(複数項目指定可)
  | のいずれかにマッチすればNULL値に置換する。

**sub=** : 型=bool , 任意(default=False)

  | 部分文字列マッチを行う。

**W=** : 型=bool , 任意(default=False)

  | ワイド文字としてマッチを行う。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
, :ref:`assert_nullin=<common_param_assert_nullin>`
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
    '''item,quantity,price
    A,0,1
    B,1,0
    C,2,200
    D,3,0
    E,0,298
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''item,price
    fruit:apple,100
    fruit:peach,250
    fruit:grape,300
    fruit:pineapple,450
    fruit:orange,500
    ''')


**基本例**

``quantity`` と ``price`` 項目が0をNULL値に置換する。

  .. code-block:: python
    :linenos:

    nm.mtonull(f="quantity,price", v="0", i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # item,quantity,price
    # A,,1
    # B,1,
    # C,2,200
    # D,3,
    # E,,298


**NULL値に置換する数字の指定**

``quantity`` と ``price`` 項目が0もしくは1をNULL値に置換する。

  .. code-block:: python
    :linenos:

    nm.mtonull(f="quantity,price", v="0,1", i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # item,quantity,price
    # A,,
    # B,,
    # C,2,200
    # D,3,
    # E,,298


**部分文字列マッチでの置換**

``quantity`` と ``price`` 項目が0を含めばNULL値に置換する。

  .. code-block:: python
    :linenos:

    nm.mtonull(sub=True, f="quantity,price", v="0", i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # item,quantity,price
    # A,,1
    # B,1,
    # C,2,
    # D,3,
    # E,,298


**指定の文字列の置換**

``item`` 項目に ``apple、orange、pineapple`` を含む値をNULL値に置換する。

  .. code-block:: python
    :linenos:

    nm.mtonull(f="item", v="apple,orange,pineapple", sub=True, i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # item,price
    # ,100
    # fruit:peach,250
    # fruit:grape,300
    # ,450
    # ,500


関連メソッド
''''''''''''''''''''

* :doc:`mnullto` : 逆にNULL値を指定の文字列に置換する。

