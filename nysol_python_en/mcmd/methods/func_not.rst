not 否定
------------

* 書式1: not(bool) 


:math:`bool` で与えられた真偽値の否定を返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,b
    1,1
    2,
    3,0
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='not($b{b})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,b,rsl
    # 1,1,0
    # 2,,
    # 3,0,1


