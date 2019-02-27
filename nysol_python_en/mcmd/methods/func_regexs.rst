regexs マッチ
--------------------

* 書式1: regexs(str,正規表現) 
* 書式2: regexsw(str,正規表現) 


指定した正規表現が、文字列 :math:`str` の一部にでもマッチすれば真を返す。
:math:`str` もしくは正規表現にマルチバイト文字を含み、
Shift\_JISなど文字の出現順によっては意に沿わない検索結果となる場合はregexsw関数を使うこと。


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
    4,cbcbcc
    ''')


**基本例**

``id=1,id=2`` 共に、正規表現で示された ``c`` に続く ``aa`` を含んでいるので真を返す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexs($s{str},"c.*aa")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,caabaa,1
    # 2,acabaaa,1
    # 3,,0
    # 4,cbcbcc,0


**先頭一致**

正規表現 ``.*c`` を$str$項目が含むのは ``id=3`` 以外全ての行である。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexs($s{str},".*c")', a='rsl', i="dat1.csv", o="rsl2.csv").run()
    ### rsl2.csv の内容
    # id,str,rsl
    # 1,caabaa,1
    # 2,acabaaa,1
    # 3,,0
    # 4,cbcbcc,1


