power 累乗
----------------

* 書式1: power(num,指数) 


:math:`num` の累乗を計算する。
演算子 ``^`` と等価である。
結果が実数の最大値を超えると、NULL値が出力される。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,base,exponent
    1,5,2
    2,2,8
    3,,
    4,0,10
    5,10,0
    6,2,0.5
    7,2,-1
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='power(${base},${exponent})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,base,exponent,rsl
    # 1,5,2,25
    # 2,2,8,256
    # 3,,,
    # 4,0,10,0
    # 5,10,0,1
    # 6,2,0.5,1.414213562
    # 7,2,-1,0.5


