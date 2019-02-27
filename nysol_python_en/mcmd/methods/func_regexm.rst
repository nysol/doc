regexm 全体マッチ
------------------------

* 書式1: regexm(str,正規表現) 
* 書式2: regexmw(str,正規表現) 


指定した正規表現が、文字列 :math:`str` 全体にマッチすれば真を返す。
:math:`str` もしくは正規表現にマルチバイト文字を含み、
Shift\_JISなど文字の出現順によっては意に沿わない検索結果となる場合はregexmw関数を使うこと。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,str
    1,caabaa
    2,acabaaa
    3,
    4,bbcbcc
    ''')


**基本例**

``id=1,id=2`` 共に、正規表現で示された ``c`` に続く ``aa`` を含んでいるが、
``id=2`` ではマッチする範囲が部分的(2文字目の ``c`` から最後まで)であるために偽となっている。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexm($s{str},"c.*aa")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,caabaa,1
    # 2,acabaaa,0
    # 3,,0
    # 4,bbcbcc,0


**末尾一致**

正規表現 ``.*c`` で$str$項目の全体がカバーされるのは ``id=4`` の行のみである。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexm($s{str},".*c")', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str,rsl
    # 1,caabaa,0
    # 2,acabaaa,0
    # 3,,0
    # 4,bbcbcc,1


**空文字マッチ**

正規表現 ``^$`` で ``id=3`` の空文字にマッチする。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexm($s{str},"^$")', a='rsl', i="dat1.csv", o="rsl3.csv").run()
    ### rsl3.csv の内容
    # id,str,rsl
    # 1,caabaa,0
    # 2,acabaaa,0
    # 3,,1
    # 4,bbcbcc,0


