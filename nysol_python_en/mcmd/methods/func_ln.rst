ln 自然対数
--------------

* 書式1: ln(num,底) 


:math:`num` の自然対数を計算する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,10
    2,2.718281828
    3,
    4,0
    5,1
    6,-8
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='ln(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,10,2.302585093
    # 2,2.718281828,0.9999999998
    # 3,,
    # 4,0,
    # 5,1,0
    # 6,-8,


