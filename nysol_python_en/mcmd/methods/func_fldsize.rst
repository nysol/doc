fldsize 項目数
----------------------

* 書式1: fldsize() 


入力データの項目数を返す。
mcmdでは全行同じ項目数を想定しているので、この関数の結果は全行同じ値になる。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''a,b,c,d
    1,2,3,4
    2,3,4,5
    3,,,
    4,x,y,z
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='fldsize()', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # a,b,c,d,rsl
    # 1,2,3,4,4
    # 2,3,4,5,4
    # 3,,,,4
    # 4,x,y,z,4


