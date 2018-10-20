
.. _はじめよう:

はじめよう
==================
それでは、簡単な例から始めよう。
nysol_python のインストールができたら、pythonを起動して、例に従って入力しながら動作を確認していこう。

  .. note::  
   tty(ターミナル端末）からインタプリタモード(対話モード）で、pytonを起動した場合、コマンド入力を促すプライマリプロンプト(>>>)や
   、継続行にセカンダリプロンプト(デフォルトでは...)が表示されるが、このサイトの例では省略している。
   また実行結果をコメント行(#で始まる行)として示している。

それでは、:numref:`hello_intable` に示される顧客の日別購買金額データを用いて簡単な実行例をみていこう。
mcmdは下記に示すような表構造データを扱う。
現在のところは2重リストもしくはCSVのいずれかのフォーマットにより与える。

  .. csv-table:: 入力データ例:mcmdが扱う表構造データ
    :name: hello_intable

    customer,date,amount
    A,20180101,5200
    B,20180101,800
    B,20180102,3500
    A,20180105,2000
    B,20180107,4000
 
まずは、mcmdモジュールをimportし、上記の表を二重リストとして ``dat`` 変数に格納してみよう( :numref:`hello_indat` )。

  .. code-block:: python
    :linenos:
    :caption: mcmdのインポートと入力データの設定
    :name: hello_indat

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

このデータから、顧客別に合計金額を合計する処理を以下に示す。
まずは、必要となる顧客と金額の2項目(``customer`` , ``amount`` )のみを切り出してみよう(:numref:`hello_cutCustAmount` )。
``mcut`` がその機能を実現するメソッドで、入力データとして ``dat`` 変数を指定している( ``i=`` )。
そして続けて ``run`` メソッドを指定することで ``mcut`` の処理が実行される。
mcmdでは、このような単一の機能を持ったメソッドを80以上提供しており、
それらのメソッドを特に **処理メソッド** と呼ぶ。

  .. code-block:: python
    :linenos:
    :caption: 必要な項目の切り出し処理
    :name: hello_cutCustAmount

    nm.mcut(f="customer,amount",i=dat).run()
    #[['A', '5200'], ['B', '800'], ['B', '3500'], ['A', '2000'], ['B', '4000']]

切り出したデータについて、顧客別に金額を合計する処理は ``msum`` メソッドにより実現できる。
以下では、``mcut`` に続けて、msumを ``.`` (ドット)でつなげて指定しているが、
この書き方により、``mcut`` の出力結果が、``msum`` の入力として用いられることになる。
それぞれのメソッドはスレッド上で動作し、データはパイプ(FIFOキュー)によって接続されている [#f1]_。
詳細は「 :doc:`flow` 」の節を参照されたい。

  .. code-block:: python
    :linenos:
    :caption: 顧客別金額合計の処理
    :name: hello_custAmount

    nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount").run()
    #[['A', '7200'], ['B', '8300']]

なお、上述の2つの実行結果のリストからは項目名が省かれているがこれは仕様である [#f2]_。
mcmdでは、:numref:`hello_custAmount` の例のようにメソッドを連結して段階的に処理を行うが、
メソッド間を流れるデータはPythonリストではなく、テキストのバイトストリームである。
そして、最後のメソッド(:numref:`hello_custAmount` の例では ``msum`` )に明示的に出力ファイル ``o=`` を指定しなければ、
項目名ヘッダを省いたリストが出力されるようになっている。

組み合わせるmcmdメソッドの数が増えると、それらのメソッドをドットで繋げていくと見にくくなる。
また、途中にコメントや条件文を書いたりすることもできない。
そこで、同じ機能を ``<<=`` 演算子を使うことで、これらの問題を解決することができる。
:numref:`hello_ope` は、 :numref:`hello_custAmount` と同様の処理を ``<<=`` 演算子で書き直したものである。
変数 ``f`` に次々と処理内容を追加登録し、最後に ``run`` メソッドで実行している。

  .. code-block:: python
    :linenos:
    :caption: ``<<=`` 演算子を利用した例
    :name: hello_ope

    f=None
    f <<= nm.mcut(f="customer,amount",i=dat)
    f <<= nm.msum(k="customer",f="amount")
    f.run()
    #[['A', '7200'], ['B', '8300']]

複数のメソッドをより複雑に連結することも可能であり、詳細は「 :doc:`flow` 」の節を参照されたい。

最後に、表構造のデータをpythonのネイティブコードを使って処理する例を紹介する。
mcmdには、上記で紹介したようなメソッドの組み合わせで多様な処理を実現するが、
それだけでは実現困難な処理もでてくる。
そのようなときは、mcmdに組み込まれている、イテレータを用いればよい。
mcmdで処理した結果をシームレスにイテレータに接続することが可能である。
:numref:`hello_iterator` にその例を示す。
これは :numref:`hello_ope` の結果を、( ``run`` せずに) ``for in`` のイテレータに接続したものである。
このイテレータは一行ずつ読み込むイテレータで、
``amount`` 項目を100で割った結果を出力している。
``for in`` イテレータでは、データは全て文字列として出力される。
mcmdには、 ``for in`` 以外にもいくつかのイテレータが用意されており、
データ型の指定や、コンテナ型の指定、さらにはブロック単位のイテレータなど、
多様な機能が用意されている。詳細は「 :doc:`iterator` 」の節を参照されたい。

  .. code-block:: python
    :linenos:
    :caption: イテレータを利用した例
    :name: hello_iterator

    f=None
    f <<= nm.mcut(f="customer,amount",i=dat)
    f <<= nm.msum(k="customer",f="amount")
    for line in f:
       print(line[0],int(line[1])/100)
    #A 72.0
    #B 83.0

.. [#f1] 正確には、処理フローオブジェクトに処理メソッド(mcutやmsum)を登録していっているだけで、最後のrunメソッドが登録された処理フローを実行している。詳しくは「 :doc:`処理フロー<flow>` 」の節を参照されたい。

.. [#f2] 項目名を1要素目に出力したければ ``writelist`` 関数を用いれば実現することができる。本例では、 ``nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount").writelist(header=True).run()`` と書けばよい。

