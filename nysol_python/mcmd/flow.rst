
.. index::
   single: 処理フロー

.. _処理フロー:

処理フロー
=======================

mcmdでは、単一機能に特化した80以上の処理メソッドを自由に組み合わせることで、
データ処理の複雑なフローを構築することができ、それらは並列で処理される。
このようなフロー全体のことを **データ処理フロー** もしくは単に **処理フロー** と呼ぶ。
そして処理フローを扱うオブジェクトを **データ処理フローオブジェクト**  もしくは単に **処理フローオブジェクト** と呼ぶ。
処理フローは、有向非循環グラフ( |DAG| :Directed Acyclic Graph)で表される。
DAGの節点が処理メソッドに、そして有向辺がデータの流れに対応する。
:numref:`flow_dat.png` はいずれもDAGで表された処理フローである。
(a)や(b)のように比較的単純な構造の処理フローも、(c)のような複雑な処理フローも実現可能である。
処理フローにおいて、いずれからも入力のない節点をソース節点と呼び、いずれへも出力のない節点をシンク節点と呼ぶ。
:numref:`flow_dat.png` では、ソース節点が赤枠で示され、シンク節点が青色で示されている。
ソース節点には、必ず入力データが指定されなければならす、シンク節点には必ず出力データが指定されなければならない
(後述するように、出力データの指定は省略できる)。
また、シンク節点の数により、処理フローの実行方法が異なり、
１つしか無い処理フローは ``run`` メンバーメソッドで、複数ある場合は ``runs`` クラスメソッドで実行される。
実行の詳細については「 :doc:`run` 」の節を参照されたい。

  .. figure:: figure/flow_dag.png
    :scale: 40%
    :align: center
    :name: flow_dag.png

    DAG(有向非循環グラフ)で表される処理フロー


以下では、単純な例から始め、mcmdがデータ処理フローをどのように構成していくかについて説明する。

  .. |yahoo| raw:: html

    <a href="https://en.wikipedia.org/wiki/Directed_acyclic_graph" target="_blank">DAG</a>

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

そして、このように作成された処理フローの実行は ``f.run()`` のように、処理フローオブジェクト
``f`` のメンバーメソッドである ``run`` を呼び出せばよい。

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
オブジェクト名を変えることで、これを明示的な接続へと変更することも可能である。
:numref:`flow_explicit` にその内容を示す。
フロー図は、 :numref:`flow_share.png` と同様である。
:numref:`flow_share` とは異なり、全てのメソッドに ``i=`` を指定することで
接続を明示的に指定しているのがわかるであろう。
なお、 ``run`` で実行する対象は、シンク節点である最後に登録された処理メソッドとなる。
:numref:`flow_explicit` において、 ``f4.run()`` を ``f3.run()`` にすれば、
当然、 ``mprodcut`` の結果までが出力されることになる。

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

複数の出力がある例
----------------------------
ここまでに扱ってきた例は、 :numref:`flow_dat.png` の(a),(b)のように、全て最終出力が1つの処理フローであった。
ここでは出力が複数ある処理フローについて説明する。
:numref:`flow_multio` にそのようなフローの一例を示している。
この例では、 ``mselstr`` にて、 ``customer`` 項目が ``A`` である行とそれ以外の行に分岐させ、
それぞれで ``amount`` 項目を合計するという処理を実行している。
分岐には、前述の ``redirect`` メソッドを使っている。
まず、このように複数の最終出力があるケースの実行には、 ``runs`` クラスメソッドを利用し、
引数に、最終出力を含むオブジェクトをリストで与える(例では ``nm.runs([fa,fb])`` )。
``runs`` は引数に与えられた処理フロー全てを統合し、全体の構造を識別した上で実行する。
そして、全体の処理フローに登録された処理メソッドをthreadに展開し並列処理で実行される。
ただし、同時にオープンできるthread数の上限等の制約があるので、詳細は「 :doc:`run` 」の節を参照されたい。

``runs`` の返り値は、出力されたCSVファイル名のリストである。
また、出力は ``o=`` によりCSVファイルへのみ指定可能となる。
技術的には ``run`` メソッドのように3重リスト等のデータ構造で返すことも可能ではあるが、多様な項目の出力がある場合、
出力順序など考慮すべきことが多く、現在のところCSVのみにの対応としている。

 .. code-block:: python
    :linenos:
    :caption: redirectを用いた例
    :name: flow_multio

    >>> fa=None
    >>> fb=None
    >>> fa <<= nm.mcut(f="customer,amount",i=dat)
    >>> fa <<= nm.mselstr(f="customer",v="A")
    >>> fb <<= fa.redirect("u")

    >>> fa <<= nm.msum(k="customer",f="amount",o="out1.csv")
    >>> fb <<= nm.msum(k="customer",f="amount",o="out2.csv")
                  
    >>> nm.runs([fa,fb])
    ['out1.csv', 'out2.csv']

