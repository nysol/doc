pi 円周率
------------

* 書式1: pi() 


円周率( :math:`\pi` )を出力する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id
    1
    2
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='pi()', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,rsl
    # 1,3.141592654
    # 2,3.141592654


