exp 指数関数
----------------

* 書式1: exp(num) 


power関数の特殊形で、 :math:`e` (ネイピア数)を底とする :math:`num` 乗を計算する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,exponent
    1,1
    2,-1
    3,
    4,0
    5,0.5
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='exp(${exponent})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,exponent,rsl
    # 1,1,2.718281828
    # 2,-1,0.3678794412
    # 3,,
    # 4,0,1
    # 5,0.5,1.648721271


