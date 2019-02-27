binomdist 二項分布の累積確率
--------------------------------------

* 書式1: binomdist(成功回数k,試行回数n,成功確率p) 


試行回数 :math:`n` 、成功確率 :math:`p` の二項分布 :math:`B(n,p)` に従う確率変数 :math:`X` について、
累積確率 :math:`P[X\le k]` を計算する。
:math:`k,n,p` は、定数としても項目として与えることができる。
なお、 :math:`k>n` や :math:`p<0,p>1` の場合の計算結果はnullとなる。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''k,n,p
    0,2,0.5
    1,2,0.5
    2,2,0.5
    4,10,0.2
    40,100,0.2
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='binomdist(${k},${n},${p})', a='prob', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # k,n,p,prob
    # 0,2,0.5,0.25
    # 1,2,0.5,0.75
    # 2,2,0.5,1
    # 4,10,0.2,0.9672065024
    # 40,100,0.2,0.9999987078


