nrand 正規乱数
--------------------

* 書式1: nrand(nrand) ([正規乱数])


指定された平均値と標準偏差による正規乱数を発生させる。
同じ乱数の種を指定すれば、同じ乱数系列となる。
指定可能な乱数の種の範囲は-2147483648〜2147483647である。
乱数の種を省略すると、
時刻(1/1000秒単位)に応じた異なる乱数の種が利用される。
乱数の生成にはメルセンヌ・ツイスター法を利用している
(\href{http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html}{原作者のページ}
, \href{http://www.boost.org/doc/libs/1_54_0/doc/html/boost_random.html}{boostライブラリ})。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id
    1
    2
    3
    4
    ''')


**例1: 基本例**

平均 0 標準偏差 1(標準正規分布) に基づく乱数を成する。また、乱数の種は 10 に設定している。

  .. code-block:: python
    :linenos:

    nm.mcal(c='nrand(0,1,10)', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,rsl
    # 1,1.161957445
    # 2,-0.7429729875
    # 3,-1.10165004
    # 4,1.03149223


