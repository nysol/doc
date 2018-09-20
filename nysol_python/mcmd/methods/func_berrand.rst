berrand ベルヌーイ乱数
------------------------------

* 書式1: berrand(確率,[乱数の種]) 


ベルヌーイ分布 :math:`f(x)=p^x(1-p)^{1-x} x=0,1` について、指定された確率 :math:`p` における :math:`x` の乱数を生成する。
本関数では、 :math:`x=0` をfalse、 :math:`x=1` をtrueとした論理型として値を返す。
また確率 :math:`p` は定数としてのみ指定可能で、項目名を指定することはできない。
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


**基本例**

確率$p=0.2$のベルヌーイ乱数を生成する。
乱数の種を指定しているので、何度実行しても同じ乱数系列が生成される。

  .. code-block:: python
    :linenos:

    nm.mcal(c='berrand(0.2,111)', a='rand', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,rand
    # 1,0
    # 2,1
    # 3,1
    # 4,0


**0,1の整数乱数**

0と1の2種類の整数乱数を生成する。
乱数の種を指定していないので、実行の度に異なる乱数系列が生成される。

  .. code-block:: python
    :linenos:

    nm.mcal(c='randi(0,1)', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,rsl
    # 1,1
    # 2,1
    # 3,0
    # 4,0


