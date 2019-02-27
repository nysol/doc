log2 底が2の対数
----------------------

* 書式1: log2(num) 


:math:`num` について2を底とする対数を計算する。


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
    2,256
    3,
    4,0
    5,1
    6,-8
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='log2(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,10,3.321928095
    # 2,256,8
    # 3,,
    # 4,0,
    # 5,1,0
    # 6,-8,


