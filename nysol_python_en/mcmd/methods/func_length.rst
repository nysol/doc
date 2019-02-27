length 文字列長
----------------------

* 書式1: length(str) 
* 書式2: lengthw(str) 


文字列の長さを計算する。
lengthw関数を用いると、 :math:`str` をワイド文字として扱う。
NULL値の長さは0であることに注意する。


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
    2,3.1415
    3,
    4,hello world!
    ''')

    with open('dat2.csv','w') as f:
      f.write(
    '''id,str
    1,こんにちは
    2,大阪
    ''')


**基本例**


  .. code-block:: python
    :linenos:

    nm.mcal(c='length($s{str})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,abc,3
    # 2,3.1415,6
    # 3,,0
    # 4,hello world!,12


**マルチバイト文字を含む例**

以下はutf-8でエンコーディングされた日本語を用いた例である。
utf-8の日本語は1文字3バイトでエンコーディングされているので、
length関数では日本語としての文字数ではなく、そのバイト数を返す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='length($s{str})', a='rsl', i="dat2.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str,rsl
    # 1,こんにちは,15
    # 2,大阪,6


**ワイド文字として扱う例**

lengthwを使うと、内部で文字列をワイド文字に変換するので、マルチバイト文字1文字を正しく認識して計算する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='lengthw($s{str})', a='rsl', i="dat2.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,str,rsl
    # 1,こんにちは,5
    # 2,大阪,2


