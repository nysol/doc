regexrep マッチ文字列の置換
------------------------------------

* 書式1: regexrep(str,正規表現,置換文字列) 
* 書式2: regexrepw(str,正規表現,置換文字列) 


指定した正規表現が最長マッチした文字列 :math:`str` の部分文字列を置換文字列で置換する。
:math:`str` もしくは正規表現にマルチバイト文字を含み
Shift\_JISなど文字の出現順によっては意に沿わない検索結果となる場合はregexrepw関数を使うこと。


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

``id=1,id=2`` の$str$項目にマッチした部分文字列を ``MMM`` に置換する。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexrep($s{str},"c.*aa","MMM")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,caabaa,MMM
    # 2,acabaaa,aMMM
    # 3,,
    # 4,cbcbcc,cbcbcc


