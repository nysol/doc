mid 部分文字列切り出し
--------------------------

* 書式1: mid(str,開始位置,長さ) 
* 書式2: midw(str,開始位置,長さ) 


文字列 :math:`str` の指定した開始位置から長さ分を切り出す。
開始位置は0から始まることに注意する。
マルチバイト文字を含む場合はmidwを使うこと。


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
    2,1234567あ8
    3,1あ
    4,ああ
    ''')


**基本例**

str項目の2文字目からから3文字を切り出す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='mid($s{str},2,3)', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,abcdefg,cde
    # 2,12345678,345
    # 3,,
    # 4,12,


**基本例**

マルチバイト文字を含む場合はmidwを使う。

  .. code-block:: python
    :linenos:

    nm.mcal(c='midw($s{str},2,3)', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str,rsl
    # 1,あいうえお,うえお
    # 2,1234567あ8,345
    # 3,1あ,
    # 4,ああ,


