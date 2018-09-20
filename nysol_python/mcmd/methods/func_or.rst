or 論理和
------------

* 書式1: or(bool_1,bool_2,...) 


:math:`bool_i` で与えられた真偽値全ての論理和を計算する。
NULL値を含めた真偽値表は表ef{tbl:mcal_or}を参照のこと。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,b1,b2,b3
    1,1,0,0
    2,1,,1
    3,0,,0
    4,0,0,0
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='or($b{b1},$b{b2},$b{b3})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,b1,b2,b3,rsl
    # 1,1,0,0,1
    # 2,1,,1,1
    # 3,0,,0,
    # 4,0,0,0,0


**ワイルドカードを利用した例**

``b`` から始まる項目( ``b1,b2,b3`` )をワイルドカード「 ``b*`` 」によって指定している。

  .. code-block:: python
    :linenos:

    nm.mcal(c='or($b{b*})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,b1,b2,b3,rsl
    # 1,1,0,0,1
    # 2,1,,1,1
    # 3,0,,0,
    # 4,0,0,0,0


