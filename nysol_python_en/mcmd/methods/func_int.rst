int 整数部
--------------

* 書式1: int(num) 


:math:`num` の整数部を返す。
符号はそのまま出力される。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,3.14
    2,3
    3,
    4,-12.56789
    5,1.2345e+2
    6,1.2345e-10
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='int(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.14,3
    # 2,3,3
    # 3,,
    # 4,-12.56789,-12
    # 5,1.2345e+2,123
    # 6,1.2345e-10,0


