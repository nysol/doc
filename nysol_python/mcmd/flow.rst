
.. index::
   single: 処理フロー

.. _処理フロー:

処理フロー
=======================

mcmdでは、単一機能に特化した80以上のメソッドを自由に組み合わせることで、
データ処理の複雑なフローを構築することができ、それらは並列で処理される。
このようなフロー全体のことを **データ処理フロー** もしくは単に **処理フロー** と呼ぶ。
そして処理フローを扱うオブジェクトを **データ処理フローオブジェクト**  もしくは単に **処理フローオブジェクト** と呼ぶ。
以下では、単純な例から始め、mcmdがデータ処理フローをどのように構成していくかについて説明する。

.. _処理フロー_基本例:

暗黙の接続
---------------
単純なデータ処理フローから始めよう。
図 :numref:`flow_base` は、「 :doc:`はじめよう<hello>` 」節の :numref:`hello_ope` に示したフローである。
2重リストに格納された3項目5行のデータを入力データとして、
``mcut`` メソッドにより、 ``customer`` と ``amount`` 項目のみを切り出し、
``amount`` 項目を合計するというものである。

  .. code-block:: python
    :linenos:
    :caption: 処理フローの基本例
    :name: flow_base

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]
    >>> f=None
    >>> f <<= nm.mcut(f="customer,amount",i=dat)
    >>> f <<= nm.msum(k="customer",f="amount")
    >>> f.run()
    [['A', '7200'], ['B', '8300']]

.. index::
   single: 暗黙の接続

``<<=`` 演算子により、左辺の処理フローオブジェクトに右辺のメソッドが追加登録される。
左辺が ``None`` の場合は、新規に処理フローオブジェクトが生成され、メソッドが登録される。
登録順は重要で、明示的な接続関係(後述)を設定しなければ、前のメソッドの出力データが次のメソッドの入力データとして接続される。
このような接続方式を **暗黙の接続** と呼ぶ。
:numref:`flow_base` では、``mcut`` の出力が ``msum`` の入力として暗黙に接続される。

また、``drawModelD3`` メソッドを利用すれば処理フロー全体を視覚化することができる( :numref:`flow_drawModel` )。
結果は :numref:`flow_drawModelPNG` に示されるように、メソッドの接続関係を有向グラフで描画される。
円のノードでメソッドを、四角のノードでデータを表している。
また、メソッド名が薄字のものは、mcmdが実行時に裏で自動追加した処理を示しているが、ここでは無視して考えて問題ない。
処理の自動追加については「 :doc:`autoadd` 」の節を参照されたい。


  .. code-block:: python
    :linenos:
    :caption: 処理フローの視覚化
    :name: flow_drawModel

    nm.drawModelsD3(f,"cust_amount.html") 

  .. figure:: figure/flowChart.png
    :scale: 40%
    :align: center
    :name: flow_drawModelPNG
    :target: ../_static/cust_amount.html

    視覚化された処理フロー

.. _データストリームの明示的接続方法:

明示的な接続
---------------------------------
処理フローオブジェクトにおけるデータの流れを明示的に接続する方法はいくつかある。
mcmdが提供する処理メソッドの多くは、入出力のための共通したパラメータを持っている。
``i=`` および ``m=`` は入力データを指定するパラメータで、
``o=`` および ``u=`` は出力データを指定するパラメータである。
データストリームの接続は、入力のパラメータに処理フローオブジェクトを指定することで実現する。
いくつかの例を見てみよう。

