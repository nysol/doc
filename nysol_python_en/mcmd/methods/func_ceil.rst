ceil 切り上げ
------------------

* 書式1: ceil(num,基数) 


:math:`num` を切り上げにより丸める。
この時、基数の整数倍の値集合のうち、 :math:`num` より大きい最小の目盛点にまるめられる。
例えば、ceil(3.42,0.5)の場合、0.5とびに目盛がうたれた数直線上で、
3.42より大きい最小の目盛点、すなわち3.5が基数0.5における切り上げ点となる。
基数を省略すると1.0がデフォルト値として用いられる。
これは小数点以下1桁目を切り上げて整数値にまるめることに等しい。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,3.28
    2,3.82
    3,
    4,-0.6
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,val
    1,1341.28
    2,188
    3,1.235E+3
    4,-1.235E+3
    ''')


**基本例**

小数点以下一桁目を切り上げる。

  .. code-block:: python
    :linenos:

    nm.mcal(c='ceil(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.28,4
    # 2,3.82,4
    # 3,,
    # 4,-0.6,-0


**基本例**

小数点以下二桁目を切り上げる。

  .. code-block:: python
    :linenos:

    nm.mcal(c='ceil(${val},0.1)', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,val,rsl
    # 1,3.28,3.3
    # 2,3.82,3.9
    # 3,,
    # 4,-0.6,-0.5


**基数0.5の例**

0.5を基数として切り上げる。

  .. code-block:: python
    :linenos:

    nm.mcal(c='ceil(${val},0.5)', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,val,rsl
    # 1,3.28,3.5
    # 2,3.82,4
    # 3,,
    # 4,-0.6,-0.5


**基数10の例**

一桁目を切り上げる。

  .. code-block:: python
    :linenos:

    nm.mcal(c='ceil(${val},10)', a='rsl', i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,val,rsl
    # 1,1341.28,1350
    # 2,188,190
    # 3,1.235E+3,1240
    # 4,-1.235E+3,-1230


