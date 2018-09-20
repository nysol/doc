factorial 階乗
------------------------

* 書式1: factorial(num) 


:math:`num` の階乗を計算する。
結果が実数の最大値を超えると、NULL値が出力される。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,1
    2,5
    3,
    4,10000
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='factorial(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,1,1
    # 2,5,120
    # 3,,
    # 4,10000,


**定数を与える例**

5の階乗を計算する。定数を与えているので、全行同じ結果が出力される。

  .. code-block:: python
    :linenos:

    nm.mcal(c='factorial(5)', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,val,rsl
    # 1,1,120
    # 2,5,120
    # 3,,120
    # 4,10000,120


