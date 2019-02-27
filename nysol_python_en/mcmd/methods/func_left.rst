left 先頭切り出し
----------------------

* 書式1: left(str,長さ) 
* 書式2: leftw(str,長さ) 


文字列 :math:`str` について先頭から長さパラメータで指定した文字数を切り出す。
マルチバイト文字を含む場合はleftwを使うこと。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,str
    1,abcdefg
    2,12345678
    3,
    4,12
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,str
    1,あいうえお
    2,1あ2345678
    3,1あ
    4,ああ
    ''')


**基本例**

str項目の先頭から3文字を切り出す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='left($s{str},3)', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,abcdefg,abc
    # 2,12345678,123
    # 3,,
    # 4,12,12


**マルチバイト文字を含む例**

マルチバイト文字を含む場合はleftwを使う。

  .. code-block:: python
    :linenos:

    nm.mcal(c='leftw($s{str},3)', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str,rsl
    # 1,あいうえお,あいう
    # 2,1あ2345678,1あ2
    # 3,1あ,1あ
    # 4,ああ,ああ


