mcmdのメソッド比較
================================================================

nysol.mcmdが提供する70以上の処理メソッドの中から、主な処理メソッドについての処理速度の実験を行う。

準備
-------------------------------------
本節で扱っているPythonスクリプトの全ては `github <https://github.com/nysol/bench>`_ よりダウンロードできる
( :numref:`methods_fit2018_download` )。
ダウンロードしたディレクトリ下 bench/methods に 以下の2つのスクリプトがある。

 * mkdata.py : 集計キーや数値項目を備えたランダムなデータを生成する
 * bench.py : ベンチマーク用スクリプト( :numref:`mcmd_fit2018_bench` )


.. code-block:: bash
  :linenos:
  :caption: ベンチマークスクリプトのダウンロード
  :name: methods_fit2018_download

  $ git clone https://github.com/nysol/bench.git
  $ cd bench/methods
 
利用データ
------------------------------------
利用したデータは、「 :doc:`../dataset/rand` 」節で解説されている人工的に生成したデータであり、
上述のgitからダウンロードしたスクリプト mkdata.py を実行すれば
./DATA ディレクトリが作成され、
そこに :numref:`bench_methods_data` に示される異なる3つのサイズのデータが生成される。
処理には10分ほどかかる。
データの詳細については、「 :doc:`../dataset/rand` 」節を参照されたい。

.. list-table:: ベンチマークに用いたデータ一覧
  :header-rows: 1
  :name: bench_methods_data

  * - 名称
    - ファイル名
    - 行数(ヘッダ除く)
    - サイズ
  * - small
    - 10000.csv
    - 10000
    - 665 KB
  * - middle
    - 1000000.csv
    - 1000000
    - 68.5 MB
  * - large
    - 100000000.csv
    - 100000000
    - 7.05 GB

検証内容
------------------------------------
mcmdの処理メソッドの速度を評価するために、最も処理速度が速いであろう mcut 処理メソッドをベンチマークに、
他のメソッドの相対的実行時間を計測した。
個々の処理メソッドの関数を bench.py から抜粋したものを :numref:`bench_methods_code_part` に示している。
それぞれの関数では、入力ファイル名 ``iFile`` と 実行回数 ``loop`` をパラメータとしてとる。
入力ファイルは、 :numref:`bench_methods_data` に示される3種のCSVデータで、
実行回数は5回固定である。
時間の計測は、実行に要した実時間を計測し、その平均と標準偏差を計算している。
なお、出力は基本的にカレントディレクトリにファイルとして書き出している。

``msum_key3`` 関数は、key3項目を集計キーにして全ての数値項目を合計する処理である。
このように関数の名前にキー項目など主だった特徴となるキーワードを用いている。
``msum_key3_presort`` 関数では、キー項目を事前に並べ替えた後で ``msum`` を実行している。
このことによって、裏で自動的に実行される並べ替えを省いて純粋なmsumの実行時間を計測できることになる。

