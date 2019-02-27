atan2 座標の角度
----------------------

* 書式1: atan2(num_1,num_2) 


:math:`x,y` 座標 :math:`(num_1,num_2)` と原点を結ぶ線分と :math:`x` 軸とが作る角度をラジアンで返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,x,y
    1,5,10
    2,10,20
    3,-1,0
    4,0,0
    5,,
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='atan2(${x},${y})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,x,y,rsl
    # 1,5,10,1.107148718
    # 2,10,20,1.107148718
    # 3,-1,0,3.141592654
    # 4,0,0,0
    # 5,,,


