heron 三角形の面積
------------------------

* 書式1: heron(タイプ,num_1,num_2,...,n_k,num_{k+1},num_{k+2},...,num_{2k},num_{2k+1},num_{2k+2},...,num_{3k}) 


k次元空間の3点の座標$(num_1,num_2,\cdots,n_k),(num_{k+1},num_{k+2},\cdots,num_{2k)}
,(num_{2k+1},num_{2k+2},\cdots,num_{3k})$によって作られる3角形の面積を計算する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,x1,y1,x2,y2,x3,y3
    1,0,0,1,0,0,1
    2,0,0,0,2,2,0
    4,,,,,,
    3,0,0,1,1,2,2
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='heron(${x1},${y1},${x2},${y2},${x3},${y3})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,x1,y1,x2,y2,x3,y3,rsl
    # 1,0,0,1,0,0,1,0.5
    # 2,0,0,0,2,2,0,2
    # 4,,,,,,,
    # 3,0,0,1,1,2,2,0


