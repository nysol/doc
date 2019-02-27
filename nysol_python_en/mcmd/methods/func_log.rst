log 対数
------------

* 書式1: log(num,底) 


:math:`num` についての指定された底の対数を計算する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val,base
    1,100,10
    2,256,2
    3,,
    4,2,0
    5,0,2
    6,1,10
    7,-8,2
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='log(${val},${base})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,base,rsl
    # 1,100,10,2
    # 2,256,2,8
    # 3,,,
    # 4,2,0,-0
    # 5,0,2,
    # 6,1,10,0
    # 7,-8,2,


