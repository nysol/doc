hasspace 空白類文字検索
--------------------------------

* 書式1: hasspace(str,長さ) 
* 書式2: hasspacew(str,長さ) 


文字列 :math:`str` に空白類文字列が含まれていれば真を、含まれていなければ偽を返す。
空白類文字とは、ASCIIコードの0x20および0x09〜0x0dまでの事をいう。
それぞれ、半角スペース(0x20)、水平tab(0x09)、改行(0x0a)、垂直タブ(0x0b)、改ページ(0x0c)、復帰(0x0d)である。
マルチバイト文字における空白類文字を検索したければhasspacewを使うこと。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,str
    1,a b
    2,ab	c
    3,ab　c
    4,
    5,"aa
    bb"
    ''')


**基本例**

``str`` 項目に空白類文字列が含まれていれば真を返す。
``id=1`` の行は半角スペース文字が含まれ、
``id=2`` の行はtab文字が含まれ、
そして ``id=4`` の行は改行文字が含まれているために真となっている。
ここで、 ``id=3`` の行は全角スペースのため、検知できていない。

  .. code-block:: python
    :linenos:

    nm.mcal(c='hasspace($s{str})', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,a b,1
    # 2,ab	c,1
    # 3,ab　c,0
    # 4,,0
    # 5,"aa
    # bb",1


**マルチバイト文字**

hasspacew関数を使えば全角スペースも正しく検知できる。

  .. code-block:: python
    :linenos:

    nm.mcal(c='hasspacew($s{str})', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str,rsl
    # 1,a b,1
    # 2,ab	c,1
    # 3,ab　c,1
    # 4,,0
    # 5,"aa
    # bb",1


