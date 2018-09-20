countnull 合計
------------------------

* 書式1: countnull(num_1,num_2,...) 
* 書式2: countnull(str_1,str_2,...) 
* 書式3: countnull(date_1,date_2,...) 
* 書式4: countnull(time_1,time_2,...) 
* 書式5: countnull(bool_1,bool_2,...) 


:math:`num_i` (その他の型も同様)で与えられた数値の中でNULL値の数を返す。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''a,b,c,d
    1,,3,4
    1,,,
    ,,,
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='countnull(${a},${b},${c},${d})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # a,b,c,d,rsl
    # 1,,3,4,1
    # 1,,,,3
    # ,,,,4


**他の項目型として項目名をワイルドカードで指定**


  .. code-block:: python
    :linenos:

    nm.mcal(c='countnull($s{*})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # a,b,c,d,rsl
    # 1,,3,4,1
    # 1,,,,3
    # ,,,,4


