cos コサイン
----------------

* 書式1: cos(r) 


ラジアン :math:`r` に対するコサインを計算する。


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

    nm.mcal(c='cos(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.141592,-1
    # 2,1.047197,0.5000004774
    # 3,,
    # 4,6.283185,1


