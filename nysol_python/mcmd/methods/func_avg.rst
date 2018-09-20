avg 平均
------------

* 書式1: avg(num_1,num_2,...) 
* 書式2: avg(num_1,num_2,...,str) 


:math:`num_i` で与えられた数値の平均を計算する。
書式1では、NULL値は無視されるが、全てがNULL値であれば結果もNULLとなる。
書式2において最後の引数として"-n"を与えると、
NULL値に対する扱いが変わり、
項目値に一つでもNULL値がある場合は、結果もNULL値となる。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,v1,v2,v3
    1,1,2,3
    2,-5,2,1
    3,1,,3
    4,,,
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='avg(${v1},${v2},${v3})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,v1,v2,v3,rsl
    # 1,1,2,3,2
    # 2,-5,2,1,-0.6666666667
    # 3,1,,3,2
    # 4,,,,


**ワイルドカードを利用した例**

``v`` から始まる項目( ``v1,v2,v3`` )をワイルドカード「 ``v*`` 」によって指定している。

  .. code-block:: python
    :linenos:

    nm.mcal(c='avg(${v*})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,v1,v2,v3,rsl
    # 1,1,2,3,2
    # 2,-5,2,1,-0.6666666667
    # 3,1,,3,2
    # 4,,,,


**-nを利用した例**

``v2`` にNULL値を含む ``id=3`` の行の結果もNULLとなる。

  .. code-block:: python
    :linenos:

    nm.mcal(c='avg(${v1},${v2},${v3},"-n")', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,v1,v2,v3,rsl
    # 1,1,2,3,2
    # 2,-5,2,1,-0.6666666667
    # 3,1,,3,
    # 4,,,,


