bottom 終端行
--------------------

* 書式1: bottom() 


終端行であれば真を、そうでなければ偽を返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''val
    1
    2
    3
    4
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='bottom()', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # val,rsl
    # 1,0
    # 2,0
    # 3,0
    # 4,1


