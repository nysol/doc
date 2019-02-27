abs 絶対値
--------------

* 書式1: abs(num) 


:math:`num` の絶対値を計算する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,1.0
    2,-2.5
    3,
    4,0
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='abs(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,1.0,1
    # 2,-2.5,2.5
    # 3,,
    # 4,0,0


