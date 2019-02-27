cat 文字列併合
------------------

* 書式1: cat(token,str_1,str_2,...) 


:math:`token` を区切り文字として、指定された :math:`str_i` をその順番に併合して一つの文字列を生成する。
:math:`token` として空文字 ``""`` を指定すれば、文字列の単純な結合となる。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,str1,str2,str3
    1,abc,def,ghi
    2,A,,CDE
    3,,,
    4,,,XY
    ''')


**基本例**

3つの項目str1,str2,str3を ``"#"`` の区切り文字を挿入して併合する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='cat("#",$s{str1},$s{str2},$s{str3})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str1,str2,str3,rsl
    # 1,abc,def,ghi,abc#def#ghi
    # 2,A,,CDE,A##CDE
    # 3,,,,##
    # 4,,,XY,##XY


**tokenが空文字の場合**


  .. code-block:: python
    :linenos:

    nm.mcal(c='cat("",$s{str1},$s{str2},$s{str3})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str1,str2,str3,rsl
    # 1,abc,def,ghi,abcdefghi
    # 2,A,,CDE,ACDE
    # 3,,,,
    # 4,,,XY,XY


**ワイルドカードを利用した例**

``str`` から始まる項目( ``str1,str2,str3`` )をワイルドカード「 ``str*`` 」によって指定している。

  .. code-block:: python
    :linenos:

    nm.mcal(c='cat("",$s{str*})', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,str1,str2,str3,rsl
    # 1,abc,def,ghi,abcdefghi
    # 2,A,,CDE,ACDE
    # 3,,,,
    # 4,,,XY,XY


