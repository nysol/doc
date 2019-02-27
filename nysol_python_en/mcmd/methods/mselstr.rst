mselstr 文字列による行選択
----------------------------------

``f=`` で指定した項目の値が、 ``v=`` で指定した文字列に一致すれば、その行を選択する。
典型例を :numref:`mselstr_input` 〜 :numref:`mselstr_out2` に示す。
:numref:`mselstr_out1` では ``key`` に関係なく ``val`` が ``"y"`` である行を選択する。
:numref:`mselstr_out2` では、 ``val`` が ``"x"`` の行を含んでいる同一キーの行全て、
すなわち ``key`` 項目が ``"a"`` である行全てを選択する。
すなわち ``key`` 項目が ``"b"`` の行はいずれも ``"x"`` を含んでいないので選択されない。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mselstr_input

  key,val
  a,x
  a,y
  b,y
  b,z




.. csv-table:: f=val v=y
  :header-rows: 1
  :name: mselstr_out1

  key,val
  a,y
  b,y




.. csv-table:: k=key f=val v=x
  :header-rows: 1
  :name: mselstr_out2

  key,val
  a,x
  a,y


また、以下に示すように多様な選択条件を指定することも可能である。
このコマンドで指定できない複雑な条件(例えば正規表現など)を設定するのであれば
:doc:`msel` コマンドを利用すればよい。

 *   ``v=`` に複数の文字列を指定すれば、いずれかの文字列にマッチすれば選択される。
 *   ``f=`` に複数項目を指定すれば、いずれかの項目の値がマッチすれば選択される。
 *  複数項目のマッチ条件をAND条件とすることも可能( ``F`` オプション)。
 *  完全一致だけでなく、先頭一致、末尾一致、部分一致の指定も可能( ``head`` , ``tail`` ``sub`` オプション)。
 *   ``k=`` を指定することでキー単位で選択することが可能。
 *  キー単位選択の場合、複数レコードのAND条件を指定可能( ``R`` オプション)。

いま同じキーのデータとして２項目２行からなるデータ( :numref:`mselstr_input2` )に対して、
``mselstr k=key f=fld1,fld2 v=s1,s2``
を実行した場合、
オプション ``R`` , ``F`` の指定の有無によるマッチ条件を :numref:`mselstr_cond` に示す。


.. csv-table:: 入力データ
  :header-rows: 1
  :name: mselstr_input2

  :math:` ``key`` ` , :math:` ``fld1`` ` , :math:` ``fld2`` `
  k, :math:`v_{a1}` , :math:`v_{a2}`
  k, :math:`v_{b1}` , :math:`v_{b2}`




.. csv-table::  :numref:`mselstr_input2` で示されるデータに、mselstr k=key f=fld1,fld2 v=v1,v2を実行した時の、-R,-Fオプションの指定の有無によるマッチ条件の違い。条件にマッチすれば全行(２行)出力され、アンマッチなら１行も出力されない。
  :header-rows: 1
  :name: mselstr_cond

  ``F`` オプション, ``R`` オプション,マッチ条件
  ,,(( :math:`v_{a1}`   ``==``  s1 or  :math:`v_{a1}`   ``==``  s2)  or ( :math:`v_{a2}`   ``==``  s1 or  :math:`v_{a2}`   ``==``  s2)) or (( :math:`v_{b1}`   ``==``  s1 or  :math:`v_{b1}`   ``==``  s2)  or ( :math:`v_{b2}`   ``==``  s1 or  :math:`v_{b2}`   ``==``  s2))
  -F,,(( :math:`v_{a1}`   ``==``  s1 or  :math:`v_{a1}`   ``==``  s2)  and ( :math:`v_{a2}`   ``==``  s1 or  :math:`v_{a2}`   ``==``  s2)) or (( :math:`v_{b1}`   ``==``  s1 or  :math:`v_{b1}`   ``==``  s2)  and ( :math:`v_{b2}`   ``==``  s1 or  :math:`v_{b2}`   ``==``  s2))
  ,-R,(( :math:`v_{a1}`   ``==``  s1 or  :math:`v_{a1}`   ``==``  s2)  or ( :math:`v_{a2}`   ``==``  s1 or  :math:`v_{a2}`   ``==``  s2)) and (( :math:`v_{b1}`   ``==``  s1 or  :math:`v_{b1}`   ``==``  s2)  or ( :math:`v_{b2}`   ``==``  s1 or  :math:`v_{b2}`   ``==``  s2))
  -F,-R,(( :math:`v_{a1}`   ``==``  s1 or  :math:`v_{a1}`   ``==``  s2)  and ( :math:`v_{a2}`   ``==``  s1 or  :math:`v_{a2}`   ``==``  s2)) and (( :math:`v_{b1}`   ``==``  s1 or  :math:`v_{b1}`   ``==``  s2)  and ( :math:`v_{b2}`   ``==``  s1 or  :math:`v_{b2}`   ``==``  s2))




