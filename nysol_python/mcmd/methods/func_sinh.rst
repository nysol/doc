sinh 双曲線正弦
--------------------

* 書式1: sinh(r) 


双曲線正弦 (ハイパーボリック サイン) を計算する。


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

    nm.mcal(c='sinh(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.141592,11.54873178
    # 2,-1.047197,-1.249366168
    # 3,,
    # 4,6.283185,267.7448118


