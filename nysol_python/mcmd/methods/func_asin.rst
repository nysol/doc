asin サインの逆関数
------------------------

* 書式1: asin(num) 


アークサイン(サインの逆関数)を計算する。
パラメータの範囲は :math:`-1.0\sim 1.0` で戻り値の範囲は :math:`-\pi/2\sim \pi/2` である。


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
    5,2
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='asin(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,-1.0,-1.570796327
    # 2,0,0
    # 3,1.0,1.570796327
    # 4,,
    # 5,2,


