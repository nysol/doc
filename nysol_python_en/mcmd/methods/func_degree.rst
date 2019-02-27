degree 角度
------------------

* 書式1: degree(r) 


ラジアン :math:`r` に対応する角度を計算する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,3.141592
    2,1.047197
    3,
    4,6.283185
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='degree(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.141592,179.9999626
    # 2,1.047197,59.99996842
    # 3,,
    # 4,6.283185,359.9999824