並列処理への応用
------------------------------------
``runs`` を使うことで、 SIMD(Single Instruction Multiple Data)型の並列処理を実現することも可能である。
あらかじめ同じ項目のデータを多数用意しておき、それらのデータに同一の処理を並列計算で実行するというものである。
一例として簡単な例を :numref:`flow_meach` に示そう。
ここでは、2つのデータ ``dat1`` と ``dat2`` を１つの配列 ``dat`` に格納し、
それらのデータを並列で合計処理するというものである。
データはリストで与えなても、予め分割された多数のCSVファイルでも良い。
数十万というファイルを用意して実行することも可能である。
例では、for文で、 ``msum`` のみから構成される処理フローを ``runlist`` に登録していき、
最後に、それらの処理フローを ``nm.runs(runlist)`` にて実行している。
runsは登録された全ての処理フローを解析し、繋がりのない複数の処理フローの島を確認する。
処理フローが独立であればお互いに干渉しないとの前提で並列で実行する。
よって、それぞれの処理フローとの最終ファイル名が全て同一であったりすると(すなわち島同士で干渉していると)正しい結果は得られない。

 .. code-block:: python
    :linenos:
    :caption: redirectを用いた例
    :name: flow_meach

    import nysol.mcmd as nm
    dat1=[
    ["key","val"],
    ["a",1],
    ["a",2],
    ]

    dat2=[
    ["key","val"],
    ["b",3],
    ["b",4],
    ]
    dat=[dat1,dat2]

    runlist=[]
    for i in range(len(dat)):
      f=nm.msum(f="val",o="out%d.csv"%i)
      runlist.append(f)
    nm.runs(runlist)
    # out0.csvの内容
    # key,val
    # a,3
    # out1.csvの内容
    # key,val
    # b,7
    

途中の処理メソッドにo=を使うケース
------------------------------------
複数の出力でも、処理フローの途中の処理メソッドに ``o=CSVファイル名`` を指定するケースは
その処理メソッドはシンク節点とはならないので、 ``run`` で実行可能である。
極端な例を :numref:`flow_oooo` に示している。
内容的には意味のないことではあるが、5つの ``msetstr`` で項目を1つずつ追加していっているだけである。
最後の ``msetstr`` 以外は、 ``o=`` で出力ファイル名を指定しているが、
そこまでの途中経過がそのファイルに出力される。
最後の ``msetstr`` は ``o=`` を指定していないのでリストで出力される。

 .. code-block:: python
    :linenos:
    :caption: redirectを用いた例
    :name: flow_multio

    >>> f=None
    >>> f <<= nm.msetstr(v="out1",a="out1",i=dat,o="out1.csv")
    >>> f <<= nm.msetstr(v="out2",a="out2",o="out2.csv")
    >>> f <<= nm.msetstr(v="out3",a="out3",o="out3.csv")
    >>> f <<= nm.msetstr(v="out4",a="out4")
    >>> f.run() 
    [['A', '20180101', '5200', 'out1', 'out2', 'out3', 'out4'], ['B', '20180101', '800', 'out1', 'out2', 'out3', 'out4'], ['B', '20180112', '3500', 'out1', 'out2', 'out3', 'out4'], ['A', '20180105', '2000', 'out1', 'out2', 'out3', 'out4'], ['B', '20180107', '4000', 'out1', 'out2', 'out3', 'out4']]
    # out1.csvの内容
    # customer,date,amount,out1
    # A,20180101,5200,out1
    # B,20180101,800,out1
    # B,20180112,3500,out1
    # A,20180105,2000,out1
    # B,20180107,4000,out1
    # out2.csvの内容
    # customer,date,amount,out1,out2
    # A,20180101,5200,out1,out2
    # B,20180101,800,out1,out2
    # B,20180112,3500,out1,out2
    # A,20180105,2000,out1,out2
    # B,20180107,4000,out1,out2
    # out3.csvの内容
    # customer,date,amount,out1,out2,out3
    # A,20180101,5200,out1,out2,out3
    # B,20180101,800,out1,out2,out3
    # B,20180112,3500,out1,out2,out3
    # A,20180105,2000,out1,out2,out3
    # B,20180107,4000,out1,out2,out3