項目結合の例
'''''''''''''''''
:numref:`flow_share` は顧客別( ``A`` と ``B`` )の合計金額を求め、それぞれの構成比を求める処理である。
1行目のフローオブジェクト ``f`` を2行目の ``msum`` の入力データに指定し( ``i=f`` )、
その処理内容を ``total`` という別の処理フローオブジェクトとして設定している。
``total`` オブジェクトを4行目の ``mproduct`` の参照データに指定することで( ``m=total`` )、
合計金額項目 ``totalAmount`` が結合される。
3行目の ``msum`` の入力データは、同じフローオブジェクト ``f`` に対する追加になるため、
1行目の ``mcut`` の出力がそのまま接続される。
:numref:`flow_share.png` には、それらの接続関係が視覚化されている。
ここでも :doc:`自動追加<autoadd>` されたメソッドがあるが、それらは無視して構わない。

  .. code-block:: python
    :linenos:
    :caption: 顧客別構成比の計算：項目の結合によるデータストリームの接続
    :name: flow_share

    >>> f=None
    >>> f<<= nm.mcut(f="customer,amount",i=dat)
    >>> total=nm.msum(f="amount:totalAmount",i=f)
    >>> f <<= nm.msum(k="customer", f="amount")
    >>> f <<= nm.mproduct(m=total, f="totalAmount")
    >>> f <<= nm.mcal(c='${amount}/${totalAmount}', a="share")
    >>> f.drawModelD3("flow_share.html")
    >>> f.run()
    [['A', '7200', '15500', '0.464516129'], ['B', '8300', '15500', '0.535483871']]

  .. figure:: figure/flow_share.png
    :scale: 40%
    :align: center
    :name: flow_share.png
    :target: ../_static/flow_share.html

    項目の結合の処理フロー

この例では、処理フローオブジェクト ``f`` における接続の多くは暗黙の接続である。
オブジェクト名を買えることで、これを明示的な接続へと変更することも可能である。
:numref:`flow_explicit` にその内容を示す。
フロー図は、 :numref:`flow_share.png` と同様である。
:numref:`flow_share` とは異なり、全てのメソッドに ``i=`` を指定することで
接続を明示的に指定しているのがわかるであろう。

  .. code-block:: python
    :linenos:
    :caption: 顧客別構成比の計算：項目の結合によるデータストリームの接続
    :name: flow_explicit

    >>> f1 = nm.mcut(f="customer,amount", i=dat)
    >>> total=nm.msum(f="amount:totalAmount", i=f1)
    >>> f2 = nm.msum(k="customer", f="amount", i=f1)
    >>> f3 = nm.mproduct(m=total, f="totalAmount", i=f2)
    >>> f4 = nm.mcal(c='${amount}/${totalAmount}', a="share", i=f3)
    >>> f4.run()
    [['A', '7200', '15500', '0.464516129'], ['B', '8300', '15500', '0.535483871']]

レコード併合の例
'''''''''''''''''
データを種別で分割し、一方にはある処理を、他方には別の処理を付した上で両者を併合するといった処理はよく用いられる。
:numref:`flow_merge` はそのような処理を例示したフローである。
``msestr`` を2回使い、顧客 ``A`` と顧客 ``B`` を分割し、 ``B`` のみ ``amount`` が1000以上を選択し、
分割した2つのデータを ``msum`` メソッドの ``i=`` パラメータ指定にて併合している。
入力パラメータ ``i=`` の指定は ``[custA,custB]`` のように、処理フローオブジェクトのリストでなければならない。


  .. code-block:: python
    :linenos:
    :caption: 顧客別計算結果の併合の例
    :name: flow_merge

    >>> f1=None
    >>> f1 <<= nm.mcut(f="customer,amount",i=dat)
    >>> custA   = nm.mselstr(f="customer",v="A",i=f1)
    >>> custB   = nm.mselstr(f="customer",v="B",i=f1)
    >>> custB <<= nm.mselnum(f="amount",c="[1000,]")
    >>> f2=None
    >>> f2 <<= nm.msum(k="customer", f="amount", i=[custA,custB])
    >>> f2.drawModelD3("flow_merge.html")
    >>> f2.run()
    [['A', '7200'], ['B', '7500']]

  .. figure:: figure/flow_merge.png
    :scale: 40%
    :align: center
    :name: flow_merge.png
    :target: ../_static/flow_merge.html

    レコード併合の処理フロー


.. index::
   single: redirect

redirect
----------------------------
:numref:`flow_merge` では、``mselstr`` を2回用いているために、``f1`` の出力を2度読み込んでいることになり効率が悪い。
``mselstr`` には条件にマッチした行の出力先を ``o=`` で指定する一方で、
アンマッチの行を ``u=`` で出力することができる。
この機能を使えば、 ``mselstr`` の実行は1回で済むことになる。
``o=`` の出力は次に登録されるメソッドの入力となるが、 ``u=`` を次のメソッドに接続するにはどうすればよいであろうか？
それを実現するのが、 ``redirect`` メソッドである。
:numref:`flow_redirect` は、:numref:`flow_merge` を ``redirect`` を用いて書き直したものである。
違いは4行目だけで、 ``custA.redirect("u")`` によって、 ``custA`` に登録された最後のメソッド( ``mselstr`` )の ``u=`` パラメータを 
``custB`` の処理フローオブジェクトに接続することになる。
:numref:`flow_redirect.png` を見てもわかるように、 ``mselstr`` は1回のみ実行されており、 :numref:`flow_merge` より効率的に動作する。

  .. code-block:: python
    :linenos:
    :caption: redirectを用いた例
    :name: flow_redirect

    >>> f1=None
    >>> f1 <<= nm.mcut(f="customer,amount",i=dat)
    >>> custA  = nm.mselstr(f="customer",v="A",i=f1)
    >>> custB  = custA.redirect("u")
    >>> custB <<= nm.mselnum(f="amount",c="[1000,]")
    >>> f2=None
    >>> f2 <<= nm.msum(k="customer", f="amount", i=[custA,custB])
    >>> f2.drawModelD3("flow_redirect.html")
    >>> f2.run()
    [['A', '7200'], ['B', '7500']]

  .. figure:: figure/flow_redirect.png
    :scale: 40%
    :align: center
    :name: flow_redirect.png
    :target: ../_static/flow_redirect.html

    redirectを用いた例

