2アイテム相関ルール
========================
本節では「ビールを買えばおむつも購入する」で有名な相関ルールの列挙をmcmdで行う方法について解説する。
相関ルールとは、どのような商品が同時購入しやすいかについてのルールを列挙する手法である。
ルールは通常、「A=>B」のように表され、商品AとBに強い関係があることを表している。
そして、関係の強さを測る指標が色々と提案されており、特に支持度(support)、確信度(confidence)、リフト値(lift)がよく用いられる。
本節では、2つのアイテムに限定して、相関ルールを列挙する方法について紹介する。
デーは、online storeのデータ・セットを用いる。
データセットの利用方法については、 :doc:`../../dataset/uci_onlineretail` を参照されたい。

出力イメージ
----------------------------------------
:numref:`tutorial_as_output_image` にこの課題での出力イメージを示す。
左の2項目で相関ルール「 ``item1`` => ``item2`` 」を示している。
``freq`` は ``item1`` と ``item2`` の共起件数を表している。
共起件数とは、2つのアイテムを共に含むトランザクションの何件である。
ここで、トランザクションの定義は分析者に依存することに注意されたい。
本ケースでは、例えば、一回の注文(同じ請求番号)をトランザクションとも定義できるし、
一人の顧客をトランザクションの単位とすることも可能である。
また、一人の顧客の一ヶ月の買い物をトランザクションと定義する人もいるかも知れない。
ここでは、顧客をトランザクションの単位とすることにしよう。
このことにより、一回の注文時の組み合わせではなく、
顧客が、どのような商品を購入してきたかに関するルールを抽出できるようになる。

``freq1`` ( ``freq2`` )は、 ``item1`` ( ``item2`` ) を含むトランザクションの件数である。
``total`` は、総トランザクション件数(総顧客数)である。

  .. csv-table:: 入力データ例:mcmdが扱う表構造データ
    :name: intable
    :header: item1,item2,freq,freq1,freq2,total,support,confidence,lift

    15034,10002,2,95,49,19296,0.0001036484245,0.02105263158,8.290440387
    22414,10002,1,72,49,19296,5.182421227e-05,0.01388888889,5.469387755
    35961,10002,3,154,49,19296,0.0001554726368,0.01948051948,7.671349059
      :  ,  :  ,:, : , :,  :  ,      :        ,  :          , :

``support`` ``confidence`` ``lift`` はルールの興味深さを定義する指標で、
相関ルール「 ``item1`` => ``item2`` 」に関するそれぞれの定義式を以下に示す。

.. math::

   support(item1=>item2) = \frac{freq}{total}

   confidence(item1=>item2) = \frac{freq}{freq1}

   lift(item1=>item2) = \frac{freq \cdot total}{freq1 \cdot freq2}

supportとは、 ``item1`` と ``item2`` の共起確率を表しており、
confidenceは、 ``item1`` の出現を条件とした時の ``item2`` の出現確率を表している。
liftは、 定義式では分かりにくいが、 ``item1`` と ``item2`` それぞれの出現確率から計算される ``item1`` と ``item2`` の期待共起確率に対する
実際の共起確率( ``support`` )の比である。
support と liftは、定義式よりルールに方向性はない。
すなわち :math:`support(item1=>item2) = support(item2=>item1)`  であり、
:math:`lift(item1=>item2) = lift(item2=>item1)` である。
一方で、confidenceには方向性があり、 :math:`confidence(item1=>item2) \ne confidence(item2=>item1)` である。

さてそれでは、以上9項目からなるルール一覧を作成してみよう。

トータルトランザクション数
-------------------------------------
項目を一つずつ作成していこう。
まずは、トランザクションの総件数 ``total`` を計算する。
:numref:``tutorial_as_total`` にそのスクリプトを示す。

  .. code-block:: python
    :linenos:
    :caption: トランザクション件数の計算
    :name: tutorial_as_totauci_online_download

    >>> import nysol.mcmd as nm
    >>> total=None
    total <<= nm.mcut(f="Cusotomer", i="onlineRetail2.csv")
    total <<= nm.muniq(k="Cusotomer")
    total <<= nm.mcount(a="total")
    total.run()

他のパッケージ同様、pipを利用してインストールできる。
PyPiにおけるnysolのページは  |pypi_nysol| を参照されたい。

  .. code-block:: bash
    :linenos:
    :caption: nysolのインストール
    :name: install_pip

    $ pip install nysol


  .. |pypi_nysol| raw:: html

    <a href="https://test.pypi.org/project/nysol" target="_blank">https://test.pypi.org/project/nysol</a>

オフラインインストール
-------------------------------------
ネット環境がない環境では、あらかじめgitHubよりソース一式をダウンロードしておき、以下の手順でインストールを行う。

  .. code-block:: bash
    :linenos:
    :caption: nysolのダウンロードとオフラインインストール
    :name: custAmount

    # 以下、オンライン環境でソース一式をgitHubよりダウンロード(clone)しておく。
    $ git clone https://github.com/nysol/nysol_python.git
    # nysol_pythonディレクトリをオフライン環境に移し、以下でインストールする。
    $ cd nysol_python
    $ pip install .

