mcmdのベンチマークテスト(FIT2018)
================================================================

`FIT2018 <https://www.ipsj.or.jp/event/fit/fit2018/>`_ に発表した原稿 [#f1]_
に掲載されたスクリプトについて説明する。
そこでは2つのスクリプトが掲載されており、1つはmcmdとpandasのベンチマークテストに関するもので、
他方は、相関ルール生成のスクリプトである。
いずれもデータとして株価4本値データを利用している。

準備
-------------------------------------
本節で扱っているPythonスクリプトの全ては `github <https://github.com/nysol/bench>`_ にupされているのでダウンロードする。
ダウンロードしたディレクトリ下 bench/fit2018/nysol_mcmd に 以下の3つのスクリプトがある。

 * mkdata.py : 株価データセット生成用スクリプト
 * bench.py : pandasとのベンチマーク用スクリプト( :numref:`mcmd_fit2018_bench` )
 * apriori.py : 原稿のfig.1に示された相関ルール分析のスクリプト( :numref:`mcmd_fit2018_fig1` )

.. code-block:: bash
  :linenos:
  :caption: ベンチマークスクリプトのダウンロード
  :name: mcmd_fit2018_download

  $ git clone https://github.com/nysol/bench.git
  $ cd bench/fit2018/nysol_mcmd
 

mcmdベンチマークテスト(vs. pandas)
-------------------------------------
nysol.mcmdの処理速度を評価する時に、Pythonにおける表構造データの加工によく利用される
`Pandas <https://pandas.pydata.org/>`_ をベンチマークとする速度比較テストを実施した。
Pandasは、表データをメモリ上で加工するための多種のメソッドを提供しており、
mcmdと同様にデータの前処理によく利用されるモジュールである。
内部では `Numpy <http://www.numpy.org/>`_ のコードも利用しており高速に動作する。
mcmdとの大きな違いは、Pandasはメモリ内に収まるデータを対象としているのに対して、
mcmdはファイル処理が基本のため、メモリサイズの制約を受けない。

利用データ
''''''''''''''''''''''''''''''''''''
利用したデータは、「 :doc:`../dataset/randStock` 」節で解説されている人工的に生成した株価4本値データであり、
上述のgitからダウンロードしたスクリプト ``mkdata.py`` を実行すれば( :numref:`mcmd_fit2018_datarun` )、
DATAディレクトリの下にデータが生成される。20〜30分ほど時間を要する。

  .. code-block:: bash
    :linenos:
    :caption: 株価生成スクリプトの実行
    :name: mcmd_fit2018_datarun

    $ ./mkdata.py 
    id 1000 period 3902
    id 1001 period 6941
    id 1002 period 5896
             :
    id 6999 period 6877

データは :numref:`mcmd_fit2018_sample` に例示されるように、
銘柄ID( ``id`` )、日付( ``date`` )、 始値( ``o`` )、 高値( ``h`` )、 安値( ``l`` )、 終値( ``c`` )
の6項目から構成される株価4本値データである。

.. csv-table:: 個別銘柄の4本値データ
  :name: mcmd_fit2018_sample
  :header: id,date,o,h,l,c

  1000,20180628,63427,63492,58474,61979
  1000,20180627,61341,65684,61341,63604
  1000,20180626,64200,66672,62960,64267
  1000,20180625,65361,66354,63189,65268
    : ,   :    ,  :  ,  :  ,  :  , :

このデータからサイズ違いの3種類のデータ(large,middle,small)を用意した。
それぞれのデータ行数とサイズは、 :numref:`mcmd_fit2018_data` に示される通りである。
名称=multiは、並列処理用にlargeデータを日別に分割したものである。
株価生成スクリプトでは固定の乱数シードを用いているので、データの内容も同一であるはずであるが、
乱数システムの違いから異なる可能性もあり、サイズを確認されたい。

.. list-table:: ベンチマークに用いたデータ一覧
  :header-rows: 1
  :name: mcmd_fit2018_data

  * - 名称
    - ファイル名
    - 行数(ヘッダ含む)
    - サイズ(byte)
    - 内容
  * - large
    - price_large.csv
    - 27,707,820
    - 1,032,785,399 
    - 個別銘柄別4本値データ
  * - middle
    - price_middle.csv
    - 1,116,001 
    - 42,182,505 
    - largeから2017/12/25以降を選択
  * - small
    - price_small.csv
    - 114,001
    - 4,297,064
    - largeから2018/6/10以降を選択
  * - multi
    - sep
    - 11,546(ファイル数)
    -  
    - largeを日別ファイルにしたもの 


処理内容
''''''''''''''''''''''''''''''''''''
処理内容は、平均計算(task="avg")、移動平均の計算(task="win")、ループ処理(task="for")の3つのである。
それぞれについて、mcmdとpandasの最速と思われる実装によりコーディングしている。
時間計測も含めたベンチマークテストのスクリプトは :numref:`mcmd_fit2018_bench` に示すとおりである。
平均値の計算においては、largeデータを日別に分割しておき、
それぞれのファイルで平均値を並列計算させる処理を参考までに実施した( 関数 ``nm1a`` )。
また、mcmdでの移動平均の結果出力において、Pythonのリストに変換せず、ファイルにそのまま出力する実験も追加している( 関数 ``nm2a`` )。
ループ処理については、pandasの提供するインデックス参照 ``iloc`` が低速であったために、
内部的にnumpyを用いた ``values`` を用いた処理(関数 ``pd3a`` )も行った。
計測結果は、 ``OUTPUT/bench/price_5.txt`` に出力される。

.. code-block:: python
  :linenos:
  :caption: ベンチマークスクリプト
  :name: mcmd_fit2018_bench

  #!/usr/bin/env python
  # -*- coding: utf-8 -*-/
  import os
  import sys
  import time
  from pprint import pprint
  from datetime import datetime
  from glob import glob

  import pandas as pd
  import math
  import nysol.mcmd as nm

  loop=5

  iPath=root="./DATA"
  oPath=root="./OUTPUT/bench"
  os.system("mkdir -p %s"%(oPath))
  oFile="%s/price_%d.txt"%(oPath,loop)

  # CSVテキストをPython内部のデータ型に変換するための項目名-データ型対応表
  # pd2,nm2,pd3,pd3aで利用している。
  t={'id':'str','date':'int','o':'float','h':'float','l':'float','c':'float'}

  # pandasによる平均計算
  def pd1(iFile):
    df = pd.read_csv(iFile)
    dfg=df.groupby("date")
    r = dfg.mean(numeric_only = True)

  # mcmdによる平均計算
  def nm1(iFile):
    r = nm.mhashavg(k="date",f="o,h,l,c",i=iFile).run()

  # mcmdによる平均計算(並列処理)
  def nm1a(iPath):
    fs=[]
    for iFile in glob("%s/*"%iPath):
      fs.append(nm.mhashavg(f="o,h,l,c",i=iFile))
    r=nm.runs(fs)

  # pandasによる移動平均
  def pd2(iFile):
    df=pd.read_csv(iFile,dtype=t,usecols=['id','date','c'])
    df_id=df.groupby("id", sort=False).apply(lambda x: x.sort_values(["date"])).reset_index(drop=True)
    r=df_id.groupby("id", sort=False).rolling(on="date",window=3, min_periods=3).mean()

  # mcmdによる移動平均(リスト出力)
  def nm2(iFile):
    f=None
    f <<= nm.mcut(f="id,date,c",i=iFile)
    f <<= nm.mwindow(k="id",wk="date:win",t=3)
    f <<= nm.mavg(k="id,win",f="c")
    f <<= nm.writelist(dtype="win:int,date:int,c:float")
    r=f.run()

  # mcmdによる移動平均(file出力)
  def nm2a(iFile):
    f=None
    f <<= nm.mcut(f="id,date,c",i=iFile)
    f <<= nm.mwindow(k="id",wk="date:win",t=3)
    f <<= nm.mavg(k="id,win",f="c",o="%s/output_nm2.csv"%oPath)
    r=f.run()

  # pandasによる行単位のloop処理
  def pd3(iFile):
    df = pd.read_csv(iFile,dtype=t)
    dfo = df.o.iloc; dfh = df.h.iloc
    dfl = df.l.iloc; dfc = df.c.iloc
    r=[0.0,0.0,0.0,0.0]
    for idx in range(df.shape[0]):
      r[0]+=dfo[idx] if not math.isnan(dfo[idx]) else 0.0
      r[1]+=dfh[idx] if not math.isnan(dfh[idx]) else 0.0
      r[2]+=dfl[idx] if not math.isnan(dfl[idx]) else 0.0
      r[3]+=dfc[idx] if not math.isnan(dfc[idx]) else 0.0

  # pandasによる行単位のloop処理(numpyのvaluesを利用)
  def pd3a(iFile):
    df = pd.read_csv(iFile,dtype=t)
    dfo = df.o.values; dfh = df.h.values
    dfl = df.l.values; dfc = df.c.values
    r=[0.0,0.0,0.0,0.0]
    for idx in range(df.shape[0]):
      r[0]+=dfo[idx] if not math.isnan(dfo[idx]) else 0.0
      r[1]+=dfh[idx] if not math.isnan(dfh[idx]) else 0.0
      r[2]+=dfl[idx] if not math.isnan(dfl[idx]) else 0.0
      r[3]+=dfc[idx] if not math.isnan(dfc[idx]) else 0.0

  # mcmdによる行単位のloop処理
  def nm3(iFile):
    r=[0.0,0.0,0.0,0.0]
    for line in nm.mnullto(f="*",v=0,i=iFile).convtype(t):
      r[0]+= line[2];r[1]+= line[3]
      r[2]+= line[4];r[3]+= line[5]
  
  # entry point
  sec={}
  mean={}
  params=[]
  small ="%s/price_small.csv"%iPath
  middle="%s/price_middle.csv"%iPath
  large ="%s/price_large.csv"%iPath

  params.append(["pd1" ,small])
  params.append(["nm1" ,small])
  params.append(["pd2" ,small])
  params.append(["nm2" ,small])
  params.append(["nm2a",small])
  params.append(["pd3" ,small])
  params.append(["pd3a",small])
  params.append(["nm3" ,small])
  params.append(["pd1" ,middle])
  params.append(["nm1" ,middle])
  params.append(["pd2" ,middle])
  params.append(["nm2" ,middle])
  params.append(["nm2a",middle])
  params.append(["pd3" ,middle])
  params.append(["pd3a",middle])
  params.append(["nm3" ,middle])

  params.append(["pd1" ,large])
  params.append(["nm1" ,large])
  params.append(["nm1a","%s/sep"%iPath])
  params.append(["pd2" ,large])
  params.append(["nm2" ,large])
  params.append(["nm2a",large])
  params.append(["pd3" ,large])
  params.append(["pd3a",large])
  params.append(["nm3" ,large])

  for param in params:
    func=param[0]
    iFile=param[1]
    name="%s_%s"%(func,iFile)
    print("START:",name)
    sec[name]=[]
    for i in range(loop):
      st=time.time()
      eval(func+'("%s")'%iFile)
      sec[name].append(time.time()-st)
    mean[name]=0
    for i in range(loop):
      mean[name]+=sec[name][i]
    mean[name]/=loop

  print("write to: ",oFile)
  with open(oFile, "w") as file:
    pprint(sys.argv[0], stream=file)
    pprint(loop, stream=file)
    pprint(sec, stream=file)
    pprint(mean, stream=file)

結果
''''''''''''''''''''''''''''''''''''
出力結果をまとめたものを :numref:`mcmd_fit2018_bench_result` に示している。
defは :numref:`mcmd_fit2018_bench` の関数名を表す。
small,mid,largeは :numref:`mcmd_fit2018_data` に示したサイズ別データセットの名称である。

.. csv-table:: ベンチマークの結果(単位:秒)。
  :name: mcmd_fit2018_bench_result
  :header: task,program,def,small,mid,large

  avg ,pandas        ,pd1 ,0.130,  1.28,29.18
  avg ,mcmd          ,nm1 ,0.036,  0.33, 7.39
  avg ,mcmd(multi)   ,nm1a,     ,      , 5.38
  win ,pandas        ,pd2 ,16.91, 19.22,74.88
  win ,mcmd          ,nm2 , 0.27,  2.54,63.94
  win ,mcmd(file)    ,nm2a, 0.19,  1.63,41.87
  for ,pandas        ,pd3 ,18.72,174.54,
  for ,pandas(values),pd3a, 0.35,  3.10,73.42
  for ,mcmd          ,nm3 , 0.27,  2.73,60.43

ベンチマークテストを実施した計算環境は以下の通りである。

 * PC: MacPro(2013)
 * CPU: 2.7GHz 12-Core Intel Xeon E5
 * memory: 64GB
 * hdd: USB3 HDD


.. note::

  ここ以降の内容は、近い将来「 :doc:`../tutorial/index` 」の節に移動します。


高収益率による銘柄の共起分析
---------------------------------

:numref:`mcmd_fit2018_fig1` は原稿の図1に掲載したスクリプトである
(原稿にはタイポがいくつかあり修正している)。
このスクリプトは、日をトランザクションにして、収益率が高くなる時に共起しやすい銘柄について
2アイテムの相関ルール分析を行ったものである。
内容の詳細については、原稿を参考にしてもらいたい。

.. code-block:: python
  :linenos:
  :caption: 株価をランダムに生成するスクリプト
  :name: mcmd_fit2018_fig1

  import nysol.mcmd as nm
  tra=None
  tra <<= nm.mcut(f="id,date,c",i=iFile)
  tra <<= nm.mjoin(k="date",m=topix,f="i")
  tra <<= nm.mslide(k="id",s="date",f="date:date2,c:c2,i:i2")
  tra <<= nm.mcal(c="${c2}/${c}-${i2}/${i}",a="ret")
  tra <<= nm.mselnum(f="ret",c="[0.05,0.1]")
  tra <<= nm.mcut(f="id,date2:date,ret")
  freq=None
  freq <<= nm.mcut(f="id",i=tra)
  freq <<= nm.mcount(k="id",a="freq")
  freq <<= nm.mselnum(f="freq",c="[5,]")
  total=None
  total <<= nm.mcut(f="date",i=tra)
  total <<= nm.muniq(k="date")
  total <<= nm.mcount(a="total")
  coFreq=None
  coFreq <<= nm.mcut(f="date,id",i=tra)
  coFreq <<= nm.mcommon(k="id",m=freq)
  coFreq <<= nm.mcombi(k="date",n=2,f="id",a="id1,id2")
  coFreq <<= nm.mcut(f="id1,id2")
  coFreq <<= nm.mfsort(f="id1,id2")
  coFreq <<= nm.mcount(k="id1,id2",a="coFreq")
  coFreq <<= nm.mjoin(k="id1",m=freq,K="id",f="freq:freq1")
  coFreq <<= nm.mjoin(k="id2",m=freq,K="id",f="freq:freq2")
  coFreq <<= nm.mproduct(m=total,f="total")
  coFreq <<= nm.mcal(c="(${coFreq}*${total})/(${freq1}*${freq2})",a="lift")
  coFreq <<= nm.msel(c="${lift}>10 && ${coFreq}>6",o="result.csv")
  coFreq.run(msg="on")
  # result.csvの内容
  # id1,id2%0,coFreq,freq1,freq2,total,lift
  # 1075,3669,7,126,123,9127,4.122402891
  # 3519,3669,8,96,123,9127,6.183604336
  # 1921,3669,7,94,123,9127,5.525774088
  #   : ,  : ,:, :, :,   : ,     :
  # 4729,6609,8,112,129,9127,5.053709856


.. rubric:: Footnotes

.. [#f1] 中元政一,羽室行信,「NYSOL: Pythonにおける大規模データ前処理支援ツール」FIT2018:第17回情報科学技術フォーラム,2018/9/20,福岡工業大学.

