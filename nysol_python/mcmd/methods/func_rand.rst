rand 一様乱数
------------------

* 書式1: rand([乱数の種]) 


0.0〜1.0の範囲で一様乱数を生成する。
単独で利用するとその結果はmrandコマンドを ``-int`` オプションなしで実行した結果に等しい。
同じ乱数の種を指定すれば、同じ乱数系列となる。
指定可能な乱数の種の範囲は-2147483648〜2147483647である。
乱数の種を省略すると、
時刻(ミリ(1/1000秒単位)に応じた異なる乱数の種が利用される。
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


**基本例**

0.0から1.0の一様乱数を生成する。
乱数の種を指定しているので、何度実行しても同じ乱数系列が生成される。

  .. code-block:: python
    :linenos:

    nm.mcal(c='rand(1)', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,rsl
    # 1,0.4170219984
    # 2,0.9971848081
    # 3,0.7203244893
    # 4,0.9325573612


**乱数の種未指定**

乱数の種を指定していないので、実行の度に異なる乱数系列が生成される。

  .. code-block:: python
    :linenos:

    nm.mcal(c='rand()', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,rsl
    # 1,0.2873856472
    # 2,0.8765916736
    # 3,0.7697916306
    # 4,0.7824931054