.. code-block:: python
  :linenos:
  :caption: ベンチマークスクリプトのダウンロード
  :name: bench_methods_code_part

  def mcut(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.mcut(f="id,key1,key2,key3,int1,int2,float1,float2,date,time",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec

  def msum_key3(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.msum(k="key3",f="int1,int2,float1,float2",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec
  
  def msum_key3_presort(iFile,loop):
    nm.msortf(f="key3",i=iFile,o="sorted").run()
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.msum(k="key3",f="int1,int2,float1,float2",i="sorted",o="oFile").run()
      sec.append(time.time()-st)
    return sec
  


実験結果
-------------------------------------

:numref:`bench_methods_results` に、mcut処理メソッドをベンチマークにした相対時間を示す。
msum_key3 のlargeで6.2となっているが、mcutのlargeを処理した時間に比べて6.2倍の時間を要したことを意味している。
個々の処理内容の詳細については bench.py を直接参照されたい。
また、:numref:`bench_methods_results_time`  に実時間の平均と標準偏差を示す。

.. csv-table:: 実験結果(対mcutの実行時間比)
  :name: bench_methods_results
  :header: method,small(1万行:665KB),middle(100万行:68.5MB),large(1億行:7.05GB)

  mcut,1,1,1
  msum_key3,21.9,4.9,6.2
  msum_key3_presort,3.7,1.5,1.1
  mhashsum_key3,7.4,2.6,1.8
  msortf_key3,4.8,2.2,4.6
  msortf_float2,20.8,6.1,12.9

.. csv-table:: 実験結果(実時間秒数:mean(sd))
  :name: bench_methods_results_time
  :header: method,small(1万行:665KB),middle(100万行:68.5MB),large(1億行:7.05GB)

  mcut,0.004002(0.000703),0.307001(0.001781),30.737572(0.125166)
  msum_key3,0.087729(0.113214),1.494672(0.012172),190.174376(1.948978)
  msum_key3_presort,0.014930(0.000098),0.463388(0.001697),35.182463(0.048672)
  mhashsum_key3,0.029656(0.002965),0.805394(0.003971),56.813676(0.107048)
  msortf_key3,0.019332(0.004538),0.666170(0.004806),140.808167(0.528175)
  msortf_float2,0.083201(0.131085),1.887404(0.024765),397.061643(0.161616)


ベンチマークテストを実施した計算環境は以下の通りである。

 * PC: MacPro(2013)
 * CPU: 2.7GHz 12-Core Intel Xeon E5
 * memory: 64GB
 * hdd: USB3 HDD

参考: ベンチマークスクリプト
-----------------------------------------
参考までにベンチマークテストに利用したスクリプトを、 :numref:`bench_methods_code` に示す( |today| 時点)。

.. code-block:: python
  :linenos:
  :caption: ベンチマークスクリプト
  :name: bench_methods_code

  #!/usr/bin/env python
  # -*- coding: utf-8 -*- 
  
  import os
  import time
  import datetime
  import nysol.mcmd as nm
  
  def mcut(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.mcut(f="id,key1,key2,key3,int1,int2,float1,float2,date,time",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec

  def msortf_key1(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.msortf(f="key1",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec
  
  def msortf_key2(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.msortf(f="key1",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec
  
  def msortf_key3(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.msortf(f="key1",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec
  
  def msortf_float2(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.msortf(f="float2%n",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec
  
  def msum_key3(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.msum(k="key3",f="int1,int2,float1,float2",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec
  
  def msum_key3_presort(iFile,loop):
    nm.msortf(f="key3",i=iFile,o="sorted").run()
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.msum(k="key3",f="int1,int2,float1,float2",i="sorted",o="oFile").run()
      sec.append(time.time()-st)
    return sec
  
  
  def mhashsum_key3(iFile,loop):
    sec=[]
    for i in range(loop):
      st=time.time()
      nm.mhashsum(k="key3",f="int1,int2,float1,float2",i=iFile,o="oFile").run()
      sec.append(time.time()-st)
    return sec
  
  
  ##########################################################################
  # functions for benchmark test
  ##########################################################################
  # calculate actual execution time for each method
  # iFile
  # method,dataSize,mean,sd
  # mcut,10000,0.004002,0.000703
  # mcut,1000000,0.307001,0.001781
  # oFile
  # method,small,middle,large
  # mcut,0.004002(0.000703),0.307001(0.001781),30.737572(0.125166)
  # msum_key3,0.087729(0.113214),1.494672(0.012172),190.174376(1.948978)
  # msum_key3_presort,0.014930(0.000098),0.463388(0.001697),35.182463(0.048672)
  def calTime(iFile,oFile):
    f=None
    f <<= nm.mnumber(q=True, a="id", i=iFile)
    f <<= nm.mcal(c='$s{mean}+"("+$s{sd}+")"', a="time")
    f <<= nm.m2cross(k="method",s="dataSize",f="time")
    f <<= nm.msortf(f="id%n")
    f <<= nm.mcut(f="method,10000:small,1000000:middle,100000000:large")
    f <<= nm.mfldname(q=True,o=oFile)
    f.run()
  
  # calculate relative execution time to "mcut" method for each method
  # iFile
  # method,dataSize,mean,sd
  # mcut,10000,0.004002,0.000703
  # mcut,1000000,0.307001,0.001781
  # oFile
  # mcut,1,1,1
  # msum_key3,21.9,4.9,6.2
  # msum_key3_presort,3.7,1.5,1.1
  # mhashsum_key3,7.4,2.6,1.8
  def calRelative(iFile,oFile):
    mcut=None
    mcut <<= nm.mselstr(f="method",v="mcut", i="methods.csv")
  
    f=None
    f <<= nm.mnumber(q=True, a="id", i=iFile)
    f <<= nm.mjoin(k="dataSize",m=mcut,f="mean:base")
    f <<= nm.mcal(c='round(${mean}/${base},0.1)', a="score")
    f <<= nm.m2cross(k="method",s="dataSize",f="score")
    f <<= nm.msortf(f="id%n")
    f <<= nm.mcut(f="method,10000:small,1000000:middle,100000000:large")
    f <<= nm.mfldname(q=True,o=oFile)
    f.run()

  # calculate mean and SD of multiple executions
  def cal(sec):
    mean=0
    for s in sec:
      mean+=s
    mean/=len(sec)
    sd=0
    for s in sec:
      sd+=(s-mean)**2
    sd/=(len(sec)-1)
    sd=sd**(1/2)
    return mean,sd
  
  ################
  # entry point
  
  iPath="./DATA"
  loop=5
  small =10000
  middle=1000000
  large =100000000
  funcs=[]
  funcs.append("mcut")
  funcs.append("msum_key3")
  funcs.append("msum_key3_presort")
  funcs.append("mhashsum_key3")
  funcs.append("msortf_key3")
  funcs.append("msortf_float2")
  
  with open("methods.csv","w") as fpw:
    fpw.write("method,dataSize,mean,sd\n")
    for func in funcs:
      for size in [small,middle,large]:
        iFile="%s/%d.csv"%(iPath,size)
        name="%s_%s"%(func,size)
        print("START:",name)
        sec=eval(func+'("%s",%d)'%(iFile,loop))
        print("tm",sec)
        mean,sd=cal(sec)
        fpw.write("%s,%s,%f,%f\n"%(func,size,mean,sd))
  
  today = datetime.date.today().strftime('%Y%m%d')
  calTime("methods.csv","time_%s.csv"%today)
  calRelative("methods.csv","score_%s.csv"%today)
  
  os.system("output files: methods.csv, time.csv, score.csv")
  
