lcm 最小公倍数
------------------

* 書式1: lcm(num_1,num_2) 


:math:`num_1` と :math:`num_2` の最小公倍数を求める。
実数は整数に変換して(切り下げ)実行される。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val1,val2
    1,5,3
    2,12,4
    3,,
    4,5.1,3.1
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='lcm(${val1},${val2})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val1,val2,rsl
    # 1,5,3,15
    # 2,12,4,12
    # 3,,,
    # 4,5.1,3.1,15


**定数を与える例**

val1項目と15の最小公倍数を求める。

  .. code-block:: python
    :linenos:

    nm.mcal(c='lcm(${val1},15)', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,val1,val2,rsl
    # 1,5,3,15
    # 2,12,4,60
    # 3,,,
    # 4,5.1,3.1,15


