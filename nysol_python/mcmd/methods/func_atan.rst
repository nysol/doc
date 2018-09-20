atan タンジェントの逆関数
------------------------------

* 書式1: atan(num) 


アークタンジェント(タンジェントの逆関数)を計算する。
パラメータの範囲は :math:`-\infty\sim \infty` で戻り値の範囲は :math:`-\pi/2 \sim \pi/2` である。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,-1.0
    2,0
    3,1.0
    4,
    5,1.0e+10
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='atan(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,-1.0,-0.7853981634
    # 2,0,0
    # 3,1.0,0.7853981634
    # 4,,
    # 5,1.0e+10,1.570796327


