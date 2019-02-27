焼き肉購買データ
=============================

|ofs| より提供を受けた焼肉店の販売データの利用方法について解説する。
焼肉店は以下のような特徴を持つ店舗である。

* 高級住宅地が近く電車の駅と国道に挟まれた好立地に位置する店舗。
* 生肉をオーダーし、客自身がテーブルで焼くスタイル。
* ワインの種類が豊富である。
* 内装は落ち着いた雰囲気でかつ照明も暗めで「おしゃれ感」を演出している。
* 昼食は定食を中心とした別メニューを用意している

データは :numref:`yakiniku_fields` に示される7項目から構成されるCSVファイルで提供されている。
データの期間は、2007年7月1日〜2008年10月14日の1年3ヶ月強である。

.. |ofs| raw:: html

  <a href="https://okayamafs.com/" target="_blank">岡山フードサービス株式会社</a>

.. csv-table:: 焼き肉データの項目一覧
    :name: yakiniku_fields
    :header: 項目名,      型,    内容

    date     ,文字列,注文日付でyyyymmddの8桁固定長。470営業日。
    time     ,文字列,注文時刻でhhmmssの6桁固定長。同じレシートの中で異なる時刻あり。
    receipt  ,文字列,レシート番号で、この番号が同じであれば同じテーブルでの注文である。96789枚。
    itemID   ,文字列,商品を唯一識別するID。 793種。
    item     ,文字列,商品名
    price    ,整数  ,単価
    quantity ,整数  ,注文数量

ダウンロード
------------------

CSVファイルは商品名が日本語と英語の2つのファイルを用意している。
商品名以外は全て共通で、 ``itemID`` が同じであれば、対応する商品も同じである。
また項目名も :numref:`yakiniku_fields` に示した内容で全て共通である。
以下のリンクよりダウンロードできる。

* :download:`yakiniku_jp.csv(日本語:utf-8)<../_static/yakiniku_jp.csv>` (5,698,013 byte)
* :download:`yakiniku_en.csv(英語)<../_static/yakiniku_en.csv>` (6,201,232 byte)

データの内容は :numref:`yakiniku_csv` に示すとおりである。

  .. code-block:: bash
    :linenos:
    :caption: 焼き肉購買データの内容
    :name: yakiniku_csv

    $ head yakiniku_jp.csv 
    date,time,receipt,itemID,item,price,quantity
    20070701,115200,5589,107,和牛焼肉弁当,1240,1
    20070701,122800,5594,102,冷麺定食,1130,2
    20070701,120800,5595,105,オリジナル３品盛り合わせ,880,1
    20070701,120800,5595,107,和牛焼肉弁当,1240,1
    20070701,122600,5596,107,和牛焼肉弁当,1240,1
    20070701,135400,5601,103,石焼ビビンバ膳,1130,1
    20070701,115600,5598,201,いわて和牛しゃぶしゃぶ膳,1720,2
    20070701,112300,5588,302,焼肉ヘルシーセット,1410,1
    20070701,113200,5590,305,特上焼肉厚切りセット,2470,2

    $ head yakiniku_en.csv 
    date,time,receipt,itemID,item,price,quantity
    20070701,115200,5589,107,Japanese grilled beef lunch box,1240,1
    20070701,122800,5594,102,Buckwheat noodles in a cold beef broth set,1130,2
    20070701,120800,5595,105,Three kind of assorted house special dishes ,880,1
    20070701,120800,5595,107,Japanese grilled beef lunch box,1240,1
    20070701,122600,5596,107,Japanese grilled beef lunch box,1240,1
    20070701,135400,5601,103,Stone roasted Bibim Bab set meal,1130,1
    20070701,115600,5598,201,IWATE beef Shabu‐shabu set meal,1720,2
    20070701,112300,5588,302,Low-fat BBQ set,1410,1
    20070701,113200,5590,305,Super deluxe thick‐sliced BBQ set,2470,2

.. * このデータセットを用いたチュートリアルは :doc:`こちら<../tutorial/index>`