パラメータ
''''''''''''''''''''''

**i=** : 型=str , 任意(default=標準入力)

  | 入力データを指定する。

**f=** : 型=str , 必須

  | 検索対象となる項目名リスト(複数項目指定可)を指定する。

**v=** : 型=str , 必須

  | ``f=`` パラメータで指定した項目の値が、ここで指定した文字列リスト(複数項目指定可)の1つにマッチすれば選択される。

**k=** : 型=str , 任意(default=キーブレイク処理しない)

  | 選択する単位となるキー項目(複数項目指定可)を指定する。

**o=** : 型=str , 任意(default=標準出力)

  | 指定の条件に一致する行を出力するデータを指定する。

**u=** : 型=str , 任意(default=出力しない)

  | 指定の条件に一致しない行を出力するデータを指定する。

**F=** : 型=bool , 任意(default=False)

  | ``f=``  パラメータで複数項目を指定した場合、その全ての値がマッチする行を撰択する。

**r=** : 型=bool , 任意(default=False)

  | 条件反転
  | 選択ではなく削除する。

**R=** : 型=bool , 任意(default=False)

  | ``k=``  パラメータを指定した場合、その全ての行がマッチすれば行を撰択する。

**sub=** : 型=bool , 任意(default=False)

  | 検索を完全一致ではなく部分文字列マッチで比較する。
  | すなわち、 ``f=`` パラメータで指定した項目の値に、
  | ``v=`` パラメータで指定の文字列が部分文字列として含まれていればその行を撰択する。

**head=** : 型=bool , 任意(default=False)

  | 先頭文字列マッチオプション

**tail=** : 型=bool , 任意(default=False)

  | 末尾文字列マッチオプション

**W=** : 型=bool , 任意(default=False)

  | ``sub`` , ``head`` , ``tail`` オプションが指定されているときにワイド文字として部分文字列マッチをおこなう。

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
    '''item,amount
    apple,100
    milk,350
    orange,100
    pineapplejuice,500
    wine,1000
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''customer,item,amount
    A,apple,100
    A,milk,350
    B,orange,100
    B,orange,100
    B,pineapple,500
    B,wine,1000
    C,apple,100
    C,orange,100
    ''')

    with open('dat3.csv','w') as f:
      f.write(
    '''item,amount
    果物:柿,100
    果物:桃,250
    果物:葡萄,300
    果物:梨,450
    果物:苺,500
    ''')

    with open('dat4.csv','w') as f:
      f.write(
    '''customer,item,amount,gender,buyDate,prevBuyDate
    A,apple,100,1,2013/01/04,2013/01/01
    A,milk,350,1,2013/04/04,2011/05/06
    B,orange,100,2,2012/11/11,2011/12/12
    B,orange,100,2,2013/05/30,2012/11/11
    B,pineapple,500,2,2013/04/15,2013/04/01
    B,wine,1000,2,2012/12/24,2011/12/24
    C,apple,100,2,2013/02/14,NULL
    C,orange,100,2,2013/02/14,2013/01/31
    D,orange,100,2,2011/10/28,NULL
    ''')


**基本例**

``item`` 項目の値が ``apple、orange`` に完全一致する行を選択し、
``rsl1.csv`` に出力する。
``u=oth1.csv`` を指定すれば、それ以外の行は ``oth1.csv`` に出力する。
``pineapplejuice`` は完全一致ではないので、 ``oth1.csv`` に出力される。

  .. code-block:: python
    :linenos:

    nm.mselstr(f="item", v="apple,orange", u="oth1.csv", i="dat1.csv", o="rsl1.csv").run()
    ### oth1.csv の内容
    # item,amount
    # milk,350
    # pineapplejuice,500
    # wine,1000
    ### rsl1.csv の内容
    # item,amount
    # apple,100
    # orange,100


**行の削除**

``r=True`` オプションを指定することで、例1とは逆に、商品項目の値が ``apple、orange`` に完全一致する行を削除し、
``rsl2.csv`` に出力する。

  .. code-block:: python
    :linenos:

    nm.mselstr(f="item", v="apple,orange", r=True, i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # item,amount
    # milk,350
    # pineapplejuice,500
    # wine,1000


**キー単位での選択**

``orange`` を購入したことのある顧客を選択する
``k=顧客`` を指定することで、 ``orange`` を購入したことのある顧客の他に購入した商品の行を含めて選択する。
それ以外の行は ``oth2.csv`` に出力する。

  .. code-block:: python
    :linenos:

    nm.mselstr(k="customer", f="item", v="orange", u="oth2.csv", i="dat2.csv", o="rsl3.csv").run()
    ### oth2.csv の内容
    # customer%0,item,amount
    # A,apple,100
    # A,milk,350
    ### rsl3.csv の内容
    # customer%0,item,amount
    # B,orange,100
    # B,orange,100
    # B,pineapple,500
    # B,wine,1000
    # C,apple,100
    # C,orange,100


**部分一致**

``item`` 項目の値が ``apple`` に部分一致するの行を選択し、
``rsl4.csv`` に出力する。
部分一致であるため ``pine(apple)juice`` も ``rsl4.csv`` に出力される。

  .. code-block:: python
    :linenos:

    nm.mselstr(f="item", v="apple", sub=True, i="dat1.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # item,amount
    # apple,100
    # pineapplejuice,500


**ワイド文字の部分一致**

``item`` 項目の値がワイド文字の「柿」、「桃」、「葡萄」の行を選択(部分一致)
選択項目にワイド文字が使用されている場合にバイト単位のマッチングを使用すると、
マルチバイト文字をまたいだ文字列にマッチングする可能性がある。
その為、ワイド文字が選択項目に含まれる場合は ``W=True`` オプションを使用して、
ワイド文字を使用していることを意図的に示す必要がある。

  .. code-block:: python
    :linenos:

    nm.mselstr(f="item", v="柿,桃,葡萄", sub=True, W=True, i="dat3.csv", o="rsl5.csv").run()
    ### rsl5.csv の内容
    # item,amount
    # 果物:柿,100
    # 果物:桃,250
    # 果物:葡萄,300


**商品の購入日と前回の購入日が2013年の商品データを選択**

``F=True`` オプションを指定することで、同じ商品を2013年内に購入したことのある(購入日と前回購入日両方が2013年)商品行を選択し、
``rsl6.csv`` に出力する。
それ以外の行は ``oth3.csv`` に出力する。

  .. code-block:: python
    :linenos:

    nm.mselstr(f="buyDate,prevBuyDate", F=True, sub=True, v="2013", u="oth3.csv", i="dat4.csv", o="rsl6.csv").run()
    ### oth3.csv の内容
    # customer,item,amount,gender,buyDate,prevBuyDate
    # A,milk,350,1,2013/04/04,2011/05/06
    # B,orange,100,2,2012/11/11,2011/12/12
    # B,orange,100,2,2013/05/30,2012/11/11
    # B,wine,1000,2,2012/12/24,2011/12/24
    # C,apple,100,2,2013/02/14,NULL
    # D,orange,100,2,2011/10/28,NULL
    ### rsl6.csv の内容
    # customer,item,amount,gender,buyDate,prevBuyDate
    # A,apple,100,1,2013/01/04,2013/01/01
    # B,pineapple,500,2,2013/04/15,2013/04/01
    # C,orange,100,2,2013/02/14,2013/01/31


**商品の購入日と前回の購入日が2013年の顧客データの抽出**

``k=顧客`` を指定することで、同じ商品を2013年内に購入したことのある顧客の他に購入した商品の行を含めて選択する。
それ以外の行は ``oth4.csv`` に出力する。

  .. code-block:: python
    :linenos:

    nm.mselstr(k="customer", f="buyDate,prevBuyDate", F=True, sub=True, v="2013", u="oth4.csv", i="dat4.csv", o="rsl7.csv").run()
    ### oth4.csv の内容
    # customer%0,item,amount,gender,buyDate,prevBuyDate
    # D,orange,100,2,2011/10/28,NULL
    ### rsl7.csv の内容
    # customer%0,item,amount,gender,buyDate,prevBuyDate
    # A,apple,100,1,2013/01/04,2013/01/01
    # A,milk,350,1,2013/04/04,2011/05/06
    # B,orange,100,2,2012/11/11,2011/12/12
    # B,orange,100,2,2013/05/30,2012/11/11
    # B,pineapple,500,2,2013/04/15,2013/04/01
    # B,wine,1000,2,2012/12/24,2011/12/24
    # C,apple,100,2,2013/02/14,NULL
    # C,orange,100,2,2013/02/14,2013/01/31


**2013年度の新規顧客情報の抽出**

``R=True`` オプションを指定することで、購入日、前回購入日両方が2013年,NULL(前回購入なし)の顧客情報を抽出する。
つまり2013年の新規顧客データを選択し、 ``rsl8.csv`` に出力する。
それ以外の行は  ``oth5.csv`` に出力する。

  .. code-block:: python
    :linenos:

    nm.mselstr(k="customer", f="buyDate,prevBuyDate", F=True, R=True, sub=True, v="2013,NULL", u="oth5.csv", i="dat4.csv", o="rsl8.csv").run()
    ### oth5.csv の内容
    # customer%0,item,amount,gender,buyDate,prevBuyDate
    # A,apple,100,1,2013/01/04,2013/01/01
    # A,milk,350,1,2013/04/04,2011/05/06
    # B,orange,100,2,2012/11/11,2011/12/12
    # B,orange,100,2,2013/05/30,2012/11/11
    # B,pineapple,500,2,2013/04/15,2013/04/01
    # B,wine,1000,2,2012/12/24,2011/12/24
    # D,orange,100,2,2011/10/28,NULL
    ### rsl8.csv の内容
    # customer%0,item,amount,gender,buyDate,prevBuyDate
    # C,apple,100,2,2013/02/14,NULL
    # C,orange,100,2,2013/02/14,2013/01/31


関連メソッド
''''''''''''''''''''

* :doc:`msel` : より複雑な条件で行選択を行う。
* :doc:`mcommon` : 選択対象となる文字列の数が多いときは、参照データを用意することで ``mcommon`` コマンドが使える。

