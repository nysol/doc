isnull NULL値判定
----------------------------

* 書式1: isnull,isnull,isnull,isnull,isnull(bool) 


:math:`num` (他のデータ型も同様)で与えられた値がNULL値であるかどうかを判定する。
NULL値であれば ``0b1`` (真)を、そうでなければ ``0b0`` (偽)を返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,val
    1,a
    2,
    3,b
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='isnull(${val})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,val,rsl
    # 1,a,0
    # 2,,1
    # 3,b,0


**他の項目型も指定可能**


  .. code-block:: python
    :linenos:

    nm.mcal(c='isnull($s{val})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,val,rsl
    # 1,a,0
    # 2,,1
    # 3,b,0


**空文字を定数で与えた場合**


  .. code-block:: python
    :linenos:

    nm.mcal(c='isnull("")', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,val,rsl
    # 1,a,1
    # 2,,1
    # 3,b,1


