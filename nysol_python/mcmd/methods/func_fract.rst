fract 小数部
------------------

* 書式1: fract(num) 


:math:`num` の小数部を返す。
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

    nm.mcal(c='fract(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.14,0.14
    # 2,3,0
    # 3,,
    # 4,-12.56789,-0.56789
    # 5,1.2345e+2,0.45
    # 6,1.2345e-10,1.2345e-10


