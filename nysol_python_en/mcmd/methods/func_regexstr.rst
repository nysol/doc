regexstr マッチ文字列
------------------------------

* 書式1: regexstr(str,正規表現) 
* 書式2: regexstrw(str,正規表現) 


指定した正規表現が最長マッチする文字列 :math:`str` の部分文字列を返す。
:math:`str` もしくは正規表現にマルチバイト文字を含み、
Shift\_JISなど文字の出現順によっては意に沿わない検索結果となる場合はregexstrw関数を使うこと。


利用例
''''''''''''

**importと入力データ(CSV)の準備**

  .. code-block:: python
    :linenos:

    import nysol.mcmd as nm

    with open('dat1.csv','w') as f:
      f.write(
    '''id,str
    1,xcbbbayy
    2,xxcbaay
    3,
    4,bacabbca
    ''')


**基本例**

正規表現 ``c.*a`` に最も長くマッチする部分文字列を得る。
``id=2`` では、 ``cba`` もしくは ``cbaa`` いずれの部分文字列にもマッチしたと考えることができるが、
本関数では、より長くマッチした文字列を返す。

  .. code-block:: python
    :linenos:

    nm.mcal(c='regexstr($s{str},"c.*a")', a='rsl', i="dat1.csv", o="rsl1.csv").run()
    ### rsl1.csv の内容
    # id,str,rsl
    # 1,xcbbbayy,cbbba
    # 2,xxcbaay,cbaa
    # 3,,
    # 4,bacabbca,cabbca


