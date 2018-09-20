msel 条件式による行選択
----------------------------

``c=`` パラメータで指定した計算式で計算をおこない、結果が真であれば、その行を選択する。
なおmcalと同じ計算式が利用できるので、詳細は :doc:`mcal` を参照されたい。


パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**c=** : 型=str , 必須

  | 用意された関数を組み合わせて計算する式を指定する。
  | 詳細は :doc:`mcal` を参照。

**o=** : 型=str , 任意(default=標準出力)

  | 指定の条件に一致する行を出力するデータを指定する。

**u=** : 型=str , 任意(default=出力しない)

  | 指定の条件に一致しない行を出力するデータを指定する。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | 選択ではなく削除する。



共通パラメータ
''''''''''''''''''''

:ref:`i=<common_param_i>`
, :ref:`o=<common_param_o>`
, :ref:`assert_diffSize=<common_param_assert_diffSize>`
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
    '''customer,quantity,amount
    A,1,10
    A,2,20
    B,1,30
    B,3,40
    B,1,50
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''a,b
    A,-1
    B,
    C,1
    ''')


**基本例**

``amount`` 項目の値が40より大きい行を選択する。
それ以外のデータは ``unmatch1.csv`` に出力する。

  .. code-block:: python
    :linenos:

    nm.msel(c="${amount}>40", u="unmatch1.csv", i="dat1.csv", o="match1.csv").run()
    ### unmatch1.csv の内容
    # customer,quantity,amount
    # A,1,10
    # A,2,20
    # B,1,30
    # B,3,40
    ### match1.csv の内容
    # customer,quantity,amount
    # B,1,50


**NULL値の選択規制**

``msel`` コマンドでは ``c=`` で与えられた式を評価した結果がNULL値の場合その行は選択されない。
また、アンマッチ出力ファイルが ``u=`` によって指定されていれば、そのファイルに出力される。
以下の例では項目 ``b`` に ``1=True`` 、NULL値、 ``1`` を持つ3行のデータについて、0より大きい行を選択しているが、
NULL値を含む行はアンマッチ出力ファイルへと出力される。

  .. code-block:: python
    :linenos:

    nm.msel(c="${b}>0", i="dat2.csv", o="match2.csv", u="unmatch2.csv").run()
    ### match2.csv の内容
    # a,b
    # C,1
    ### unmatch2.csv の内容
    # a,b
    # A,-1
    # B,


**-rオプション指定**

真偽は逆転するがNULL値の評価に変わりはない。
すなわちNULL値の行は選択されない。
以下の例では、上の例と同様のデータおよび選択条件で ``r=True`` をつけている。
真偽の選択条件は逆転しているが、NULL値を含む行は上記の例と同様にアンマッチファイルへと出力されていることがわかる。

  .. code-block:: python
    :linenos:

    nm.msel(r=True, c="${b}>0", i="dat2.csv", o="match3.csv", u="unmatch3.csv").run()
    ### match3.csv の内容
    # a,b
    # A,-1
    ### unmatch3.csv の内容
    # a,b
    # B,
    # C,1


関連メソッド
''''''''''''''''''''

* :doc:`mselnum` : 簡単な数値範囲による行選択はこちら。
* :doc:`mselstr` : 簡単な文字列マッチによる行選択はこちら。
* :doc:`mcal` : 行選択でなく、計算の結果を項目として出力する。

