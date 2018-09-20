sign 符号
--------------

* 書式1: sign(num) 


:math:`num` の符号を判定する。
プラスであれば1を、マイナスであれば-1を、ゼロであれば0を返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,5
    2,-5
    3,
    4,0
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='sign(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,5,1
    # 2,-5,-1
    # 3,,
    # 4,0,0


