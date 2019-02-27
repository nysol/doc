tan タンジェント
--------------------

* 書式1: tan(r) 


ラジアン :math:`r` に対するタンジェントを計算する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,0.785398
    2,1.047197
    3,
    4,3.141593
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='tan(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,0.785398,0.9999996732
    # 2,1.047197,1.732048603
    # 3,,
    # 4,3.141593,3.464102066e-07


