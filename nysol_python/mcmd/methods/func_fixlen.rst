fixlen 固定長変換
------------------------

* 書式1: fixlen(str,長さ,位置,padding文字) 
* 書式2: fixlenw(str,長さ,位置,padding文字) 


:math:`str` を固定の長さの文字列に変換する。
:math:`str` が指定の長さに満たない場合は、
右詰もしくは左詰めで指定した文字を埋め込む。
左右の選択では、「位置」パラメータに ``"L"`` もしくは ``"R"`` を指定する。
埋め込む文字は「padding文字」パラメータに任意の文字を指定する。
また、 :math:`str` の長さが、指定した固定長の長さを超えた場合、
右詰の場合は先頭側が、左詰めの場合は末尾側の文字列が削られることに注意する。
マルチバイト文字を対象とした固定長変換については ``fixlenw`` 関数を利用する。


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
    2,123
    3,
    4,1234567
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,str
    1,こんにちは
    2,大阪
    ''')


**基本例**

str項目を5文字の固定長文字列に変換する。
5文字に満たない文字列は右詰( ``"R"`` )で ``"#"`` を埋める。

  .. code-block:: python
    :linenos:

    nm.mcal(c='fixlen($s{str},5,"R","#")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,abc,##abc
    # 2,123,##123
    # 3,,#####
    # 4,1234567,34567


**左詰め例**

左詰( ``"L"`` )で ``"#"`` を埋める。

  .. code-block:: python
    :linenos:

    nm.mcal(c='fixlen($s{str},5,"L","#")', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str,rsl
    # 1,abc,abc##
    # 2,123,123##
    # 3,,#####
    # 4,1234567,12345


**マルチバイト文字を含む場合**


  .. code-block:: python
    :linenos:

    nm.mcal(c='fixlenw($s{str},4,"R","埋")', a='rsl', i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,str,rsl
    # 1,こんにちは,んにちは
    # 2,大阪,埋埋大阪


