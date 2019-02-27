cosh 双曲線余弦
--------------------

* 書式1: cosh(r) 


双曲線余弦 (ハイパーボリック コサイン) を計算する。


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
    2,-1.047197
    3,
    4,6.283185
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='cosh(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.141592,11.59194573
    # 2,-1.047197,1.600286169
    # 3,,
    # 4,6.283185,267.7466792


