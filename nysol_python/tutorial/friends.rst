ランク情報に基づく相関ルール分析
-----------------------------------------------

相関ルール分析は、データマイニングの分野で代表的な分析手法で、
特にルールを高速に列挙する技術は飛躍的な進展を遂げてきた。
しかしながら、パラメータの設定次第では時に大量のルールが出力され、
そこから興味深いルールを抽出するまでにユーザに多大な負担を強いることも少なくない。

この問題を解決する一つの方法として相互ランク情報に基づいたルールの抽出方法が提案されている [#f2]_ 。
Takeモジュールでは、 ``mfriends`` 及び ``mpal`` メソッドとして実装されている。
この手法の特徴は、相関ルール列挙において2アイテムルール :math:`A=>B(|A|=1,|B|=1)` のみを列挙し、
そこから :math:`A,B` 相互に関連の強いルールを選択するというものである。
:math:`A=>B` 及び :math:`B=>A` の評価指標(supportやconfidence)が、それぞれの前件部を共通としてもつルール集合の中で
ユーザが指定した k 位以内であるとき、アイテム集合 :math:`A` と :math:`B` の関連が強いと考える。

入力データと出力データ
'''''''''''''''''''''''''''''''''
:numref:`tutorial_friends_input_image` に本課題で利用する入力データ ``onlineRetail2.csv`` 
のサンプルを示している。
このファイルは、 :doc:`../../dataset/uci_onlineretail` で作成したデータセットである。
スクリプトを保存するディレクトリに保存しておく。
本分析を進めるにあたって必要となる項目は、
顧客IDの ``InvoiceNo`` と ``StockCode`` の2項目のみである。
``InvoiceNo`` はトランザクション識別のためのIDとして用い、 ``StockCode`` はアイテムとして用い、
どの商品( ``StockCode`` )同士の関連が強いかを、 一回の購入( ``InvoiceNo`` )における共起情報によって計算しようということである。

.. csv-table:: online retailデータセット
  :name: tutorial_friends_input_image
  :header: InvoiceNo,StockCode,Description,Quantity,UnitPrice,CustomerID,Country,date,time

  536365,85123A,WHITE HANGING HEART T-LIGHT HOLDER,6,2.55,17850,United Kingdom,20101201,082600
  536365,71053 ,WHITE METAL LANTERN               ,6,3.39,17850,United Kingdom,20101201,082600
  536365,84406B,CREAM CUPID HEARTS COAT HANGER    ,8,2.75,17850,United Kingdom,20101201,082600
    :   ,  :   ,               :                  ,:,  : ,  :  ,       :      ,    :   ,  :

:numref:`tutorial_friends_output_image` には出力データイメージを示している。
相互に関連の強い2つのアイテム ``item1`` と ``item2`` および、それら2アイテムのリフト値を出力する。

.. csv-table:: ランク情報に基づく相関ルールの出力イメージ
  :name: tutorial_rfm_output_image
  :header: item1,item2,lift

  15056BL,15056N,29.5141
  15056BL,20679,35.015
  15056N,20679,24.1441
    :   ,  :  ,  :


スクリプト
''''''''''''''''''''''''''
:numref:`friends_scp` は、OnlineStoreのデータから、ランク情報に基づく相関ルールを列挙するPythonコードである。
そして、グラフで視覚化した結果を :numref:`friends.png` に示す。
赤い節点が一つのアイテムを示し、エッジが関連の強い結びつきを表している。
スクリプトの実行内容については、スクリプト内にコメントとして記述している。

.. literalinclude:: /scp/nysol_python/tutorial/scp/friends.py
  :language: python
  :linenos:
  :caption: ルールの相互ランク情報に基づいた2アイテム相関ルールの列挙とその可視化を実現するスクリプト
  :name: friends_scp


.. rubric:: Footnotes

.. [#f2] 岩﨑幸子,中元政一,中原孝信,宇野毅明,羽室行信,グラフ構造による相関ルールの視覚化ツール：KIZUNA,2017年度人工知能学会(第31回),ウインクあいち,2017/5/24.

