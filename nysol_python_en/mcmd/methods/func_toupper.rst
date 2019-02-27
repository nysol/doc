toupper 大文字変換
--------------------------



文字列をすべて大文字に変更する。
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
    2,Ab$12!cD
    3,
    4,Cba
    ''')


**基本例**

$str$項目のアルファベット小文字を全て大文字に変換する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='toupper($s{str})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,abc,ABC
    # 2,Ab$12!cD,AB$12!CD
    # 3,,
    # 4,Cba,CBA


