round 四捨五入
--------------------

* 書式1: round(num,基数) 


:math:`num` を四捨五入によりまるめる。
この時、基数の整数倍の値集合のうち最も近い値にまるめられる。
例えば、round(3.82,0.5)の場合、0.5とびに目盛がうたれた数直線上で、
3.82に最も近い目盛点、すなわち4.0が基数0.5における四捨五入点となる。
基数を省略すると1.0がデフォルト値として用いられる。
これは小数点以下1桁目を四捨五入して整数値にまるめることに等しい。


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

小数点以下一桁目を四捨五入する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='round(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,3.28,3
    # 2,3.82,4
    # 3,,
    # 4,-0.6,-1


**基本例**

小数点以下二桁目を四捨五入する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='round(${val},0.1)', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,val,rsl
    # 1,3.28,3.3
    # 2,3.82,3.8
    # 3,,
    # 4,-0.6,-0.6


**基数0.5の例**

0.5を基数として四捨五入する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='round(${val},0.5)', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,val,rsl
    # 1,3.28,3.5
    # 2,3.82,4
    # 3,,
    # 4,-0.6,-0.5


**基数10の例**

一桁目を四捨五入する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='round(${val},10)', a='rsl', i="dat2.csv", o="rsl4.csv").run()
    ### rsl4.csv の内容
    # id,val,rsl
    # 1,1341.28,1340
    # 2,188,190
    # 3,1.235E+3,1240
    # 4,-1.235E+3,-1230


