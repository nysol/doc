argsize 引数の数
------------------------

* 書式1: argsize(str_1,str_2,...) 


:math:`str_i` で与えられた文字列の数を返す。
ワイルドカードをで項目名を指定することで意味が出てくる。
すなわちワイルドカード条件を満たす多数の項目の数をカウントすることができる。
データ型としては文字列型のみに対応していることに注意する。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,v1,v2,v3
    1,1,2,3
    2,-5,2,1
    3,1,,3
    4,,,
    ''')


**基本例**

``"v"`` で始まる項目名の数を数える。

  .. code-block:: python
    :linenos:

    nm.mcal(c='argsize($s{v*})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,v1,v2,v3,rsl
    # 1,1,2,3,3
    # 2,-5,2,1,3
    # 3,1,,3,3
    # 4,,,,3


