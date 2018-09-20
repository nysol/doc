sin サイン
--------------

* 書式1: sin(r) 


ラジアン :math:`r` に対するサインを計算する。


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
    2,0.523599
    3,
    4,6.283185
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='sin(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.141592,6.535897931e-07
    # 2,0.523599,0.5000001943
    # 3,,
    # 4,6.283185,-3.071795869e-07


