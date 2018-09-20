乱数に基づいた株価データ
=====================================
個別銘柄の4本値データとmarket indexのデータをランダムに生成するデータセットである。
データの生成にはNysolをインストールしておく必要がある。
個別銘柄のデータイメージは :numref:`randStock_equity` に示される通りで。
銘柄ID( ``id`` )、日付( ``date`` )、 始値( ``o`` )、 高値( ``h`` )、 安値( ``l`` )、 終値( ``c`` )
の6項目から構成されるデータセットである。
marketインデックスは個別銘柄の日別単純平均で計算したもので、
そのデータイメージを :numref:`randStock_index` に示している。
それぞれの項目は基本的には乱数に基づいて生成されており、その概要を :numref:`randStock_gen4` に示している。

.. csv-table:: 個別銘柄の4本値データ
  :name: randStock_equity
  :header: id,date,o,h,l,c

  1000,20180628,63427,63492,58474,61979
  1000,20180627,61341,65684,61341,63604
  1000,20180626,64200,66672,62960,64267
  1000,20180625,65361,66354,63189,65268
    : ,   :    ,  :  ,  :  ,  :  , :

.. csv-table:: marketインデックスデータ
    :name: randStock_index
    :header: date,i

    19861118,316
    19861119,314
    19861120,321
    19861121,325
        :   , :

.. list-table:: データの生成方法
  :header-rows: 1
  :name: randStock_gen4

  * - 項目名
    - 生成方法
  * - id
    - 1000〜6999の6000の銘柄を生成している。
  * - date
    - | :math:`N(m=4600,s=2000)` の正規乱数(整数)で存続日数を生成し、
      | 2018年6月29日からその日数分過去に遡った日まで生成している。
      | 期間が1000日に満たなければ1000日に修正している。
  * - o
    - | ベース価格を :math:`N(m=4600,s=2000)` の正規乱数(整数)で決め、
      | :math:`N(m=1.0,s=0.02)` の正規乱数を掛けたもの。
  * - h
    - | ベース価格に :math:`N(m=1.04,s=0.02)` の正規乱数を掛けたものをpとすると、
      | h=max(o,c,p) により設定している。
  * - l
    - | ベース価格に :math:`N(m=0.96,s=0.02)` の正規乱数を掛けたものをpとすると、
      | l=max(o,c,p) により設定している。
  * - c
    - oと同じ方法で生成。
  * - i
    - 全個別銘柄の終値 ``c`` を日別に単純平均して整数化したもの。

データ生成のスクリプトを :numref:`randStock_mkdata` に示す。
このスクリプトを実行すると、 :numref:`randStock_run` に示されるように、
6000の個別銘柄のデータが順番に生成されていき、10分程で全データが生成される。
そして、カレントディレクトリの下に、 :numref:`randStock_files` に示されるディレクトリ/ファイルが生成される。

  .. code-block:: python
    :linenos:
    :caption: 株価をランダムに生成するスクリプト
    :name: randStock_mkdata

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-/
    from datetime import datetime,timedelta
    import os
    import numpy as np
    import nysol.mcmd as nm

    def mkData(oFile):
      np.random.seed(seed=32)
      startDate=datetime(2018, 6, 29)
      delta=timedelta(days=1)

      with open(oFile,"w") as fpw:
        fpw.write("id,date,o,h,l,c\n")
        for id in range(1000,7000):
        #for id in range(1000,1002):
          period=int(np.random.normal(4600,2000))
          if period<1000:
            period=1000
          print("id",id,"period",period)
          date=startDate
          c=np.random.randint(500,100000)
          for days in range(period):
            if c<10:
              break
            c=np.random.normal(1.00,0.02)*c
            o=np.random.normal(1.00,0.02)*c
            h=np.random.normal(1.04,0.02)*c
            l=np.random.normal(0.96,0.02)*c
            hh=max(c,o,h,l)
            ll=min(c,o,h,l)
            h=hh
            l=ll
            date=date-delta
            fpw.write("%d,%s,%d,%d,%d,%d\n"%(id,date.strftime("%Y%m%d"),o,h,l,c))

    def mkIndex(oFile,iFile):
      f=None
      f <<= nm.mcat(i=iFile)
      f <<= nm.mcut(f="date,c")
      f <<= nm.mavg(k="date",f="c")
      f <<= nm.mcal(c="round(${c},1)", a="i")
      f <<= nm.mcut(f="date,i", o="%s"%oFile)
      f.run()

    os.system("mkdir -p DATA")
    mkData("./DATA/price_large.csv")
    mkIndex("./DATA/index.csv","./DATA/price_large.csv")

    nm.mselnum(f="date",c="[20171225,]",i="./DATA/price_large.csv",o="./DATA/price_middle.csv").run()
    nm.mselnum(f="date",c="[20180610,]",i="./DATA/price_middle.csv",o="./DATA/price_small.csv").run()
    nm.msep(d="./DATA/sep/${date}", p=True, i="./DATA/price_large.csv").run()

  .. code-block:: bash
    :linenos:
    :caption: 株価生成スクリプトの実行
    :name: randStock_run

    $ ./mkdata.py 
    id 1000 period 3902
    id 1001 period 6941
    id 1002 period 5896
             :
    id 6999 period ....

.. list-table:: 生成されるデータ一覧
  :header-rows: 1
  :name: randStock_files

  * - ファイル名
    - 行数(ヘッダ含む)
    - サイズ
    - 内容
  * - price_large.csv
    - 27,707,820
    - 1,032,785,399 
    - 個別銘柄別4本値データ
  * - price_middle.csv
    - 1,116,001 
    - 42,182,505 
    - price_large.csvから2017年12月25日以降のデータを選択したもの
  * - price_small.csv
    - 114,001
    - 4,297,064
    - price_large.csvから2018年6月10日以降のデータを選択したもの
  * - index.csv
    - 11,547
    - 172,763
    - marketインデックスデータ
  * - sep
    - 11,546(ファイル数)
    -  
    - price_large.csvを日別ファイルにしたもの 
