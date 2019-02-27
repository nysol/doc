tolower 小文字変換
--------------------------



文字列をすべて小文字に変更する。
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
    1,ABC
    2,aB$12!Cd
    3,
    4,cBA
    ''')


**基本例**

$str$項目のアルファベット大文字を全て小文字に変換する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='tolower($s{str})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,ABC,abc
    # 2,aB$12!Cd,ab$12!cd
    # 3,,
    # 4,cBA,cba


