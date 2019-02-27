radian ラジアン
----------------------

* 書式1: radian(角度) 


角度をラジアンに変換する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,60
    2,180
    3,
    4,0
    5,-90
    ''')


**例1: 基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='radian(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,60,1.047197551
    # 2,180,3.141592654
    # 3,,
    # 4,0,0
    # 5,-90,-1.570796327


