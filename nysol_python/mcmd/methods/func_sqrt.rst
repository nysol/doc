sqrt 平方根
----------------

* 書式1: sqrt(num) 


:math:`num` の平方根を求める。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,9
    2,2
    3,
    4,-1
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='sqrt(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,9,3
    # 2,2,1.414213562
    # 3,,
    # 4,-1,


