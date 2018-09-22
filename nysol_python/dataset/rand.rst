mcmdベンチマーク用乱数データセット
====================================================
「:doc:`../bench/methods` 」の節で解説されている、
mcmd処理メソッドの処理速度に関するベンチマークテストで用いられているデータセットである。
データイメージは :numref:`dataset_rand_data` に示される通りで。
``id`` , ``key1`` , ``key2`` , ``key3`` , ``int1`` , ``int2`` , ``float1`` , ``float2`` , ``date`` , ``time``
の10項目から構成されるデータセットである。
全ての項目はランダムに生成されたもので、その概要を :numref:`dataset_rand_field` に示している。

.. csv-table:: 乱数データセット
  :name: dataset_rand_data
  :header: id,key1,key2,key3,int1,int2,float1,float2,date,time

  0,0,982,31795,516,224,0.09428928373,-10.87915357,20190608,100405
  1,4,747,24803,552,-758,0.02317879722,-14.61856635,20150122,084221
  2,9,839,92127,570,-662,0.2467738762,81.67126765,20101120,030642
  3,2,546,67524,952,-396,0.8956414664,93.21300858,20121117,223858
  4,3,681,74869,28,-128,0.9464241466,-85.74571619,20161213,023745
  :,:, : ,   : , :,  : ,       :    ,      :     ,    :   ,   :

.. list-table:: データの生成方法
  :header-rows: 1
  :name: dataset_rand_field

  * - 項目名
    - 生成方法
  * - id
    - 先頭行から0,1,2,...の整数を振ったもの。
  * - key1
    - キーブレイク処理用の項目で、0〜9の10種の一様乱数を生成。1桁固定長。
  * - key2
    - キーブレイク処理用の項目で、100〜999の900種の一様乱数を生成。3桁固定長。
  * - key3
    - キーブレイク処理用の項目で、10000〜99999の9万種の一様乱数を生成。5桁固定長。
  * - int1
    - 集計用の整数項目で、0〜999の一様乱数を生成。
  * - int2
    - 集計用の整数項目で、-999〜999の一様乱数を生成。
  * - float1
    - 集計用の実数項目で、0〜1の一様乱数を生成。
  * - float2
    - 集計用の実数項目で、-100〜100の一様乱数を生成。
  * - date
    - 日付計算用の項目で、2010年1月1日を基準に、0〜3650日の乱数を加算したもの。
  * - time
    - 時刻計算用の項目で、0時0分0秒を基準に0〜86399秒の乱数を加算したもの。

データ生成のスクリプトを :numref:`dataset_rand_mkdata` に示す。
このスクリプトを実行すると、 :numref:`dataset_rand_files` に示されるような
サイズ違いの3つのデータが ``./DATA`` に生成される。
10分ほどの時間を要する。

  .. code-block:: python
    :linenos:
    :caption: ランダムデータの生成するスクリプト ``mkdata.py``
    :name: dataset_rand_mkdata

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- 

    import os
    import nysol.mcmd as nm
    
    # generate random data
    # id,key1,key2,key3,int1,int2,float1,float2,date,time
    def mkdata(rowSize,oFile):
      f=None
      f <<= nm.mnewnumber(a="id", l=rowSize)
      f <<= nm.mrand(min=0   ,max=9     ,int=True,S=1111,a="key1")
      f <<= nm.mrand(min=100 ,max=999   ,int=True,S=1113,a="key2")
      f <<= nm.mrand(min=10000,max=99999,int=True,S=1117,a="key3")
      f <<= nm.mcal(c='randi(0,999,101)',   a="int1")
      f <<= nm.mcal(c='randi(-999,999,111)',a="int2")
      f <<= nm.mcal(c='rand(991)',          a="float1")
      f <<= nm.mcal(c='rand(997)*200-100',  a="float2")
      f <<= nm.mcal(c='0d20100101+randi(0,3650,137)',    a="date")
      f <<= nm.mcal(c='right(t2s(0t000000+randi(0,86399,133)),6)', a="time", o=oFile)
      f.run()
    
    oPath="./DATA"
    os.system("mkdir -p %s"%oPath)
    
    for size in [10000,1000000,100000000]:
      mkdata(size, "%s/%s.csv"%(oPath,size))
    

.. list-table:: 生成されるデータ一覧
  :header-rows: 1
  :name: dataset_rand_files

  * - 名称
    - ファイル名
    - 行数(ヘッダ除く)
    - サイズ(MB)
  * - small
    - 10000.csv
    - 10000
    - 665 KB
  * - middle
    - 1000000.csv
    - 1000000
    - 68 MB
  * - large
    - 100000000.csv
    - 100000000
    - 7056 MB

