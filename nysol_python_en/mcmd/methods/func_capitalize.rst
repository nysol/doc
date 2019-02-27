capitalize 先頭文字大文字変換
----------------------------------------

* 書式1: capitalize(str) 


文字列の先頭文字のみ大文字に変更する。
アルファベット26文字以外の文字については何の影響もない。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,str
    1,abc
    2,aBd
    3,
    4,#abc
    ''')


**基本例**

$str$項目の先頭文字を大文字に変換する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='capitalize($s{str})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,abc,Abc
    # 2,aBd,ABd
    # 3,,
    # 4,#abc,#abc


